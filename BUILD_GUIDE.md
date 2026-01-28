# LaTeX Build & Workflow Guide

## Quick Start - Keyboard Shortcuts

| Shortcut         | Action       | Details                                       |
| ---------------- | ------------ | --------------------------------------------- |
| **Ctrl+Shift+B** | Full Build   | Clean old artifacts + Compile (RECOMMENDED)   |
| **Ctrl+B**       | Quick Build  | Compile only (faster, no cleaning)            |
| **Ctrl+Shift+C** | Clean Only   | Remove all generated files                    |

## What These Do

### Ctrl+Shift+B (Default Build)

```powershell
latexmk -C          # Remove old build files
latexmk -pdf main.tex   # Compile from scratch
```

✅ **Use this when:** Making significant content changes, new citations, or if you notice issues

### Ctrl+B (Quick Build)

```powershell
latexmk -pdf main.tex   # Compile with existing artifacts
```

✅ **Use this when:** Making small changes (minor text edits, formatting)

### Ctrl+Shift+C (Clean)

```powershell
latexmk -C   # Remove all .aux, .log, .bbl, etc.
```

✅ **Use this when:** You want to free up space or reset the build state

---

## Manual Build (Terminal)

Run these commands from the project root:

```powershell
# Option 1: Full clean build (recommended)
.\build.ps1

# Option 2: Direct command
latexmk -pdf main.tex
```

---

## Configuration Details

### .latexmkrc (Build Configuration)

- **$max_repeat = 8** → Prevents infinite loops by limiting build passes
- **$pdf_mode = 1** → Generates PDF (not DVI or PostScript)

This file prevents the "infinite loop" issue you experienced before.

### Build Tasks (.vscode/tasks.json)

- Defines three build tasks that can be run via keyboard or command palette
- Press `Ctrl+Shift+P` → type "Run Task" → select your preferred task

### Keybindings (.vscode/keybindings.json)

- Maps keyboard shortcuts to build tasks
- Local to this workspace (doesn't affect other VS Code projects)

---

## Troubleshooting

### Build Hangs/Times Out?

```powershell
# Check if there are compilation errors
Get-Content main.log | Select-String "Error|Fatal"
```

### References Still Undefined?

```powershell
# Run complete cycle manually
latexmk -C
latexmk -pdf main.tex
latexmk -pdf main.tex    # Run again if needed
```

### Clean Slate

```powershell
latexmk -C              # Remove all artifacts
git checkout main.tex   # Restore original file
latexmk -pdf main.tex   # Fresh build
```

---

## Branch Status

✅ **Single branch: main** (blackboxai/fix-latex-errors merged and deleted)

All changes are on `main`. No branch confusion!

---

## What's in This Repo

```text
OTPOCMRRTBHL/
├── main.tex              # Main LaTeX document
├── references.bib        # Bibliography entries
├── .latexmkrc            # Build configuration (prevents loops)
├── build.ps1             # Build script
├── .vscode/
│   ├── tasks.json        # VS Code build tasks
│   ├── keybindings.json  # Keyboard shortcuts
│   └── settings.json     # Other settings
└── figures/              # Images directory
```

---

## Pro Tips

1. **Always commit .latexmkrc** - It's critical for preventing build loops
2. **Use Ctrl+Shift+B before pushing** - Ensures clean builds work
3. **Check main.log for warnings** - Not errors, but helpful for quality
4. **Bibliography won't update?** - Use Ctrl+Shift+B to force full rebuild

---

**Last Updated:** 2026-01-28  
**Branch:** main (only)  
**Status:** ✅ Production Ready
