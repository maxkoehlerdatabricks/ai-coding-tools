#!/usr/bin/env bash
# Run notebooks with the project .venv (bypasses Cursor kernel picker).
# Usage:
#   ./scripts/run_notebook.sh              # execute default notebook
#   ./scripts/run_notebook.sh path/to.ipynb
#   ./scripts/run_notebook.sh --jupyter    # open Jupyter in browser (then use Run All there)
set -e
cd "$(dirname "$0")/.."
if [[ "$1" == "--jupyter" ]]; then
  echo "Starting Jupyter. Use kernel 'Python (ai-coding-tools)' or the only Python kernel, then Run All."
  unset DATABRICKS_AUTH_TYPE DATABRICKS_METADATA_SERVICE_URL
  exec .venv/bin/python -m jupyter notebook playground/
fi
NOTEBOOK="${1:-playground/test_databricks_connect.ipynb}"
if [[ ! -f "$NOTEBOOK" ]]; then
  echo "Not found: $NOTEBOOK"
  exit 1
fi
# Use profile token from ~/.databrickscfg; avoid metadata-service (only works inside Cursor/IDE).
unset DATABRICKS_AUTH_TYPE DATABRICKS_METADATA_SERVICE_URL
.venv/bin/python -m jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=300 -- "$NOTEBOOK"
echo "Done. Outputs are in the notebook."
