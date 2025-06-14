from playwright.sync_api import sync_playwright
import os
import pickle
import random
import time

class X_Login:
    def __init__(self, email, username, password, cookie_file="user_data/cookies.pkl"):
        self.email = email
        self.username = username
        self.password = password
        self.cookie_file = cookie_file

    def save_cookies(self, context):
        cookies = context.cookies()
        with open(self.cookie_file, "wb") as f:
            pickle.dump(cookies, f)

    def load_cookies(self, context):
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, "rb") as f:
                cookies = pickle.load(f)
            context.add_cookies(cookies)
            return True
        return False

    def is_logged_in(self, page):
        try:
            page.goto("https://x.com/home", timeout=15000)
            page.wait_for_selector('nav[role="navigation"]', timeout=10000)
            return True
        except Exception:
            return False

    def login(self, browser, page):
        # セッション用cookieがあれば読み込み
        cookies_loaded = self.load_cookies(browser)
        page.goto("https://x.com", timeout=20000)
        if not self.is_logged_in(page):
            browser.clear_cookies()
            page.evaluate("window.localStorage.clear(); window.sessionStorage.clear();")
            time.sleep(2)
            referers = ["https://www.google.com/", "https://www.bing.com/", "https://www.yahoo.co.jp/"]
            page.set_extra_http_headers({"Referer": random.choice(referers)})
            def human_type(element, text):
                for c in text:
                    element.type(c, delay=random.uniform(50, 180))
                    if random.random() < 0.1:
                        time.sleep(random.uniform(0.05, 0.2))
            def human_delay(base=1.0, var=0.7):
                time.sleep(base + random.uniform(0, var))
            page.goto("https://x.com/login", timeout=20000)
            human_delay(1.2, 1.0)
            email_input = page.locator('input[name="text"]')
            email_input.click()
            human_type(email_input, self.email)
            human_delay(0.8, 0.7)
            page.get_by_text("次へ").click()
            human_delay(1.5, 1.2)
            if page.locator('input[data-testid="ocfEnterTextTextInput"]').is_visible():
                user_input = page.locator('input[data-testid="ocfEnterTextTextInput"]')
                user_input.click()
                human_type(user_input, self.username)
                human_delay(1.0, 0.8)
                if page.locator('button[data-testid="ocfEnterTextNextButton"]').is_visible():
                    page.locator('button[data-testid="ocfEnterTextNextButton"]').click()
                    human_delay(1.2, 1.0)
            elif page.locator('button[data-testid="ocfEnterTextNextButton"]').is_visible():
                page.locator('button[data-testid="ocfEnterTextNextButton"]').click()
                human_delay(1.2, 1.0)
            pw_input = page.locator('input[name="password"]')
            pw_input.click()
            human_type(pw_input, self.password)
            human_delay(1.0, 0.8)
            page.locator('button[data-testid="LoginForm_Login_Button"]').click()
            human_delay(3.0, 2.0)
            self.save_cookies(browser)
            return True
        else:
            print("既存cookieセッションでログイン済みです")
            return True
