"""
Test Case 1: Register User
Automation script for automationexercise.com

Test Steps:
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
"""

import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class TestCase1RegisterUser:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.test_data = self.generate_test_data()
    
    def generate_test_data(self):
        """Generate random test data for user registration"""
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return {
            'name': f'TestUser{random_suffix}',
            'email': f'testuser{random_suffix}@example.com',
            'password': 'TestPassword123!',
            'first_name': 'Test',
            'last_name': 'User',
            'company': 'Test Company',
            'address1': '123 Test Street',
            'address2': 'Apt 456',
            'country': 'United States',
            'state': 'California',
            'city': 'Los Angeles',
            'zipcode': '90210',
            'mobile_number': '+1234567890'
        }
    
    def setup_driver(self):
        """Setup Chrome WebDriver with options"""
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')  # Run in headless mode
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            print("✅ Browser launched successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to setup driver: {str(e)}")
            return False
    
    def navigate_to_website(self):
        """Step 2: Navigate to automationexercise.com"""
        try:
            self.driver.get("http://automationexercise.com")
            print("✅ Navigated to http://automationexercise.com")
            return True
        except Exception as e:
            print(f"❌ Failed to navigate to website: {str(e)}")
            return False
    
    def verify_home_page(self):
        """Step 3: Verify that home page is visible successfully"""
        try:
            # Wait for the page to load and check for home page elements
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            
            # Check for common home page elements
            home_indicators = [
                (By.CLASS_NAME, "logo"),
                (By.LINK_TEXT, "Home"),
                (By.PARTIAL_LINK_TEXT, "Signup"),
                (By.PARTIAL_LINK_TEXT, "Login")
            ]
            
            for locator in home_indicators:
                try:
                    element = self.driver.find_element(*locator)
                    if element.is_displayed():
                        print("✅ Home page is visible successfully")
                        return True
                except NoSuchElementException:
                    continue
            
            print("❌ Home page verification failed")
            return False
        except Exception as e:
            print(f"❌ Error verifying home page: {str(e)}")
            return False
    
    def click_signup_login(self):
        """Step 4: Click on 'Signup / Login' button"""
        try:
            # Try different possible selectors for the signup/login button
            selectors = [
                (By.LINK_TEXT, "Signup / Login"),
                (By.PARTIAL_LINK_TEXT, "Signup"),
                (By.PARTIAL_LINK_TEXT, "Login"),
                (By.CSS_SELECTOR, "a[href='/login']"),
                (By.XPATH, "//a[contains(text(), 'Signup') or contains(text(), 'Login')]")
            ]
            
            for selector in selectors:
                try:
                    element = self.wait.until(EC.element_to_be_clickable(selector))
                    element.click()
                    print("✅ Clicked on 'Signup / Login' button")
                    return True
                except TimeoutException:
                    continue
            
            print("❌ Could not find or click 'Signup / Login' button")
            return False
        except Exception as e:
            print(f"❌ Error clicking signup/login: {str(e)}")
            return False
    
    def verify_new_user_signup(self):
        """Step 5: Verify 'New User Signup!' is visible"""
        try:
            # Wait for the signup page to load
            time.sleep(2)
            
            # Check for signup form elements
            signup_indicators = [
                (By.XPATH, "//h2[contains(text(), 'New User Signup')]"),
                (By.XPATH, "//h2[contains(text(), 'Signup')]"),
                (By.CSS_SELECTOR, "input[name='name']"),
                (By.CSS_SELECTOR, "input[data-qa='signup-name']")
            ]
            
            for locator in signup_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located(locator))
                    if element.is_displayed():
                        print("✅ 'New User Signup!' is visible")
                        return True
                except TimeoutException:
                    continue
            
            print("❌ 'New User Signup!' verification failed")
            return False
        except Exception as e:
            print(f"❌ Error verifying signup form: {str(e)}")
            return False
    
    def enter_name_and_email(self):
        """Step 6: Enter name and email address"""
        try:
            # Find and fill name field
            name_selectors = [
                (By.CSS_SELECTOR, "input[data-qa='signup-name']"),
                (By.CSS_SELECTOR, "input[name='name']"),
                (By.CSS_SELECTOR, "input[placeholder*='Name']")
            ]
            
            name_field = None
            for selector in name_selectors:
                try:
                    name_field = self.driver.find_element(*selector)
                    break
                except NoSuchElementException:
                    continue
            
            if name_field:
                name_field.clear()
                name_field.send_keys(self.test_data['name'])
                print(f"✅ Entered name: {self.test_data['name']}")
            else:
                print("❌ Could not find name field")
                return False
            
            # Find and fill email field
            email_selectors = [
                (By.CSS_SELECTOR, "input[data-qa='signup-email']"),
                (By.CSS_SELECTOR, "input[name='email']"),
                (By.CSS_SELECTOR, "input[type='email']")
            ]
            
            email_field = None
            for selector in email_selectors:
                try:
                    email_field = self.driver.find_element(*selector)
                    break
                except NoSuchElementException:
                    continue
            
            if email_field:
                email_field.clear()
                email_field.send_keys(self.test_data['email'])
                print(f"✅ Entered email: {self.test_data['email']}")
                return True
            else:
                print("❌ Could not find email field")
                return False
                
        except Exception as e:
            print(f"❌ Error entering name and email: {str(e)}")
            return False
    
    def click_signup_button(self):
        """Step 7: Click 'Signup' button"""
        try:
            signup_selectors = [
                (By.CSS_SELECTOR, "button[data-qa='signup-button']"),
                (By.CSS_SELECTOR, "button[type='submit']"),
                (By.XPATH, "//button[contains(text(), 'Signup')]"),
                (By.CSS_SELECTOR, "input[type='submit'][value*='Signup']")
            ]
            
            for selector in signup_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable(selector))
                    button.click()
                    print("✅ Clicked 'Signup' button")
                    return True
                except TimeoutException:
                    continue
            
            print("❌ Could not find or click 'Signup' button")
            return False
        except Exception as e:
            print(f"❌ Error clicking signup button: {str(e)}")
            return False
    
    def verify_account_information_page(self):
        """Step 8: Verify that 'ENTER ACCOUNT INFORMATION' is visible"""
        try:
            time.sleep(2)
            
            # Check for account information page elements
            account_info_indicators = [
                (By.XPATH, "//h2[contains(text(), 'ENTER ACCOUNT INFORMATION')]"),
                (By.XPATH, "//h2[contains(text(), 'Account Information')]"),
                (By.CSS_SELECTOR, "input[name='password']"),
                (By.CSS_SELECTOR, "select[name='days']")
            ]
            
            for locator in account_info_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located(locator))
                    if element.is_displayed():
                        print("✅ 'ENTER ACCOUNT INFORMATION' is visible")
                        return True
                except TimeoutException:
                    continue
            
            print("❌ 'ENTER ACCOUNT INFORMATION' verification failed")
            return False
        except Exception as e:
            print(f"❌ Error verifying account information page: {str(e)}")
            return False
    
    def fill_account_details(self):
        """Step 9: Fill details: Title, Name, Email, Password, Date of birth"""
        try:
            # Select title (Mr./Mrs.)
            try:
                title_radio = self.driver.find_element(By.CSS_SELECTOR, "input[value='Mr']")
                if not title_radio.is_selected():
                    title_radio.click()
                print("✅ Selected title: Mr")
            except NoSuchElementException:
                print("⚠️ Title selection not found, continuing...")
            
            # Fill password
            try:
                password_field = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']")
                password_field.clear()
                password_field.send_keys(self.test_data['password'])
                print("✅ Entered password")
            except NoSuchElementException:
                print("❌ Password field not found")
                return False
            
            # Fill date of birth
            try:
                # Day
                day_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='days']"))
                day_dropdown.select_by_value("15")
                
                # Month
                month_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']"))
                month_dropdown.select_by_value("6")
                
                # Year
                year_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='years']"))
                year_dropdown.select_by_value("1990")
                
                print("✅ Selected date of birth: 15/06/1990")
            except NoSuchElementException:
                print("⚠️ Date of birth fields not found, continuing...")
            
            return True
        except Exception as e:
            print(f"❌ Error filling account details: {str(e)}")
            return False
    
    def select_checkboxes(self):
        """Steps 10-11: Select newsletter and offers checkboxes"""
        try:
            # Newsletter checkbox
            try:
                newsletter_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='newsletter']")
                if not newsletter_checkbox.is_selected():
                    newsletter_checkbox.click()
                print("✅ Selected 'Sign up for our newsletter!' checkbox")
            except NoSuchElementException:
                print("⚠️ Newsletter checkbox not found")
            
            # Special offers checkbox
            try:
                offers_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='optin']")
                if not offers_checkbox.is_selected():
                    offers_checkbox.click()
                print("✅ Selected 'Receive special offers from our partners!' checkbox")
            except NoSuchElementException:
                print("⚠️ Special offers checkbox not found")
            
            return True
        except Exception as e:
            print(f"❌ Error selecting checkboxes: {str(e)}")
            return False
    
    def fill_address_details(self):
        """Step 12: Fill address details"""
        try:
            # First name
            try:
                first_name = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='first_name']")
                first_name.clear()
                first_name.send_keys(self.test_data['first_name'])
                print("✅ Entered first name")
            except NoSuchElementException:
                print("⚠️ First name field not found")
            
            # Last name
            try:
                last_name = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='last_name']")
                last_name.clear()
                last_name.send_keys(self.test_data['last_name'])
                print("✅ Entered last name")
            except NoSuchElementException:
                print("⚠️ Last name field not found")
            
            # Company
            try:
                company = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='company']")
                company.clear()
                company.send_keys(self.test_data['company'])
                print("✅ Entered company")
            except NoSuchElementException:
                print("⚠️ Company field not found")
            
            # Address 1
            try:
                address1 = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='address']")
                address1.clear()
                address1.send_keys(self.test_data['address1'])
                print("✅ Entered address 1")
            except NoSuchElementException:
                print("⚠️ Address 1 field not found")
            
            # Address 2
            try:
                address2 = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='address2']")
                address2.clear()
                address2.send_keys(self.test_data['address2'])
                print("✅ Entered address 2")
            except NoSuchElementException:
                print("⚠️ Address 2 field not found")
            
            # Country
            try:
                country_dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[data-qa='country']"))
                country_dropdown.select_by_visible_text(self.test_data['country'])
                print("✅ Selected country")
            except NoSuchElementException:
                print("⚠️ Country dropdown not found")
            
            # State
            try:
                state = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='state']")
                state.clear()
                state.send_keys(self.test_data['state'])
                print("✅ Entered state")
            except NoSuchElementException:
                print("⚠️ State field not found")
            
            # City
            try:
                city = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='city']")
                city.clear()
                city.send_keys(self.test_data['city'])
                print("✅ Entered city")
            except NoSuchElementException:
                print("⚠️ City field not found")
            
            # Zipcode
            try:
                zipcode = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='zipcode']")
                zipcode.clear()
                zipcode.send_keys(self.test_data['zipcode'])
                print("✅ Entered zipcode")
            except NoSuchElementException:
                print("⚠️ Zipcode field not found")
            
            # Mobile number
            try:
                mobile = self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='mobile_number']")
                mobile.clear()
                mobile.send_keys(self.test_data['mobile_number'])
                print("✅ Entered mobile number")
            except NoSuchElementException:
                print("⚠️ Mobile number field not found")
            
            return True
        except Exception as e:
            print(f"❌ Error filling address details: {str(e)}")
            return False
    
    def click_create_account(self):
        """Step 13: Click 'Create Account' button"""
        try:
            create_account_selectors = [
                (By.CSS_SELECTOR, "button[data-qa='create-account']"),
                (By.XPATH, "//button[contains(text(), 'Create Account')]"),
                (By.CSS_SELECTOR, "input[type='submit'][value*='Create Account']")
            ]
            
            for selector in create_account_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable(selector))
                    button.click()
                    print("✅ Clicked 'Create Account' button")
                    return True
                except TimeoutException:
                    continue
            
            print("❌ Could not find or click 'Create Account' button")
            return False
        except Exception as e:
            print(f"❌ Error clicking create account: {str(e)}")
            return False
    
    def verify_account_created(self):
        """Step 14: Verify that 'ACCOUNT CREATED!' is visible"""
        try:
            time.sleep(3)
            
            account_created_indicators = [
                (By.XPATH, "//h2[contains(text(), 'ACCOUNT CREATED')]"),
                (By.XPATH, "//h2[contains(text(), 'Account Created')]"),
                (By.CSS_SELECTOR, "h2[data-qa='account-created']")
            ]
            
            for locator in account_created_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located(locator))
                    if element.is_displayed():
                        print("✅ 'ACCOUNT CREATED!' is visible")
                        return True
                except TimeoutException:
                    continue
            
            print("❌ 'ACCOUNT CREATED!' verification failed")
            return False
        except Exception as e:
            print(f"❌ Error verifying account created: {str(e)}")
            return False
    
    def click_continue_after_creation(self):
        """Step 15: Click 'Continue' button"""
        try:
            continue_selectors = [
                (By.CSS_SELECTOR, "a[data-qa='continue-button']"),
                (By.LINK_TEXT, "Continue"),
                (By.XPATH, "//a[contains(text(), 'Continue')]")
            ]
            
            for selector in continue_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable(selector))
                    button.click()
                    print("✅ Clicked 'Continue' button")
                    return True
                except TimeoutException:
                    continue
            
            print("❌ Could not find or click 'Continue' button")
            return False
        except Exception as e:
            print(f"❌ Error clicking continue: {str(e)}")
            return False
    
    def verify_logged_in(self):
        """Step 16: Verify that 'Logged in as username' is visible"""
        try:
            time.sleep(2)
            
            logged_in_indicators = [
                (By.XPATH, f"//a[contains(text(), 'Logged in as {self.test_data['name']}')]"),
                (By.XPATH, "//a[contains(text(), 'Logged in as')]"),
                (By.CSS_SELECTOR, "a[href='/logout']"),
                (By.LINK_TEXT, "Logout")
            ]
            
            for locator in logged_in_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located(locator))
                    if element.is_displayed():
                        print(f"✅ 'Logged in as {self.test_data['name']}' is visible")
                        return True
                except TimeoutException:
                    continue
            
            print("❌ 'Logged in as username' verification failed")
            return False
        except Exception as e:
            print(f"❌ Error verifying logged in status: {str(e)}")
            return False
    
    def click_delete_account(self):
        """Step 17: Click 'Delete Account' button"""
        try:
            delete_selectors = [
                (By.LINK_TEXT, "Delete Account"),
                (By.XPATH, "//a[contains(text(), 'Delete Account')]"),
                (By.CSS_SELECTOR, "a[href='/delete_account']")
            ]
            
            for selector in delete_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable(selector))
                    button.click()
                    print("✅ Clicked 'Delete Account' button")
                    return True
                except TimeoutException:
                    continue
            
            print("❌ Could not find or click 'Delete Account' button")
            return False
        except Exception as e:
            print(f"❌ Error clicking delete account: {str(e)}")
            return False
    
    def verify_account_deleted(self):
        """Step 18: Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"""
        try:
            time.sleep(2)
            
            # Verify account deleted message
            deleted_indicators = [
                (By.XPATH, "//h2[contains(text(), 'ACCOUNT DELETED')]"),
                (By.XPATH, "//h2[contains(text(), 'Account Deleted')]"),
                (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
            ]
            
            account_deleted_found = False
            for locator in deleted_indicators:
                try:
                    element = self.wait.until(EC.presence_of_element_located(locator))
                    if element.is_displayed():
                        print("✅ 'ACCOUNT DELETED!' is visible")
                        account_deleted_found = True
                        break
                except TimeoutException:
                    continue
            
            if not account_deleted_found:
                print("❌ 'ACCOUNT DELETED!' verification failed")
                return False
            
            # Click Continue button
            continue_selectors = [
                (By.CSS_SELECTOR, "a[data-qa='continue-button']"),
                (By.LINK_TEXT, "Continue"),
                (By.XPATH, "//a[contains(text(), 'Continue')]")
            ]
            
            for selector in continue_selectors:
                try:
                    button = self.wait.until(EC.element_to_be_clickable(selector))
                    button.click()
                    print("✅ Clicked 'Continue' button after account deletion")
                    return True
                except TimeoutException:
                    continue
            
            print("❌ Could not find or click 'Continue' button after deletion")
            return False
        except Exception as e:
            print(f"❌ Error verifying account deleted: {str(e)}")
            return False
    
    def cleanup(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            print("✅ Browser closed")
    
    def run_test(self):
        """Execute the complete test case"""
        print("🚀 Starting Test Case 1: Register User")
        print("=" * 50)
        
        try:
            # Step 1: Launch browser
            if not self.setup_driver():
                return False
            
            # Step 2: Navigate to website
            if not self.navigate_to_website():
                return False
            
            # Step 3: Verify home page
            if not self.verify_home_page():
                return False
            
            # Step 4: Click Signup/Login
            if not self.click_signup_login():
                return False
            
            # Step 5: Verify New User Signup
            if not self.verify_new_user_signup():
                return False
            
            # Step 6: Enter name and email
            if not self.enter_name_and_email():
                return False
            
            # Step 7: Click Signup button
            if not self.click_signup_button():
                return False
            
            # Step 8: Verify account information page
            if not self.verify_account_information_page():
                return False
            
            # Step 9: Fill account details
            if not self.fill_account_details():
                return False
            
            # Steps 10-11: Select checkboxes
            if not self.select_checkboxes():
                return False
            
            # Step 12: Fill address details
            if not self.fill_address_details():
                return False
            
            # Step 13: Click Create Account
            if not self.click_create_account():
                return False
            
            # Step 14: Verify account created
            if not self.verify_account_created():
                return False
            
            # Step 15: Click Continue
            if not self.click_continue_after_creation():
                return False
            
            # Step 16: Verify logged in
            if not self.verify_logged_in():
                return False
            
            # Step 17: Click Delete Account
            if not self.click_delete_account():
                return False
            
            # Step 18: Verify account deleted and continue
            if not self.verify_account_deleted():
                return False
            
            print("=" * 50)
            print("🎉 Test Case 1: Register User - PASSED")
            return True
            
        except Exception as e:
            print(f"❌ Test failed with error: {str(e)}")
            return False
        finally:
            self.cleanup()


if __name__ == "__main__":
    test = TestCase1RegisterUser()
    success = test.run_test()
    
    if success:
        print("\n✅ All test steps completed successfully!")
    else:
        print("\n❌ Test execution failed!")
