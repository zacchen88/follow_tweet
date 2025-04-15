## This script uses Playwright to create a session for Twitter (X) and save it to a JSON file. for later use in other scripts: follow_twet.py

from playwright.sync_api import sync_playwright

def save_twitter_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Go to Twitter login
        page.goto("https://x.com/login")

        print("🔐 Please log in manually and then press Enter in this terminal...")
        input()  # Wait for you to finish logging in

        # Save session
        context.storage_state(path="twitter_session.json")
        print("✅ Session saved to twitter_session.json")
        
        browser.close()

if __name__ == "__main__":
    save_twitter_session()
