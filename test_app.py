
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.app = r"C:\Users\zahid\Documents\AppiumTests\FreeTranslator-vn_6.3.46-vc_164-debug.apk"
options.auto_grant_permissions = True

print("Starting app...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Step 1: Splash Screen
    print("Waiting for splash screen (10 seconds)...")
    time.sleep(10)
    
    # Step 2: Wait for Ad to Load
    print("Waiting for ad to appear (6 seconds)...")
    time.sleep(6)
    
    # Step 3: Close Ad Button
    print("Closing ad...")
    try:
        # Method 1: Using XPath (jo aapko mila)
        close_button = driver.find_element(
            by=AppiumBy.XPATH, 
            value='//android.view.View[@resource-id="dismiss-button"]'
        )
        close_button.click()
        print("Ad closed")
        time.sleep(2)

    except NoSuchElementException:
        print("Close button not found with XPath, trying alternative...")
        
        # Method 2: Using UiSelector (alternative)
        try:
            close_button = driver.find_element(
                by=AppiumBy.ANDROID_UIAUTOMATOR,
                value='new UiSelector().className("android.widget.TextView").instance(0)'
            )
            close_button.click()
            print("Ad closed using UiSelector!")
            time.sleep(2)
        except:
            print("Could not close ad, continuing anyway...")
    
    # Screenshot after ad
    driver.save_screenshot("after_ad_close.png")
    print("Screenshot saved: after_ad_close.png")
    
    # Step 4: Onboarding Screens (4 swipes)
    print("Swiping through onboarding screens...")
    for i in range(4):
        print(f"   Swipe {i+1}/4")
        driver.swipe(800, 1000, 200, 1000, 500)
        time.sleep(1) 
    
    driver.save_screenshot("after_onboarding.png")
    print("Screenshot saved: after_onboarding.png")
    
    # Step 5: Continue Button
    print("Looking for Continue button...")
    time.sleep(2)
    
    # Continue button dhoondhein (Inspector se milega)
    # Temporarily coordinates use kar rahe hain
    driver.tap([(540, 2100)], 100)
    time.sleep(3)
    
    # Step 6: Home Screen
    print("Reached home screen!")
    driver.save_screenshot("home_screen.png")
    print("Screenshot saved: home_screen.png")
    print("Test flow completed successfully!")

except Exception as e:
    print(f"Error occurred: {e}")
    driver.save_screenshot("error_screen.png")
    print("Error screenshot saved: error_screen.png")

finally:
    time.sleep(2)
    driver.quit()
    print("Test completed!")
Collapse
