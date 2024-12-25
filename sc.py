from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# تابع برای استخراج اطلاعات از هر پست
def get_post_data(url):
    # تنظیمات برای استفاده از مرورگر Chrome بدون نمایش آن (headless)
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # اجرای مرورگر در پس‌زمینه
    chrome_options.add_argument('--no-sandbox')  # رفع مشکلات در محیط‌های محدود
    chrome_options.add_argument('--disable-dev-shm-usage')  # رفع مشکلات در محیط‌های محدود
    chrome_options.add_argument('--disable-gpu')  # غیرفعال کردن پردازش گرافیکی
    chrome_options.add_argument('--disable-software-rasterizer')  # غیرفعال کردن رندر نرم‌افزاری

    # استفاده از WebDriver برای مدیریت خودکار مرورگر
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.cointelegraph.com/tags/nft")  # URL سایت  # باز کردن صفحه وب

    # اضافه کردن تاخیر برای اطمینان از بارگذاری کامل صفحه
    time.sleep(3)  # می‌توانید زمان را بیشتر کنید اگر صفحه سنگین است

    # پارس کردن محتوای صفحه با BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # پیدا کردن تمامی تگ‌های <li> که دارای data-testid="posts-listing__item" هستند
    posts = soup.find_all('li', {'data-testid': 'posts-listing__item'})

    post_data = []
    for post in posts:
        # استخراج عنوان مقاله
        title_tag = post.find('span', {'class': 'post-card-inline__title'})
        title = title_tag.get_text(strip=True) if title_tag else "No title"

        # استخراج متن یا خلاصه مقاله
        text_tag = post.find('p', {'class': 'post-card-inline__text'})
        text = text_tag.get_text(strip=True) if text_tag else "No text available"

        # استخراج تاریخ انتشار
        date_tag = post.find('time', {'class': 'post-card-inline__date'})
        date = date_tag.get_text(strip=True) if date_tag else "No date"

        # استخراج لینک تصویر مقاله
        image_tag = post.find('img', {'class': 'lazy-image__img'})
        image_url = image_tag['src'] if image_tag else "No image"

        # ذخیره داده‌ها
        post_data.append({
            'title': title,
            'text': text,
            'date': date,
            'image_url': image_url
        })

    # بستن مرورگر
    driver.quit()

    return post_data

# URL مورد نظر برای اسکراب
url = 'https://www.cointelegraph.com/tags/nft'  # آدرس صفحه وب که می‌خواهید داده‌ها را از آن استخراج کنید

# دریافت داده‌ها از صفحه
posts = get_post_data(url)

# نمایش داده‌های استخراج شده
if posts:
    for post in posts:
        print(f"Title: {post['title']}")
        print(f"Text: {post['text']}")
        print(f"Date: {post['date']}")
        print(f"Image URL: {post['image_url']}")
        print('-' * 40)
