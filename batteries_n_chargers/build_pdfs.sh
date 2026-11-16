#!/usr/bin/env bash
# Build the battery & charger PDFs from the markdown sources.
#
# Usage:
#   ./build_pdfs.sh              # build everything into pdf/
#   ./build_pdfs.sh cards        # only the laminate cards
#   ./build_pdfs.sh guide        # only the main guide and the open-items list
#   ./build_pdfs.sh --keep-html  # also leave the intermediate HTML in build/
#
# Toolchain (no sudo, nothing to install on the dgx):
#   python3 + the python3-markdown package  -- markdown -> HTML
#   google-chrome --headless                -- HTML + style/cheatsheet.css -> PDF
# Check both are present:
#   python3 -c "import markdown; print(markdown.__version__)"
#   command -v google-chrome
# If python3-markdown is missing:  pip3 install --user markdown
#
# Page setup lives in style/cheatsheet.css (@page). The cards are written to fit
# one US Letter side each so they can be printed and laminated; if an edit pushes
# one onto a second page, trim the card rather than shrinking the type.

set -euo pipefail

cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"

BUILD=build
PDF=pdf
KEEP_HTML=0
WHAT=all

for arg in "$@"; do
  case "$arg" in
    --keep-html) KEEP_HTML=1 ;;
    cards|guide|all) WHAT="$arg" ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "unknown argument: $arg" >&2; exit 2 ;;
  esac
done

command -v google-chrome >/dev/null || { echo "google-chrome not found" >&2; exit 3; }
python3 -c "import markdown" 2>/dev/null || { echo "python3 markdown module not found (pip3 install --user markdown)" >&2; exit 3; }

mkdir -p "$BUILD" "$PDF"

# render <src.md> <body-class>  -- markdown -> HTML -> PDF
render() {
  local src="$1" cls="$2"
  local stem html out
  stem="$(basename "${src%.md}")"
  html="$BUILD/$stem.html"
  out="$PDF/$stem.pdf"
  python3 md2html.py "$src" "$html" "$cls"
  google-chrome --headless=new --disable-gpu --no-sandbox \
    --no-pdf-header-footer --virtual-time-budget=5000 \
    --print-to-pdf="$out" "file://$PWD/$html" >/dev/null 2>&1
  printf '  pdf   %s  (%s)\n' "$out" "$(du -h "$out" | cut -f1)"
}

echo "building battery & charger documents"

if [ "$WHAT" = all ] || [ "$WHAT" = guide ]; then
  render main_guide.md guide
  render todo.md guide
fi

if [ "$WHAT" = all ] || [ "$WHAT" = cards ]; then
  for card in cards/*.md; do
    render "$card" card
  done
fi

[ "$KEEP_HTML" -eq 1 ] || rm -rf "$BUILD"

echo "done -- PDFs in $PWD/$PDF"
