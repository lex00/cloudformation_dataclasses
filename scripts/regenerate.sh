#!/usr/bin/env bash
#
# Code regeneration script for cloudformation_dataclasses
#
# This script regenerates AWS service resources from CloudFormation specs:
# 1. Downloads/validates CloudFormation spec version
# 2. Regenerates specified services
# 3. Runs tests to verify generated code
#
# Usage:
#   ./scripts/regenerate.sh S3                    # Regenerate S3 only
#   ./scripts/regenerate.sh S3 EC2 Lambda         # Regenerate multiple services
#   ./scripts/regenerate.sh --all                 # Regenerate all services
#   ./scripts/regenerate.sh --list                # List available services
#   ./scripts/regenerate.sh --verify-spec         # Only verify spec version
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
SERVICES=()
LIST_SERVICES=false
VERIFY_SPEC_ONLY=false
REGENERATE_ALL=false
SKIP_TESTS=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --list)
            LIST_SERVICES=true
            shift
            ;;
        --verify-spec)
            VERIFY_SPEC_ONLY=true
            shift
            ;;
        --all)
            REGENERATE_ALL=true
            shift
            ;;
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS] [SERVICES...]"
            echo ""
            echo "Options:"
            echo "  --list          List all available AWS services"
            echo "  --verify-spec   Only verify CloudFormation spec version"
            echo "  --all           Regenerate all services"
            echo "  --skip-tests    Skip running tests after regeneration"
            echo "  --help, -h      Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0 S3                     # Regenerate S3 only"
            echo "  $0 S3 EC2 Lambda          # Regenerate multiple services"
            echo "  $0 --all                  # Regenerate all services"
            echo "  $0 --list                 # List available services"
            exit 0
            ;;
        *)
            SERVICES+=("$1")
            shift
            ;;
    esac
done

# Verify uv is installed
if ! command -v uv &> /dev/null; then
    error "uv is not installed. Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# List services mode
if [ "$LIST_SERVICES" = true ]; then
    header "Available AWS Services"
    info "Fetching service list from CloudFormation spec..."
    uv run python -m cloudformation_dataclasses.codegen.spec_parser list-services
    exit 0
fi

# Verify spec version
header "CloudFormation Spec Verification"
info "Checking CloudFormation spec version..."

if uv run python -m cloudformation_dataclasses.codegen.spec_parser version; then
    success "CloudFormation spec version verified"
else
    error "CloudFormation spec version mismatch or error"
    exit 1
fi

if [ "$VERIFY_SPEC_ONLY" = true ]; then
    info "Verify-only mode - exiting"
    exit 0
fi

# Determine services to regenerate
if [ "$REGENERATE_ALL" = true ]; then
    warn "Regenerating ALL services (this may take a while)..."
    # Get list of all services
    ALL_SERVICES=$(uv run python -m cloudformation_dataclasses.codegen.spec_parser list-services 2>/dev/null | grep -E "^\s+\w+" | awk '{print $1}' | tr -d ':')
    readarray -t SERVICES <<< "$ALL_SERVICES"
elif [ ${#SERVICES[@]} -eq 0 ]; then
    error "No services specified. Use --list to see available services."
    echo ""
    echo "Usage:"
    echo "  $0 S3              # Regenerate S3"
    echo "  $0 S3 EC2 Lambda   # Regenerate multiple services"
    echo "  $0 --all           # Regenerate all services"
    echo "  $0 --list          # List available services"
    exit 1
fi

# Regenerate each service
header "Code Generation"
info "Regenerating ${#SERVICES[@]} service(s)..."
echo ""

FAILED_SERVICES=()
SUCCESS_SERVICES=()

for service in "${SERVICES[@]}"; do
    # Skip empty lines
    if [ -z "$service" ]; then
        continue
    fi

    info "Regenerating service: $service"

    if uv run python -m cloudformation_dataclasses.codegen.generator --service "$service"; then
        success "Generated $service"
        SUCCESS_SERVICES+=("$service")
    else
        error "Failed to generate $service"
        FAILED_SERVICES+=("$service")
    fi
    echo ""
done

# Summary
header "Generation Summary"

if [ ${#SUCCESS_SERVICES[@]} -gt 0 ]; then
    success "Successfully generated ${#SUCCESS_SERVICES[@]} service(s):"
    for service in "${SUCCESS_SERVICES[@]}"; do
        echo "  • $service"
    done
    echo ""
fi

if [ ${#FAILED_SERVICES[@]} -gt 0 ]; then
    error "Failed to generate ${#FAILED_SERVICES[@]} service(s):"
    for service in "${FAILED_SERVICES[@]}"; do
        echo "  • $service"
    done
    echo ""
    exit 1
fi

# Run tests (unless skipped)
if [ "$SKIP_TESTS" = false ]; then
    header "Running Tests"
    info "Verifying generated code with test suite..."

    if "$SCRIPT_DIR/test.sh" --fast; then
        success "All tests passed!"
    else
        error "Tests failed - please review generated code"
        exit 1
    fi
else
    warn "Skipping tests (--skip-tests flag)"
fi

# Final success
echo ""
header "Regeneration Complete"
success "Successfully regenerated ${#SUCCESS_SERVICES[@]} service(s)"
echo ""
info "Next steps:"
echo "  • Review generated code in src/cloudformation_dataclasses/aws/"
echo "  • Run full test suite: ./scripts/test.sh"
echo "  • Build package: ./scripts/build.sh"
echo ""
