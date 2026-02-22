#!/usr/bin/env bash
# Register the current Python environment as a Jupyter kernel.
# Run from project root with your venv activated, or: ./scripts/register_kernel.sh
set -e
cd "$(dirname "$0")/.."
python -m ipykernel install --user --name=ai-coding-tools --display-name="Python (ai-coding-tools)"
echo "Kernel registered. Select 'Python (ai-coding-tools)' in your notebook kernel picker."
