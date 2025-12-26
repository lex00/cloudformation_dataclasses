#!/usr/bin/env bash
#
# Version bump script for cloudformation_dataclasses
#
# This script updates the package version across all files that need it:
# - pyproject.toml
# - src/cloudformation_dataclasses/__version__.py
# - CHANGELOG.md (adds placeholder section)
# - docs/DEVELOPERS.md (version footer)
#
# Usage:
#   ./scripts/bump_version.sh 0.6.0
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

# Show usage
usage() {
    echo "Usage: $0 <version>"
    echo ""
    echo "Bump the package version across all files."
    echo ""
    echo "Arguments:"
    echo "  version    New version in semantic versioning format (X.Y.Z)"
    echo ""
    echo "Examples:"
    echo "  $0 0.6.0      # Bump to 0.6.0"
    echo "  $0 1.0.0      # Bump to 1.0.0"
    echo ""
    echo "Files updated:"
    echo "  - pyproject.toml"
    echo "  - src/cloudformation_dataclasses/__version__.py"
    echo "  - CHANGELOG.md (placeholder section added)"
    echo "  - docs/DEVELOPERS.md (version footer)"
}

# Validate arguments
if [ $# -ne 1 ]; then
    error "Missing version argument"
    echo ""
    usage
    exit 1
fi

if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    usage
    exit 0
fi

NEW_VERSION="$1"

# Validate version format (X.Y.Z)
if ! [[ "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    error "Invalid version format: $NEW_VERSION"
    echo "Version must be in semantic versioning format: X.Y.Z (e.g., 0.6.0, 1.0.0)"
    exit 1
fi

# Get current version (extract just the version number from 'version = "X.Y.Z"')
CURRENT_VERSION=$(grep -E '^version = "' pyproject.toml | sed 's/version = "\([^"]*\)".*/\1/')

header "Version Bump: $CURRENT_VERSION → $NEW_VERSION"

# Confirm if versions are the same
if [ "$CURRENT_VERSION" = "$NEW_VERSION" ]; then
    warn "Version is already $NEW_VERSION"
    exit 0
fi

# Step 1: Update pyproject.toml
info "Updating pyproject.toml..."
sed -i '' "s/^version = \".*\"/version = \"$NEW_VERSION\"/" pyproject.toml
success "Updated pyproject.toml"

# Step 2: Update __version__.py
info "Updating __version__.py..."
sed -i '' "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" src/cloudformation_dataclasses/__version__.py
success "Updated __version__.py"

# Step 3: Add CHANGELOG entry
info "Adding CHANGELOG.md entry..."

# Get today's date
TODAY=$(date +%Y-%m-%d)

# Create the new changelog entry
NEW_ENTRY="## [$NEW_VERSION] - $TODAY

### Added

### Changed

### Fixed

"

# Insert after the first "## [" line (after header section)
# Find the line number of the first version entry
FIRST_VERSION_LINE=$(grep -n "^## \[" CHANGELOG.md | head -1 | cut -d: -f1)

if [ -n "$FIRST_VERSION_LINE" ]; then
    # Insert before the first version entry
    head -n $((FIRST_VERSION_LINE - 1)) CHANGELOG.md > CHANGELOG.tmp
    echo "$NEW_ENTRY" >> CHANGELOG.tmp
    tail -n +$FIRST_VERSION_LINE CHANGELOG.md >> CHANGELOG.tmp
    mv CHANGELOG.tmp CHANGELOG.md
    success "Added CHANGELOG.md entry"
else
    warn "Could not find version entries in CHANGELOG.md - manual update required"
fi

# Step 4: Update DEVELOPERS.md footer
info "Updating docs/DEVELOPERS.md..."
sed -i '' "s/^\*\*Last Updated\*\*: .*/\*\*Last Updated\*\*: $TODAY/" docs/DEVELOPERS.md
sed -i '' "s/^\*\*For\*\*: v.*/\*\*For\*\*: v$NEW_VERSION/" docs/DEVELOPERS.md
success "Updated docs/DEVELOPERS.md"

# Summary
header "Version Bump Complete"

echo "Updated files:"
echo "  • pyproject.toml"
echo "  • src/cloudformation_dataclasses/__version__.py"
echo "  • CHANGELOG.md"
echo "  • docs/DEVELOPERS.md"
echo ""

info "Next steps:"
echo "  1. Edit CHANGELOG.md to fill in the changes"
echo "  2. Run tests: ./scripts/test.sh"
echo "  3. Commit: git commit -am \"Bump version to $NEW_VERSION\""
echo "  4. Tag: git tag v$NEW_VERSION"
echo "  5. Push: git push && git push --tags"
echo ""

# Verify the changes
info "Verification:"
echo "  pyproject.toml:  version = \"$(grep -E '^version = "' pyproject.toml | sed 's/version = "\([^"]*\)".*/\1/')\""
echo "  __version__.py:  __version__ = \"$(grep '__version__ = ' src/cloudformation_dataclasses/__version__.py | sed 's/__version__ = "\([^"]*\)"/\1/')\""
echo ""

success "Version bumped to $NEW_VERSION"
