import requests
from bs4 import BeautifulSoup

# تابع برای استخراج اطلاعات از هر پست
def get_post_data(url):
    # هدرهای HTTP برای شبیه‌سازی درخواست از مرورگر
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'
    }

    # ارسال درخواست HTTP به URL با هدرهای مشخص شده
    response = requests.get(url, headers=headers)
    
    # بررسی وضعیت درخواست
    if response.status_code != 200:
        print(f"Error loading page: {url} (Status code: {response.status_code})")
        return None

    # پارس کردن محتویات صفحه با BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

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
