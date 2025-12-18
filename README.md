# BOSSHOSS - Automation Exercise Test Case 1

This repository contains the automation script for **Test Case 1: Register User** from [automationexercise.com](https://automationexercise.com/test_cases).

## 📋 Test Case Description

**Test Case 1: Register User** automates the complete user registration flow including:

1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

## 🛠️ Prerequisites

- Python 3.7 or higher
- Chrome browser installed
- ChromeDriver (automatically managed by webdriver-manager)

## 📦 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd BOSSHOSS
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Running the Test

Execute the test script:

```bash
python test_case_1_register_user.py
```

## 📁 Project Structure

```
BOSSHOSS/
├── test_case_1_register_user.py    # Main test automation script
├── requirements.txt                # Python dependencies
├── run_test.py                     # Test runner script
└── README.md                      # This file
```

## 🔧 Features

- **Robust Element Location**: Uses multiple selector strategies to find elements
- **Random Test Data**: Generates unique test data for each run to avoid conflicts
- **Comprehensive Logging**: Detailed step-by-step execution logs with emojis
- **Error Handling**: Graceful handling of timeouts and missing elements
- **Headless Execution**: Runs in headless mode for CI/CD compatibility
- **Clean Teardown**: Proper browser cleanup after test completion

## 📊 Test Output

The script provides detailed console output showing:
- ✅ Successful step completion
- ❌ Failed steps with error details
- ⚠️ Warnings for optional elements not found
- 🎉 Final test result

Example output:
```
🚀 Starting Test Case 1: Register User
==================================================
✅ Browser launched successfully
✅ Navigated to http://automationexercise.com
✅ Home page is visible successfully
✅ Clicked on 'Signup / Login' button
✅ 'New User Signup!' is visible
✅ Entered name: TestUserabc123
✅ Entered email: testuserabc123@example.com
...
==================================================
🎉 Test Case 1: Register User - PASSED

✅ All test steps completed successfully!
```

## 🧪 Test Data

The script automatically generates random test data including:
- Unique username and email
- Secure password
- Complete address information
- Phone number

## 🔍 Troubleshooting

If you encounter issues:

1. **ChromeDriver issues**: The script uses webdriver-manager to automatically download the correct ChromeDriver version
2. **Element not found**: The script uses multiple selector strategies and provides detailed error messages
3. **Timeout issues**: Increase the wait time in the WebDriverWait initialization if needed
4. **Headless mode issues**: Remove the `--headless` argument in `setup_driver()` to run in visible mode for debugging

## 📝 Notes

- The test runs in headless mode by default for better performance
- Each test run uses unique random data to avoid email conflicts
- The script includes comprehensive error handling and logging
- All test steps are modular and can be easily modified or extended

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is for educational and testing purposes.
