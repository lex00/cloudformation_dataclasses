#!/bin/bash
# Build or preview API documentation locally
#
# Usage:
#   ./scripts/docs.sh          # Serve with auto-reload (default)
#   ./scripts/docs.sh --build  # Build static HTML to docs/api/
#   ./scripts/docs.sh --help   # Show help

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$PROJECT_ROOT/docs/api"

# Explicitly list submodules to document
# Excludes: aws/ (262 generated services), codegen/ (internal tools), package_templates/
MODULES="cloudformation_dataclasses.core cloudformation_dataclasses.intrinsics cloudformation_dataclasses.linter cloudformation_dataclasses.importer cloudformation_dataclasses.constants"

# pdoc styling options
TEMPLATE_DIR="$PROJECT_ROOT/docs/pdoc-templates"

show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Build or preview API documentation locally using pdoc."
    echo ""
    echo "Options:"
    echo "  --build    Build static HTML to docs/api/"
    echo "  --serve    Serve locally with auto-reload (default)"
    echo "  --help     Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0              # Start local server at http://localhost:8080"
    echo "  $0 --build      # Generate static HTML files"
}

cd "$PROJECT_ROOT"

# Ensure pdoc is installed
if ! uv run python -c "import pdoc" 2>/dev/null; then
    echo "Installing pdoc..."
    uv sync --group docs
fi

case "${1:-}" in
    --build)
        echo "Building docs to $OUTPUT_DIR..."
        rm -rf "$OUTPUT_DIR"
        uv run pdoc $MODULES --footer-text "Python dataclasses for CloudFormation" -t "$TEMPLATE_DIR" -o "$OUTPUT_DIR"
        echo "Done! Open $OUTPUT_DIR/index.html in your browser."
        ;;
    --serve|"")
        echo "Starting local docs server..."
        echo "Press Ctrl+C to stop."
        echo ""
        uv run pdoc $MODULES --footer-text "Python dataclasses for CloudFormation" -t "$TEMPLATE_DIR"
        ;;
    --help|-h)
        show_help
        ;;
    *)
        echo "Unknown option: $1"
        show_help
        exit 1
        ;;
esac
