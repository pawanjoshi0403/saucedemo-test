# Sauce Demo Test Automation Suite

This test suite automates key user workflows for the [Sauce Demo](https://www.saucedemo.com/) e-commerce website using Playwright and pytest.

## 🛠 Setup Instructions

### Prerequisites
- Python 3.7+
- pip package manager
- Git (for version control)

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/pawanjoshi0403/saucedemo-test.git
   cd saucedemo-tests
   
2. **Create virtual environment**
     ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
   
3. **Install dependencies**
    ```bash
   pip install -r requirements.txt

4. **Install Playwright browsers**
    ```bash
   playwright install chromium
### 🚀 Running Tests

Basic Test Execution
```bash
    pytest tests/ -v
   ```

Advanced Options

| Command                            | Description                          |
|-------------------------------------|--------------------------------------|
| `pytest tests/ -n 4`               | Run tests in parallel (4 workers)   |
| `pytest tests/ --html=report.html` | Generate HTML test report           |
| `pytest tests/test_login.py`       | Run specific test file              |
| `pytest -k "test_login"`           | Run tests matching name pattern     |

### PyCharm Setup

1. Open project in PyCharm
2. Set Python interpreter:
   * File > Settings > Project > Python Interpreter
   * Select your venv Python executable

3. Configure pytest:
   * File > Settings > Tools > Python Integrated Tools
   * Set test runner to pytest

### 📋 Test Coverage
Core Features Verified
* ✅ User authentication (valid/invalid credentials)
* ✅ Product sorting (price low-high, high-low, A-Z, Z-A)
* ✅ Inventory verification (item counts, details)
* ✅ Cart management (add/remove items)
* ✅ Checkout process (shipping info, order confirmation)
* ✅ Session management (logout)

### Edge Cases Tested
* 🔒 Locked user account
* 🚫 Empty credentials
* 📦 Single/multiple item purchases
* 📝 Invalid shipping information

### 📊 Test Reports
After test execution, view detailed HTML reports:
1. Open report.html in your browser
2. Analyze:
   * Pass/fail status
   * Execution times
   * Error messages
   * Screenshots (for failed tests)
