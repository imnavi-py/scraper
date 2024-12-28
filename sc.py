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

# sample = requests.get(url= "https://cryptopotato.com/crypto-news/")

# print(sample.status_code)
# if sample.status_code == 200:
#     print("success!")
# site_text = sample.text

# soup = BeautifulSoup(site_text, "html.parser")

# product_title = soup.find('h1', class_ ='entry-title')
# print(product_title)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# تنظیمات ChromeDriver
chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')  # در صورت نیاز فعال کنید

# مسیر ChromeDriver
driver_path = r"C:\chromedriver-win64\chromedriver.exe"

# شروع WebDriver
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

try:
    # باز کردن صفحه اصلی Google
    driver.get("********************")

    # یافتن باکس جستجو و ارسال متن
    # search_box = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.NAME, "q"))
    # )
    # search_box.send_keys("Selenium")
    # search_box.send_keys(Keys.RETURN)

    # اضافه کردن تاخیر برای بارگذاری نتایج
    time.sleep(5)

    market_news_items = driver.find_elements(By.CSS_SELECTOR, "ul.market-news__list li.market-news__item")

    # حلقه برای استخراج اطلاعات از هر آیتم
    for item in market_news_items:
        # استخراج عنوان و لینک
        title_element = item.find_element(By.CSS_SELECTOR, ".post-card-inline__title-link")
        title = title_element.text
        link = title_element.get_attribute("href")

        # استخراج توضیحات (متن کوتاه)
        description = item.find_element(By.CSS_SELECTOR, ".post-card-inline__text").text

        # استخراج تصویر (URL تصویر)
        img_element = item.find_element(By.CSS_SELECTOR, ".lazy-image__img")
        img_url = img_element.get_attribute("src")
        # چاپ اطلاعات
        print("Title:", title)
        print("Link:", link)
        print("Description:", description)
        print("Image URL:", img_url)
        print("-" * 50)


    time.sleep(5)



finally:
    # بستن مرورگر
    driver.quit()
















