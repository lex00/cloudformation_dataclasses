#!/usr/bin/env bash
#
# Test automation script for cloudformation_dataclasses
#
# This script runs the test suite with various options:
# - Framework validation tests (tests/)
# - Example tests (examples/)
# - Coverage reporting
#
# Usage:
#   ./scripts/test.sh                    # Run all tests with coverage
#   ./scripts/test.sh --fast             # Run tests without coverage
#   ./scripts/test.sh --framework-only   # Run only framework tests
#   ./scripts/test.sh --examples-only    # Run only example tests
#   ./scripts/test.sh --watch            # Run tests in watch mode
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
FAST_MODE=false
FRAMEWORK_ONLY=false
EXAMPLES_ONLY=false
WATCH_MODE=false
VERBOSE=false

for arg in "$@"; do
    case $arg in
        --fast)
            FAST_MODE=true
            shift
            ;;
        --framework-only)
            FRAMEWORK_ONLY=true
            shift
            ;;
        --examples-only)
            EXAMPLES_ONLY=true
            shift
            ;;
        --watch)
            WATCH_MODE=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --fast             Run tests without coverage"
            echo "  --framework-only   Run only framework validation tests"
            echo "  --examples-only    Run only example tests"
            echo "  --watch            Run tests in watch mode (requires pytest-watch)"
            echo "  -v, --verbose      Verbose output"
            echo "  --help, -h         Show this help message"
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

# Verify uv is installed
if ! command -v uv &> /dev/null; then
    error "uv is not installed. Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Determine test paths
TEST_PATHS=""
if [ "$FRAMEWORK_ONLY" = true ]; then
    TEST_PATHS="tests/"
    info "Running framework validation tests only"
elif [ "$EXAMPLES_ONLY" = true ]; then
    TEST_PATHS="examples/"
    info "Running example tests only"
else
    TEST_PATHS="tests/ examples/"
    info "Running all tests (framework + examples)"
fi

# Build pytest command
PYTEST_CMD="uv run pytest $TEST_PATHS"

# Add verbosity
if [ "$VERBOSE" = true ]; then
    PYTEST_CMD="$PYTEST_CMD -vv"
else
    PYTEST_CMD="$PYTEST_CMD -v"
fi

# Add coverage (unless fast mode)
if [ "$FAST_MODE" = false ]; then
    PYTEST_CMD="$PYTEST_CMD --cov=cloudformation_dataclasses --cov-report=term-missing"
else
    warn "Running in fast mode (no coverage)"
fi

# Add traceback format
PYTEST_CMD="$PYTEST_CMD --tb=short"

# Watch mode
if [ "$WATCH_MODE" = true ]; then
    if ! uv pip show pytest-watch &> /dev/null; then
        error "pytest-watch not installed. Install with:"
        echo "  uv pip install pytest-watch"
        exit 1
    fi
    info "Starting test watch mode (Ctrl+C to exit)..."
    uv run ptw $TEST_PATHS -- -v --tb=short
    exit 0
fi

# Run tests
info "Running tests..."
echo ""

if eval "$PYTEST_CMD"; then
    echo ""
    success "All tests passed!"
    exit 0
else
    echo ""
    error "Some tests failed"
    exit 1
fi
