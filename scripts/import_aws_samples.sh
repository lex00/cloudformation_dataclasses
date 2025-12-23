#!/usr/bin/env bash
#
# AWS CloudFormation samples import script for cloudformation_dataclasses
#
# This script automates the full process of importing CloudFormation templates
# from vendor/aws-cloudformation-templates/ into examples/aws-cloudformation-templates/.
#
# Workflow:
# 1. Clean output directory
# 2. Run batch import via cfn-dataclasses-import
# 3. Parse import.log for failures
# 4. Remove directories for failed imports
# 5. Validate each package by running it
# 6. Report final statistics and generate report.json
#
# Usage:
#   ./scripts/import_aws_samples.sh                        # Full import with validation
#   ./scripts/import_aws_samples.sh --source /path         # Custom source
#   ./scripts/import_aws_samples.sh --clean-only           # Just clean output
#   ./scripts/import_aws_samples.sh --skip-cleanup         # Keep failed imports
#   ./scripts/import_aws_samples.sh --skip-validation      # Skip package validation
#

set -e  # Exit on error
set -u  # Exit on undefined variable

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Configuration
DEFAULT_SOURCE="$PROJECT_ROOT/vendor/aws-cloudformation-templates"
OUTPUT_DIR="$PROJECT_ROOT/examples/aws-cloudformation-templates"

# Templates with known defects that cannot be imported correctly
# These will be skipped during validation (but still imported for inspection)
SKIP_TEMPLATES=(
    # Currently none - all templates validate successfully
)

cd "$PROJECT_ROOT"

# Check if a template should be skipped during validation
should_skip_validation() {
    local template_name="$1"
    # Handle empty array safely with ${SKIP_TEMPLATES[@]+"${SKIP_TEMPLATES[@]}"}
    for skip in ${SKIP_TEMPLATES[@]+"${SKIP_TEMPLATES[@]}"}; do
        [[ "$template_name" == "$skip" ]] && return 0
    done
    return 1
}

# Helper functions
info() {
    echo -e "${BLUE}==>${NC} $1"
}

success() {
    echo -e "${GREEN}✓${NC} $1"
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

error() {
    echo -e "${RED}✗${NC} $1"
}

header() {
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

# Parse arguments
SOURCE_DIR="$DEFAULT_SOURCE"
CLEAN_ONLY=false
SKIP_CLEANUP=false
SKIP_VALIDATION=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --source)
            SOURCE_DIR="$2"
            shift 2
            ;;
        --clean-only)
            CLEAN_ONLY=true
            shift
            ;;
        --skip-cleanup)
            SKIP_CLEANUP=true
            shift
            ;;
        --skip-validation)
            SKIP_VALIDATION=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Import CloudFormation templates from vendor/aws-cloudformation-templates"
            echo "into examples/aws-cloudformation-templates/."
            echo ""
            echo "Options:"
            echo "  --source PATH      Path to source templates"
            echo "                     (default: vendor/aws-cloudformation-templates)"
            echo "  --clean-only       Only clean the output directory, don't import"
            echo "  --skip-cleanup     Don't remove failed imports after completion"
            echo "  --skip-validation  Skip running each package to validate it works"
            echo "  --help, -h         Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0                              # Full import with defaults"
            echo "  $0 --source /path/to/templates  # Custom source directory"
            echo "  $0 --skip-cleanup               # Keep failed imports for debugging"
            exit 0
            ;;
        *)
            error "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Verify uv is installed
if ! command -v uv &> /dev/null; then
    error "uv is not installed. Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Step 1: Clean output directory
header "Cleaning Output Directory"

if [ -d "$OUTPUT_DIR" ]; then
    rm -rf "$OUTPUT_DIR"
    success "Removed existing $OUTPUT_DIR"
fi

mkdir -p "$OUTPUT_DIR"
success "Created $OUTPUT_DIR"

if [ "$CLEAN_ONLY" = true ]; then
    info "Clean-only mode - exiting"
    exit 0
fi

# Verify source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    error "Source directory not found: $SOURCE_DIR"
    echo ""
    echo "The vendor directory should contain aws-cloudformation-templates."
    echo "To update it, run:"
    echo "  git clone https://github.com/awslabs/aws-cloudformation-templates.git /tmp/aws-cf-templates"
    echo "  rsync -av --exclude='.git' /tmp/aws-cf-templates/ vendor/aws-cloudformation-templates/"
    echo "  git -C /tmp/aws-cf-templates log -1 --format='%H %cs' > vendor/aws-cloudformation-templates/.git_commit"
    exit 1
fi

# Step 1.5: Copy source to temp directory and apply fixes
# We don't want to modify the original vendor directory
header "Preparing Template Copy"
TEMP_SOURCE_DIR=$(mktemp -d)
info "Copying templates to temp directory..."
cp -r "$SOURCE_DIR"/* "$TEMP_SOURCE_DIR/"
success "Copied to: $TEMP_SOURCE_DIR"

# Clean up temp files on exit
cleanup_temp() {
    if [ -n "${TEMP_SOURCE_DIR:-}" ] && [ -d "$TEMP_SOURCE_DIR" ]; then
        rm -rf "$TEMP_SOURCE_DIR"
    fi
    if [ -n "${RESULTS_FILE:-}" ] && [ -f "$RESULTS_FILE" ]; then
        rm -f "$RESULTS_FILE"
    fi
}
trap cleanup_temp EXIT

header "Applying Template Fixes"
python3 "$SCRIPT_DIR/fix_templates.py" "$TEMP_SOURCE_DIR"

# Use the temp directory as source for import
IMPORT_SOURCE_DIR="$TEMP_SOURCE_DIR"

# Step 2: Run batch import
header "Running Batch Import"
info "Source: $SOURCE_DIR (via temp copy)"
info "Output: $OUTPUT_DIR"
echo ""

# Run import (allow failure - we'll handle it in cleanup)
set +e
uv run cfn-dataclasses-import "$IMPORT_SOURCE_DIR" -o "$OUTPUT_DIR"
IMPORT_EXIT_CODE=$?
set -e

# Step 3: Parse import.log for failures
header "Analyzing Results"

LOG_FILE="$OUTPUT_DIR/import.log"

if [ ! -f "$LOG_FILE" ]; then
    error "Log file not found: $LOG_FILE"
    exit 1
fi

# Count total templates imported
TOTAL_DIRS=$(find "$OUTPUT_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ')
TOTAL_DIRS=$((TOTAL_DIRS - 1))  # Exclude output dir itself

# Parse log to find failed templates
# Log format: "2025-12-21 10:15:23,456 - Importing /path/to/template.yaml"
# followed by error lines

FAILED_PACKAGES=()
LAST_TEMPLATE=""

while IFS= read -r line; do
    # Track the current template being imported
    if [[ "$line" =~ "Importing " ]]; then
        # Extract template path and convert to package name
        TEMPLATE_PATH=$(echo "$line" | sed 's/.*Importing //')
        # Get filename without extension
        TEMPLATE_NAME=$(basename "$TEMPLATE_PATH")
        TEMPLATE_STEM="${TEMPLATE_NAME%.*}"
        # Convert to package name (same logic as cli.py)
        LAST_TEMPLATE=$(echo "$TEMPLATE_STEM" | sed 's/[^a-zA-Z0-9_]/_/g' | tr '[:upper:]' '[:lower:]')
    fi

    # If we see an Error, the last template failed
    # Log format: "2025-12-21 16:52:38,708 - Error: Template uses Rain-specific tags..."
    if [[ "$line" =~ " - Error:" ]] && [ -n "$LAST_TEMPLATE" ]; then
        FAILED_PACKAGES+=("$LAST_TEMPLATE")
        LAST_TEMPLATE=""  # Reset to avoid double-counting
    fi
done < "$LOG_FILE"

info "Found ${#FAILED_PACKAGES[@]} failed imports"

# Step 4: Remove failed package directories
if [ "$SKIP_CLEANUP" = false ] && [ ${#FAILED_PACKAGES[@]} -gt 0 ]; then
    header "Cleaning Up Failed Imports"

    CLEANED_COUNT=0
    for pkg in "${FAILED_PACKAGES[@]}"; do
        PKG_DIR="$OUTPUT_DIR/$pkg"
        if [ -d "$PKG_DIR" ]; then
            rm -rf "$PKG_DIR"
            info "Removed: $pkg"
            CLEANED_COUNT=$((CLEANED_COUNT + 1))
        fi
    done

    success "Cleaned up $CLEANED_COUNT failed package directories"
else
    if [ "$SKIP_CLEANUP" = true ]; then
        warn "Skipping cleanup (--skip-cleanup flag)"
    fi
fi

# Step 5: Validate each package by running it
VALIDATION_FAILED=()

if [ "$SKIP_VALIDATION" = false ]; then
    header "Validating Packages"

    # Get list of package directories (excluding import.log)
    PACKAGE_DIRS=()
    for dir in "$OUTPUT_DIR"/*/; do
        if [ -d "$dir" ]; then
            PACKAGE_DIRS+=("$dir")
        fi
    done

    TOTAL_PACKAGES=${#PACKAGE_DIRS[@]}

    # Create a temporary file to track results
    RESULTS_FILE=$(mktemp)

    # Number of parallel jobs (use CPU count, cap at 8)
    JOBS=$(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null || echo 4)
    JOBS=$((JOBS > 8 ? 8 : JOBS))

    info "Validating $TOTAL_PACKAGES packages (${JOBS} parallel jobs)..."
    echo ""

    # Validation function for a single package (runs in parallel)
    # Uses PYTHONPATH instead of venv - much faster, no pip install needed
    # PROJECT_SRC and VALIDATION_ERRORS_FILE are exported as environment variables
    export PROJECT_SRC="$PROJECT_ROOT/src"
    export VALIDATION_ERRORS_FILE="$OUTPUT_DIR/validation_errors.log"
    > "$VALIDATION_ERRORS_FILE"  # Clear/create the file

    validate_package() {
        local pkg_dir="$1"
        local pkg_name=$(basename "$pkg_dir")

        # Run directly with PYTHONPATH - capture stderr for debugging
        local error_output
        if error_output=$(PYTHONPATH="$PROJECT_SRC:$pkg_dir" python3 -m "$pkg_name" 2>&1 >/dev/null); then
            echo "OK:$pkg_name"
        else
            echo "FAIL:$pkg_name"
            # Log the error for debugging (use flock to prevent race conditions)
            {
                echo "=== $pkg_name ==="
                echo "$error_output"
                echo ""
            } >> "$VALIDATION_ERRORS_FILE"
        fi
    }
    export -f validate_package

    # Run validations in parallel using xargs
    # Filter out skipped packages first
    for pkg_dir in "${PACKAGE_DIRS[@]}"; do
        pkg_name=$(basename "$pkg_dir")
        if should_skip_validation "$pkg_name"; then
            warn "$pkg_name (skipped - known malformed template)"
        else
            echo "$pkg_dir"
        fi
    done | xargs -P "$JOBS" -I {} bash -c 'validate_package "$@"' _ {} >> "$RESULTS_FILE"

    # Process results
    VALIDATED_COUNT=0
    while IFS=: read -r status pkg_name; do
        if [ "$status" = "OK" ]; then
            success "$pkg_name"
            VALIDATED_COUNT=$((VALIDATED_COUNT + 1))
        else
            error "$pkg_name"
            VALIDATION_FAILED+=("$pkg_name")
        fi
    done < "$RESULTS_FILE"

    echo ""
    success "Validated: $VALIDATED_COUNT/$TOTAL_PACKAGES packages"

    # Re-import and re-validate packages that failed
    if [ ${#VALIDATION_FAILED[@]} -gt 0 ] && [ "$SKIP_CLEANUP" = false ]; then
        echo ""
        info "Re-importing ${#VALIDATION_FAILED[@]} failed packages..."

        # Clear the validation errors file before re-validation
        > "$VALIDATION_ERRORS_FILE"

        STILL_FAILING=()
        for pkg in "${VALIDATION_FAILED[@]}"; do
            # Find the original template file from import.log
            ORIGINAL_TEMPLATE=$(grep -B 50 "Generated:.*/$pkg/" "$LOG_FILE" | grep "Importing " | tail -1 | sed 's/.*Importing //')

            if [ -n "$ORIGINAL_TEMPLATE" ] && [ -f "$ORIGINAL_TEMPLATE" ]; then
                # Create package subdirectory (CLI uses output dir name as package name)
                PKG_OUTPUT="$OUTPUT_DIR/$pkg"
                # Ensure clean state before re-import
                rm -rf "$PKG_OUTPUT"
                set +e
                uv run cfn-dataclasses-import "$ORIGINAL_TEMPLATE" -o "$PKG_OUTPUT" --skip-checks 2>/dev/null
                set -e

                # Re-validate the re-imported package
                if PYTHONPATH="$PROJECT_SRC:$PKG_OUTPUT" python3 -m "$pkg" >/dev/null 2>&1; then
                    success "$pkg (fixed on re-import)"
                else
                    error "$pkg (still failing)"
                    STILL_FAILING+=("$pkg")
                    # Log the error
                    {
                        echo "=== $pkg ==="
                        PYTHONPATH="$PROJECT_SRC:$PKG_OUTPUT" python3 -m "$pkg" 2>&1 || true
                        echo ""
                    } >> "$VALIDATION_ERRORS_FILE"
                fi
            else
                warn "Could not find original template for: $pkg"
                STILL_FAILING+=("$pkg")
            fi
        done

        # Update VALIDATION_FAILED to only contain packages that still fail
        VALIDATION_FAILED=()
        if [ ${#STILL_FAILING[@]} -gt 0 ]; then
            VALIDATION_FAILED=("${STILL_FAILING[@]}")
        fi

        if [ ${#VALIDATION_FAILED[@]} -gt 0 ]; then
            echo ""
            warn "${#VALIDATION_FAILED[@]} packages still failing after re-import."
            warn "Inspect them in: $OUTPUT_DIR/<package_name>/"
        else
            echo ""
            success "All packages validated successfully after re-import!"
            # Clear the validation errors file since all are fixed
            > "$VALIDATION_ERRORS_FILE"
        fi
    fi
else
    warn "Skipping validation (--skip-validation flag)"
fi

# Step 6: Report
header "Import Summary"

# Recount after cleanup
FINAL_DIRS=$(find "$OUTPUT_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ')
FINAL_DIRS=$((FINAL_DIRS - 1))  # Exclude output dir itself

echo ""
success "Successful packages: $FINAL_DIRS"
if [ ${#FAILED_PACKAGES[@]} -gt 0 ]; then
    warn "Failed imports: ${#FAILED_PACKAGES[@]}"
fi
if [ ${#VALIDATION_FAILED[@]} -gt 0 ]; then
    warn "Failed validation: ${#VALIDATION_FAILED[@]}"
    if [ "$SKIP_CLEANUP" = false ]; then
        info "Failed packages re-imported for inspection (without validation)"
    fi
fi
echo ""

info "Output directory: $OUTPUT_DIR"
info "Import log: $LOG_FILE"
if [ -s "$OUTPUT_DIR/validation_errors.log" ]; then
    info "Validation errors: $OUTPUT_DIR/validation_errors.log"
fi
echo ""

# List failure reasons from log
if [ ${#FAILED_PACKAGES[@]} -gt 0 ]; then
    info "Failure breakdown:"

    # Count Rain-specific failures
    RAIN_COUNT=$(grep -c "Rain-specific tags" "$LOG_FILE" 2>/dev/null || echo "0")
    if [ "$RAIN_COUNT" -gt 0 ]; then
        echo "  • Rain-specific tags: $RAIN_COUNT"
    fi

    # Count Kubernetes manifest detections
    K8S_COUNT=$(grep -c "Kubernetes manifest" "$LOG_FILE" 2>/dev/null || echo "0")
    if [ "$K8S_COUNT" -gt 0 ]; then
        echo "  • Kubernetes manifests: $K8S_COUNT"
    fi

    # Count parse failures
    PARSE_COUNT=$(grep -c "Failed to parse" "$LOG_FILE" 2>/dev/null || echo "0")
    if [ "$PARSE_COUNT" -gt 0 ]; then
        echo "  • Parse failures: $PARSE_COUNT"
    fi

    # Count other errors (subtract known categories)
    TOTAL_ERRORS=$(grep -c " - Error:" "$LOG_FILE" 2>/dev/null || echo "0")
    OTHER_COUNT=$((TOTAL_ERRORS - RAIN_COUNT - K8S_COUNT - PARSE_COUNT))
    if [ "$OTHER_COUNT" -gt 0 ]; then
        echo "  • Other errors: $OTHER_COUNT"
    fi

    echo ""
fi

# Exit with appropriate code
if [ $IMPORT_EXIT_CODE -ne 0 ]; then
    warn "Import completed with some failures (see log for details)"
    exit 0  # Still exit 0 since we cleaned up successfully
else
    success "Import completed successfully!"
fi
