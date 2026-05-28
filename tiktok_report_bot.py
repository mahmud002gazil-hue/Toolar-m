from playwright.sync_api import sync_playwright
import time

TIKTOK_USERNAME = "kullaniciadiniz"
TIKTOK_PASSWORD = "sifreniz"
VIDEO_URL = "https://www.tiktok.com/@kullanici/video/1234567890"

def report_video(video_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # TikTok'a giriş
        page.goto("https://www.tiktok.com/login")
        time.sleep(3)
        # Giriş formunu doldurmak için uygun selector'ları bulmalısın.
        # (TikTok sık sık DOM yapısını değiştirir!)
        page.fill('input[name="username"]', TIKTOK_USERNAME)
        page.fill('input[type="password"]', TIKTOK_PASSWORD)
        page.click('button[type="submit"]')
        time.sleep(5)

        # Videoya git
        page.goto(video_url)
        time.sleep(5)

        # Report (Şikayet) butonuna tıkla
        # TikTok UI/HTML yapılarını bulup ilgili butonların selector'larını update etmelisin!
        page.click('button[aria-label="More actions"]')
        time.sleep(1)
        page.click('text="Report"')
        time.sleep(1)

        # Şikayet sebebini seçip gönder
        page.click('text="Inappropriate Content"')  # seçeneğe göre değiştir
        page.click('text="Submit"')
        time.sleep(2)

        browser.close()

if __name__ == '__main__':
    report_video(VIDEO_URL)