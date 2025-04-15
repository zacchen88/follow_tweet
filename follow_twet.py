from playwright.sync_api import sync_playwright
import time
import random

# 📄 Load usernames from file (one per line, with or without @)
def load_usernames_from_file(file_path="follow_list.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()
    usernames = [line.strip().lstrip("@") for line in lines if line.strip()]
    return usernames

# 🦾 Follow one user using saved session
def follow_user_with_session(username, context):
    page = context.new_page()
    print(f"🔍 Visiting @{username}...")
    page.goto(f"https://x.com/{username}")
    page.wait_for_timeout(5000)  # Wait for profile to load

    try:
        profile_header = page.locator('div[data-testid="primaryColumn"]')
        follow_button = profile_header.locator('button[data-testid$="-follow"]').first

        # Wait up to 6 seconds for button to be attached & visible
        follow_button.wait_for(state="visible", timeout=6000)

        # Click follow
        follow_button.click()
        print(f"✅ Followed @{username}")
    except Exception as e:
        print(f"ℹ️ Already following @{username} or follow button not visible.")
    finally:
        page.close()


# 🧠 Main routine
def follow_all_users():
    usernames = load_usernames_from_file("follow_list.txt")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="twitter_session.json")

        for username in usernames:
            follow_user_with_session(username, context)
            delay = random.randint(5, 10)
            print(f"⏳ Waiting {delay} seconds before next user...")
            time.sleep(delay)

        browser.close()

if __name__ == "__main__":
    follow_all_users()
