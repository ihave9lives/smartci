# SmartCI - Automation in Software Development Lab Assignment

**Student:** Sashankar J  
**USN:** 24BTRAO037  
**University:** Jain University  
**Course:** Automation in Software Development  
**Repository:** https://github.com/ihave9lives/smartci

## Project Overview

This repository contains the lab assignments for the "Automation in Software Development" course, demonstrating CI/CD pipeline setup with GitHub Actions, Python testing, and version control practices.

## Repository Structure

```
smartci/
├── src/
│   ├── __init__.py
│   ├── pricing.py      # Price calculation functions
│   ├── cart.py         # Shopping cart implementation
│   └── inventory.py    # Inventory management
├── tests/
│   ├── test_pricing.py
│   ├── test_cart.py
│   └── test_inventory.py
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI pipeline
├── requirements.txt
├── pytest.ini
└── .gitignore
```

## Lab Completion Status

| Lab | Description | Status | Tag |
|-----|-------------|--------|-----|
| Lab 0 | Project setup, folder structure, Git init, GitHub repo | ✅ Complete | - |
| Lab 1 | Application code (pricing, cart, inventory) + unit tests | ✅ Complete | `lab1` |
| Lab 2 | CI pipeline with GitHub Actions, red/green run demo | ✅ Complete | `lab2` |

## Setup Instructions

### Prerequisites
- Python 3.12+
- Git
- VS Code (recommended) with Python and GitHub Copilot extensions

### Local Setup

```bash
# Clone the repository
git clone https://github.com/ihave9lives/smartci.git
cd smartci

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux/WSL:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v
```

## Application Code

### src/pricing.py
```python
def apply_discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError('percent must be between 0 and 100')
    return round(price * (1 - percent / 100), 2)

def add_tax(price, rate=0.18):
    return round(price * (1 + rate), 2)
```

### src/cart.py
```python
from src.pricing import apply_discount, add_tax

class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
        self.items.append((name, price, qty))

    def total(self, discount=0):
        subtotal = sum(p * q for _, p, q in self.items)
        return add_tax(apply_discount(subtotal, discount))
```

### src/inventory.py
```python
class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, name, qty):
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove_stock(self, name, qty):
        if self.stock.get(name, 0) < qty:
            raise ValueError('not enough stock')
        self.stock[name] -= qty
```

## Tests

All 9 tests pass covering:
- **Pricing**: Basic discount, boundaries (0%, 100%), invalid input (>100%), tax calculation
- **Cart**: Total with discount, empty cart
- **Inventory**: Add stock, remove stock, insufficient stock raises ValueError

```bash
pytest -v
# 9 passed in 0.04s
```

## CI Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push and pull request:

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - name: Run tests
        run: |
          set -o pipefail
          pytest 2>&1 | tee build.log
```

### Workflow Steps Explained

| Step | Purpose |
|------|---------|
| `actions/checkout@v4` | Downloads the repository code to the runner |
| `fetch-depth: 0` | Fetches full git history (needed for git diff in future labs) |
| `actions/setup-python@v5` | Installs Python 3.12 on the runner |
| `pip install -r requirements.txt` | Installs pytest and requests |
| `pytest 2>&1 \| tee build.log` | Runs tests, shows output AND saves to build.log |

## Red/Green Run Demonstration

### Red Run (Failure) - Commit `59f6484`
**Purpose:** Deliberately break a test to demonstrate CI failure detection

**Error Location:** In GitHub Actions → Actions tab → CI workflow → build job → "Run set -o pipefail" step

**Error Output:**
```
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.6.0
collected 9 items

tests/test_cart.py ..                                                    [ 22%]
tests/test_inventory.py ...                                              [ 55%]
tests/test_pricing.py .F..                                               [100%]

=================================== FAILURES ===================================
___________________________ test_discount_boundaries ___________________________

    def test_discount_boundaries():
>       assert apply_discount(100, 0) == 101.0
E       assert 100.0 == 101.0
E        +  where 100.0 = apply_discount(100, 0)

tests/test_pricing.py:8: AssertionError
====================== 1 failed, 8 passed in 0.02s =========================
##[error]Process completed with exit code 1.
```

**Why Red Runs Are Useful:**
1. **Early Detection** - Catches regressions immediately on push
2. **Visibility** - Shows exactly which test failed and why
3. **Accountability** - Prevents broken code from merging
4. **Documentation** - Creates a record of what broke and when

### Green Run (Success) - Commit `53ff836` (tagged `lab2`)
**Purpose:** Fix the test and show passing pipeline

**Output:**
```
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.6.0
collected 9 items

tests/test_cart.py ..                                                    [ 22%]
tests/test_inventory.py ...                                              [ 55%]
tests/test_pricing.py ....                                               [100%]

============================== 9 passed in 0.02s ===============================
```

## GitHub Actions Error Identification

In the GitHub Actions UI, the error appears in these locations:

1. **Actions Tab** → **CI workflow** → Red X icon on the failed run
2. **Build Job** → Click "build" → Expand "Run set -o pipefail" step
3. **Logs** → Scroll to "FAILURES" section showing the exact assertion error
4. **Summary** → "1 failed, 8 passed" with red annotation

## Commit History

```
53ff836 Lab 2: fix test - green run (tag: lab2)
59f6484 Lab 2: experiment - break test to show red run
67e4e14 Lab 2: baseline CI pipeline
943d0e3 Lab 0: project skeleton + Lab 1: app and tests (tag: lab1)
```

## Tags

- `lab1` - Lab 1 completion (app + tests)
- `lab2` - Lab 2 completion (CI pipeline with red/green demo)

## Verification

- ✅ All tests pass locally and in CI
- ✅ Repository is public at https://github.com/ihave9lives/smartci
- ✅ GitHub Actions workflow runs on push/PR
- ✅ Red run (failure) and Green run (success) both visible in Actions history
- ✅ Tags `lab1` and `lab2` pushed to remote

## Submission

This repository fulfills all requirements for the Automation in Software Development lab assignment (Labs 0, 1, and 2).