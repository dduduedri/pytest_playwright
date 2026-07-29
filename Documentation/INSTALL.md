# Installation Guide

First-time setup for the **pytest + Playwright** framework.

## Prerequisites

- Python 3.9 or newer (`python --version`)
- Git

## 1. Clone the repository

```bash
git clone <repository-url>
cd pytest_playwright
```

## 2. Create and activate a virtual environment

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> If activation is blocked, allow scripts for the current user once:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Windows (Command Prompt)

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## 5. Install Playwright browsers

This downloads the browser binaries required by Playwright:

```bash
playwright install
```

To install only a specific browser (optional):

```bash
playwright install chromium
```

## 6. Verify the installation

```bash
pytest --version
playwright --version
```

## 7. Run the tests

```bash
pytest -s
```

Run in headed mode (visible browser):

```bash
pytest -s --headed
```

Run against a specific browser:

```bash
pytest -s --headed --browser_name firefox
```

Run in parallel across CPU cores (via `pytest-xdist`):

```bash
pytest -n auto   # one worker per CPU core
pytest -n 3      # use a specific number of workers
```

## Deactivate the virtual environment

When you are finished working:

```bash
deactivate
```
