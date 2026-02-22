# Databricks extension – stuck on “Initializing”

**Recommended version: 2.4.8** – last version before the “stuck initializing” bug (2.5.0+ waits on debugpy and can hang).

The marketplace only shows the last few versions, so **2.4.8 is not in “Install Another Version”**. You can still install it from GitHub.

## Install 2.4.8 from VSIX (workaround)

1. **Uninstall** the current Databricks extension (Extensions → Databricks → Uninstall).
2. **Download** the right VSIX for your machine from the [2.4.8 release](https://github.com/databricks/databricks-vscode/releases/tag/release-v2.4.8):
   - **macOS Apple Silicon:** [databricks-darwin-arm64-2.4.8.vsix](https://github.com/databricks/databricks-vscode/releases/download/release-v2.4.8/databricks-darwin-arm64-2.4.8.vsix)
   - **macOS Intel:** [databricks-darwin-x64-2.4.8.vsix](https://github.com/databricks/databricks-vscode/releases/download/release-v2.4.8/databricks-darwin-x64-2.4.8.vsix)
   - **Windows/Linux:** see the [Assets](https://github.com/databricks/databricks-vscode/releases/tag/release-v2.4.8) on the same page.
3. In Cursor/VS Code: **Extensions** → **⋯** (top right) → **Install from VSIX…** → select the downloaded `.vsix`.
4. Reload the window.

## Or fix the current extension (no downgrade)

From 2.5.0 the extension waits for **ms-python.debugpy**. If that fails to activate, the sidebar stays on “Initializing”.

- **View → Output** → choose **Extension Host** or **Databricks Logs**. Look for errors mentioning `debugpy` or `EACCES`.
- Install **“Debugger for Python”** (`ms-python.debugpy`) from the marketplace so the dependency is present.
- If you see permission errors under `.vscode/extensions/ms-python.debugpy/`, fix write access there (e.g. Nix/read-only installs often cause this).
- Try disabling Python experiments in settings: search for `python.experiments.enabled` and set to `false`.

Workspace setting `databricks.logs.enabled` is already `true` here so Databricks logs show in the Output panel.

---

## “Extension activation failed”

To see the real error:

1. **Cmd+Shift+P** (or Ctrl+Shift+P) → run **“Developer: Toggle Developer Tools”**.
2. Open the **Console** tab and look for red errors when the Databricks extension loads (e.g. on startup or when you open a Databricks view).
3. You can also check **View → Output** → **Extension Host** for activation errors.

**Common causes:**

- **Wrong VSIX architecture** – e.g. installed `darwin-x64` on Apple Silicon (or the reverse). Uninstall the extension and install the correct [2.4.8 VSIX](https://github.com/databricks/databricks-vscode/releases/tag/release-v2.4.8) for your OS/arch.
- **Editor too new for 2.4.8** – Extension 2.4.8 (Oct 2024) may not support very recent Cursor/VS Code engine versions. If the Console shows an API or engine compatibility error, use the **latest** Databricks extension from the marketplace and fix the “Initializing” issue instead (ensure **Debugger for Python** is installed and activates; see “Or fix the current extension” above).
- **Missing or broken dependency** – e.g. Node native module or bundled CLI. Re-download the VSIX and reinstall, or try the latest extension.

Once you have the exact error from the Console, you can search it or report it for a precise fix.

### “paths[1] must be of type string. Received undefined” (Python Envs)

If the Console shows: **Activating extension 'ms-python.vscode-python-envs' failed: The "paths[1]" argument must be of type string. Received undefined**, the chain is: **Python Envs** → **Python** → **Python Debugger** → **Databricks** (all fail).

This can be triggered by `python-envs.pythonProjects` in workspace settings when `${workspaceFolder}` isn’t resolved in time. The workspace settings here no longer set `python-envs.pythonProjects`; the interpreter is set via `python.defaultInterpreterPath` instead. Reload the window after the change.
