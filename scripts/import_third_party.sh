#!/usr/bin/env bash
#
# Third-party template import script for cloudformation_dataclasses
#
# This script automates the full process of importing CloudFormation templates
# from aws-cloudformation-templates into examples/third_party/aws_cloudformation_templates/.
#
# Workflow:
# 1. Clean output directory
# 2. Run batch import via cfn-dataclasses-import
# 3. Parse import.log for failures
# 4. Remove directories for failed imports
# 5. Report final statistics
#
# Usage:
#   ./scripts/import_third_party.sh                        # Full import
#   ./scripts/import_third_party.sh --source /path         # Custom source
#   ./scripts/import_third_party.sh --clean-only           # Just clean output
#   ./scripts/import_third_party.sh --skip-cleanup         # Keep failed imports
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
DEFAULT_SOURCE="$PROJECT_ROOT/../aws-cloudformation-templates"
OUTPUT_DIR="$PROJECT_ROOT/examples/third_party/aws_cloudformation_templates"

cd "$PROJECT_ROOT"

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
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Import CloudFormation templates from aws-cloudformation-templates"
            echo "into examples/third_party/aws_cloudformation_templates/."
            echo ""
            echo "Options:"
            echo "  --source PATH      Path to source templates"
            echo "                     (default: ../aws-cloudformation-templates)"
            echo "  --clean-only       Only clean the output directory, don't import"
            echo "  --skip-cleanup     Don't remove failed imports after completion"
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
    echo "Please clone the aws-cloudformation-templates repository:"
    echo "  git clone https://github.com/awslabs/aws-cloudformation-templates.git"
    exit 1
fi

# Step 2: Run batch import
header "Running Batch Import"
info "Source: $SOURCE_DIR"
info "Output: $OUTPUT_DIR"
echo ""

# Run import (allow failure - we'll handle it in cleanup)
set +e
uv run cfn-dataclasses-import "$SOURCE_DIR" -o "$OUTPUT_DIR"
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

# Step 5: Report
header "Import Summary"

# Recount after cleanup
FINAL_DIRS=$(find "$OUTPUT_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ')
FINAL_DIRS=$((FINAL_DIRS - 1))  # Exclude output dir itself

echo ""
success "Successful packages: $FINAL_DIRS"
if [ ${#FAILED_PACKAGES[@]} -gt 0 ]; then
    warn "Failed imports: ${#FAILED_PACKAGES[@]}"
fi
echo ""

info "Output directory: $OUTPUT_DIR"
info "Import log: $LOG_FILE"
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
