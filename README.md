This project is a Python + Playwright UI automation framework built against the Sauce Demo sample e-commerce site.

## Setup

### Clone the Repository

```powershell
git clone <repo-url>
cd qa-playwright-saucedemo
```

### Create and Activate Virtual Environment

```powershell
py -3.13 -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install Python Dependencies

```powershell
python -m pip install -r requirements.txt

Note: requirements.txt installs the Python packages required by the framework, but Playwright browser binaries (Chromium, Firefox, and WebKit) must be installed separately using python -m playwright install.
```

### Install Playwright Browser Binaries

```powershell
python -m playwright install
```

### Execute Tests

```powershell
pytest
```
