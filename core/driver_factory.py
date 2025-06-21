import os, platform, chromedriver_autoinstaller
from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(profile):
        chromedriver_autoinstaller.install()

        # Platform-specific Chrome user data directory
        if platform.system() == "Linux":
            base = os.path.expanduser("~/.config/google-chrome")
        elif platform.system() == "Windows":
            base = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data")
        else:
            base = os.path.expanduser("~/Library/Application Support/Google/Chrome")

        options = webdriver.ChromeOptions()
        options.binary_location = os.getenv("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--user-data-dir={base}")
        options.add_argument(f"--profile-directory={profile}")
        return webdriver.Chrome(options=options)