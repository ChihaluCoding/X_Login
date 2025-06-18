# X_Login（開発終了）

類似プロジェクト↓
### ※開発中※
---

- Playwrightを使ってX（旧Twitter）に自動ログインするPythonクラス（ライブラリ）です。
- ログイン状態の維持が出来るのでアカウント凍結のリスクが大幅に軽減されます。
- XのHTMLの仕様が変わればもちろん使えなくなります。
---

※2025/06/18現在動作確認済み※


## 使い方
```python
from x_login import X_Login
from playwright.sync_api import sync_playwright

email = "your_email@example.com"
username = "your_username"
password = "your_password"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    x = X_Login(email, username, password)
    x.login(context, page)
    # ここでログイン後の操作が可能
    browser.close()
```

## ライセンス
MIT License
