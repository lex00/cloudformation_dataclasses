#!/usr/bin/env bash
#
# Build automation script for cloudformation_dataclasses
#
# This script performs a complete build pipeline:
# 1. Clean previous builds
# 2. Run tests
# 3. Build package distributions
# 4. Verify package contents
#
# Usage:
#   ./scripts/build.sh              # Full build with tests
#   ./scripts/build.sh --skip-tests # Build without running tests
#   ./scripts/build.sh --clean-only # Only clean build artifacts
#

set -e  # Exit on error
set -u  # Exit on undefined variable

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

# Parse arguments
SKIP_TESTS=false
CLEAN_ONLY=false

for arg in "$@"; do
    case $arg in
        --skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        --clean-only)
            CLEAN_ONLY=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --skip-tests   Skip running tests"
            echo "  --clean-only   Only clean build artifacts"
            echo "  --help, -h     Show this help message"
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $arg${NC}"
            exit 1
            ;;
    esac
done

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

# Step 1: Clean previous builds
info "Cleaning previous build artifacts..."
rm -rf build/ dist/ *.egg-info src/*.egg-info
rm -rf .pytest_cache/ .coverage htmlcov/
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true
success "Build artifacts cleaned"

if [ "$CLEAN_ONLY" = true ]; then
    info "Clean-only mode - exiting"
    exit 0
fi

# Step 2: Verify uv is installed
if ! command -v uv &> /dev/null; then
    error "uv is not installed. Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi
success "uv found: $(uv --version)"

# Step 3: Run tests (unless skipped)
if [ "$SKIP_TESTS" = false ]; then
    info "Running tests..."
    if uv run pytest tests/ examples/ -v --tb=short; then
        success "All tests passed"
    else
        error "Tests failed - aborting build"
        exit 1
    fi
else
    warn "Skipping tests (--skip-tests flag)"
fi

# Step 4: Build package
info "Building package distributions..."
if uv build; then
    success "Package built successfully"
else
    error "Package build failed"
    exit 1
fi

# Step 5: Verify build artifacts
info "Verifying build artifacts..."

if [ ! -d "dist/" ]; then
    error "dist/ directory not found"
    exit 1
fi

WHEEL_COUNT=$(find dist/ -name "*.whl" | wc -l | tr -d ' ')
SDIST_COUNT=$(find dist/ -name "*.tar.gz" | wc -l | tr -d ' ')

if [ "$WHEEL_COUNT" -eq 0 ]; then
    error "No wheel (.whl) file found in dist/"
    exit 1
fi

if [ "$SDIST_COUNT" -eq 0 ]; then
    error "No source distribution (.tar.gz) file found in dist/"
    exit 1
fi

success "Found $WHEEL_COUNT wheel file(s)"
success "Found $SDIST_COUNT source distribution file(s)"

# Step 6: Display build artifacts
info "Build artifacts:"
ls -lh dist/

# Step 7: Verify package contents
info "Verifying package contents..."
WHEEL_FILE=$(find dist/ -name "*.whl" | head -1)

if command -v unzip &> /dev/null; then
    info "Wheel contents:"
    unzip -l "$WHEEL_FILE" | grep -E "cloudformation_dataclasses/(core|intrinsics|aws|codegen|__init__|__version__)" | head -20
else
    warn "unzip not found - skipping wheel content verification"
fi

# Step 8: Success summary
echo ""
info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
success "Build completed successfully!"
info "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
info "Next steps:"
echo "  • Test installation: uv pip install dist/*.whl"
echo "  • Publish to TestPyPI: uv publish --repository testpypi dist/*"
echo "  • Publish to PyPI: uv publish dist/*"
echo ""
