import requests
from bs4 import BeautifulSoup

def get_instagram_info(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return f"❌ ما قدرت أوصل لحساب Instagram: {username}"

    soup = BeautifulSoup(res.text, "html.parser")
    try:
        description = soup.find("meta", {"name": "description"})["content"]
        profile_pic = soup.find("meta", {"property": "og:image"})["content"]
        return {
            "platform": "Instagram",
            "username": username,
            "description": description,
            "profile_pic": profile_pic,
            "link": url
        }
    except Exception as e:
        return f"⚠️ حصل خطأ أثناء تحليل صفحة Instagram: {e}"

def get_tiktok_info(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return f"❌ ما قدرت أوصل لحساب TikTok: {username}"

    soup = BeautifulSoup(res.text, "html.parser")
    try:
        description = soup.find("meta", {"name": "description"})["content"]
        profile_pic = soup.find("meta", {"property": "og:image"})["content"]
        return {
            "platform": "TikTok",
            "username": username,
            "description": description,
            "profile_pic": profile_pic,
            "link": url
        }
    except Exception as e:
        return f"⚠️ حصل خطأ أثناء تحليل صفحة TikTok: {e}"

# تجربة
username = input("اكتب اسم المستخدم: ")
print("\n--- Instagram ---")
print(get_instagram_info(username))
print("\n--- TikTok ---")
print(get_tiktok_info(username))
