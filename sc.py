# from requests import request
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests

# # تنظیمات ChromeDriver
# chrome_options = Options()
# chrome_options.add_argument('--headless')  # اجرای مرورگر در پس‌زمینه
# chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن GPU
# chrome_options.add_argument('--no-sandbox')  # رفع مشکلات در محیط‌های محدود
# chrome_options.add_argument('--disable-dev-shm-usage')  # رفع مشکلات در محیط‌های محدود

# # مسیر ChromeDriver
# driver_path = r"C:\chromedriver-win64\chromedriver.exe"

# # شروع WebDriver
# driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# # باز کردن صفحه مورد نظر
# url = "https://www.cointelegraph.com/tags/nft"
# driver.get(url)

# # انتظار برای بارگذاری کامل عنوان
# try:
#     title_tag = driver.find_element(By.XPATH, "//h1[contains(@class, 'tag-page__title')]")
#     print("Page Title:", title_tag.text)

#     print("Page Title:", title_tag.text)
# except Exception as e:
#     print("Error:", e)

# # بستن مرورگر
# driver.quit()

sample = requests.get(url= "https://cryptopotato.com/crypto-news/")

print(sample.status_code)
if sample.status_code == 200:
    print("success!")
site_text = sample.text

soup = BeautifulSoup(site_text, "html.parser")

product_title = soup.find('h1', class_ ='entry-title')
print(product_title)