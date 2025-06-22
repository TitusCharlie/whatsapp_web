import os
import platform
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pathlib import Path

class DriverFactory:
    @staticmethod
    def get_driver(profile):
        chromedriver_autoinstaller.install()

        # Get Chrome path installed by Playwright
        chrome_bin_path = str(Path.home() / ".cache/ms-playwright/chromium-*/chrome-linux/chrome")
        chrome_bin_path = next(Path.home().glob(".cache/ms-playwright/**/chrome"), None)
        if chrome_bin_path is None or not chrome_bin_path.exists():
            raise RuntimeError("Chrome binary not found from Playwright")

        # Set user data dir
        if platform.system() == "Linux":
            user_data = os.path.expanduser("~/.config/google-chrome")
        elif platform.system() == "Windows":
            user_data = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data")
        else:
            user_data = os.path.expanduser("~/Library/Application Support/Google/Chrome")

        options = Options()
        options.binary_location = str(chrome_bin_path)
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--user-data-dir={user_data}")
        options.add_argument(f"--profile-directory={profile}")

        return webdriver.Chrome(options=options)