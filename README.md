# X_Login

Playwrightを使ってX（旧Twitter）に自動ログインするPythonクラスです。

## 特徴
- Playwrightによるブラウザ自動操作
- Cookie保存・再利用によるセッション管理
- 人間らしいタイピング・遅延の再現
- ログイン維持が出来るため、アカウント凍結のリスクが大幅に軽減

## 必要要件
- Python 3.8以上
- [playwright](https://playwright.dev/python/) ライブラリ

## インストール
```bash
pip install playwright
playwright install
```

## 使い方
```python
from x_login import X_Login
from playwright.sync_api import sync_playwright

email = "your_email@example.com"
username = "your_username" #ログイン時に求められた場合のみ
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

## 注意事項
- このクラスの利用は自己責任でお願いします。
- 開発者は一切の責任も負いません。
- X（旧Twitter）の仕様変更により動作しなくなる場合があります。

## ライセンス
MIT License
