from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
    # باز کردن صفحه اصلی
    driver.get("https://cointelegraph.com/markets")

    # اضافه کردن تاخیر برای بارگذاری صفحه
    time.sleep(5)

    # پیدا کردن تمام لینک‌های 'markets-more__link'
    links = driver.find_elements(By.CSS_SELECTOR, '.markets-more__link')

    # اسکرول به لینک اول (اگر بیشتر از یک لینک پیدا کردیم)
    if len(links) > 1:
        driver.execute_script("arguments[0].scrollIntoView(true);", links[1])

    # اضافه کردن تاخیر برای بارگذاری محتوای جدید
    time.sleep(2)

    # کلیک روی دومین لینک (ایندکس 1)
    if len(links) > 1:
        links[1].click()

    # اضافه کردن تاخیر برای بارگذاری محتوای جدید
    time.sleep(5)

    market_news_items = driver.find_elements(By.CSS_SELECTOR, ".market-news__item")
    count = 0
    for item in market_news_items:
        if count >= 10:
            break

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

        # افزایش شمارنده
        count += 1

finally:
    # بستن مرورگر
    driver.quit()
