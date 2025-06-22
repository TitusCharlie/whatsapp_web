from core.interfaces import ExecutorInterface
from core.driver_factory import DriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GroupMessageExecutor(ExecutorInterface):
    def execute(self, task, profile):
        driver = DriverFactory.get_driver(profile)
        driver.get("https://web.whatsapp.com")

        try:
            # Wait for WhatsApp to load
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            search_box.clear()
            search_box.send_keys(task.target)
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
            time.sleep(2)

            msg_box = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            msg_box.send_keys(task.content)
            msg_box.send_keys(Keys.ENTER)

            print(f"[{profile}] Sent to group '{task.target}'")

        except Exception as e:
            print(f"[{profile}] ❌ Error sending group message: {e}")

        finally:
            driver.quit()


class StatusUploadExecutor(ExecutorInterface):
    def execute(self, task, profile):
        driver = DriverFactory.get_driver(profile)
        driver.get("https://web.whatsapp.com")

        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Status"]'))
            ).click()
            time.sleep(2)

            upload_btn = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((
                    By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
                ))
            )
            upload_btn.send_keys(task.media_path)
            time.sleep(5)

            # Optional caption
            if task.content:
                caption_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
                )
                caption_box.send_keys(task.content)
                time.sleep(1)

            # Send
            caption_box.send_keys(Keys.ENTER)
            print(f"[{profile}] ✅ Status uploaded")

        except Exception as e:
            print(f"[{profile}] ❌ Error uploading status: {e}")

        finally:
            driver.quit()