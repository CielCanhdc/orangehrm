import os
import time
from config import Config


def screenshot_failure(item):
    if Config.screenshotFailure:
        # Create screenshot folder
        screenshots_dir = os.path.join("report", "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        # Build screenshot filename
        test_name = item.originalname
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
        screenshot_report_path = os.path.join('screenshots', f"{test_name}_{timestamp}.png")

        # Try capturing screenshot
        try:
            driver = item.funcargs['request'].getfixturevalue('init_driver')
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot captured: {screenshot_path}")
            return screenshot_report_path
        except Exception as e:
            print(f"\n⚠️ Failed to take screenshot: {e}")

    return None
