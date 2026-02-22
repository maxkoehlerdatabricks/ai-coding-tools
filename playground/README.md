# Playground

## Run All when Cursor’s kernel picker doesn’t work

You can run the notebook without using Cursor’s Select Kernel:

**Option 1 – Execute from terminal (Run All in one go):**
```bash
./scripts/run_notebook.sh
```
Runs `playground/test_databricks_connect.ipynb` with the project `.venv` and saves outputs into the notebook.

**Option 2 – Jupyter in the browser (full UI, Run All works there):**
```bash
./scripts/run_notebook.sh --jupyter
```
Opens Jupyter in your browser; open the notebook and use **Run All** there (the correct kernel is already active).

---

## If "Select Kernel" shows no list

Cursor sometimes doesn’t show any kernels in the picker. Use one of these:

### Option A: Select interpreter first (recommended)

1. **Cmd+Shift+P** (or Ctrl+Shift+P) → run **"Python: Select Interpreter"**.
2. Pick the interpreter that points at this project’s `.venv`, e.g. **Python 3.12.x ('.venv': venv)** or the path containing `ai-coding-tools/.venv`.
3. Open the notebook and click **Select Kernel** again; the list may now include that interpreter.

### Option B: Paste the path in “Select a Python Environment”

If the list is empty, the dialog has a **text field** at the top:

1. Click **Select Kernel** → **Python Environments...**.
2. In the **“Select a Python Environment”** dialog, click in the **search/path input field** at the top.
3. Paste this path. If **pressing Enter does nothing**, **click the path with the mouse** to select it, or use Option B2 below.

**If Enter still does nothing:** use **Cmd+Shift+P** → **"Python: Select Interpreter"** → paste the same path and **click** the entry (the interpreter picker often accepts clicks). Then reopen the notebook and run a cell; it should use that interpreter.

   ```
   /Users/max.kohler/ai-coding-tools/.venv/bin/python
   ```

### Option C: Run from terminal

From the project root:

```bash
source .venv/bin/activate
jupyter notebook playground/
```

Then open the notebook in the browser and pick the **Python (ai-coding-tools)** kernel (or the only Python kernel listed).
