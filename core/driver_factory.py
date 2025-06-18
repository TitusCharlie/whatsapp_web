import os, platform
import chromedriver_autoinstaller
from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(profile):
        # Install matching chromedriver
        chromedriver_autoinstaller.install()

        # Set user-data-dir based on OS
        if platform.system() == "Linux":
            base = os.path.expanduser("~/.config/google-chrome")
        elif platform.system() == "Windows":
            base = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data")
        else:
            base = os.path.expanduser("~/Library/Application Support/Google/Chrome")

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--user-data-dir={base}")
        options.add_argument(f"--profile-directory={profile}")
        return webdriver.Chrome(options=options)