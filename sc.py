from selenium import webdriver
from selenium.webdriver.common.by import By
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

    # پیدا کردن تمام پست‌ها
    posts = driver.find_elements(By.CSS_SELECTOR, ".tag-page__posts-col li")

    # حلقه برای استخراج اطلاعات از ۱۰ رکورد اول
    for post in posts[:10]:  # فقط اولین 10 رکورد
        try:
            title = post.find_element(By.CLASS_NAME, "post-card-inline__title").text
            title_link = post.find_element(By.CLASS_NAME, "post-card-inline__title-link").get_attribute("href")
            text = post.find_element(By.CLASS_NAME, "post-card-inline__text").text

            # استفاده از WebDriverWait برای اطمینان از بارگذاری تصویر
            image_element = WebDriverWait(post, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "lazy-image__img"))
            )
            image_url = image_element.get_attribute("src")
            
            # پرینت کردن اطلاعات
            print("Title:", title)
            print("Title Link:", title_link)
            print("Text:", text)
            print("Image URL:", image_url)
            print("-" * 50)
        except Exception as e:
            print("Error:", e)

finally:
    # بستن مرورگر
    driver.quit()
