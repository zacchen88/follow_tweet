from playwright.sync_api import sync_playwright
import random
import time

COMMUNITY_URL = "https://x.com/i/communities/1669241668829323264/members"

def follow_members():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="twitter_session.json")
        page = context.new_page()

        print("🌐 Navigating to community...")
        page.goto(COMMUNITY_URL, timeout=60000)
        time.sleep(5)

        followed = 0
        seen = set()

        for _ in range(15):  # Scroll and repeat
            page.mouse.wheel(0, 2000)
            time.sleep(2)

            buttons = page.locator("button[data-testid$='-follow']").element_handles()

            for btn in buttons:
                try:
                    aria_label = btn.get_attribute("aria-label")
                    if not aria_label or "Follow @" not in aria_label:
                        continue

                    username = aria_label.replace("Follow @", "").strip()
                    if username in seen:
                        continue

                    btn.scroll_into_view_if_needed()
                    time.sleep(random.uniform(1.5, 2.5))
                    btn.click()

                    seen.add(username)
                    wait = random.randint(5, 10)
                    followed += 1
                    print(f"✅ Followed @{username} (#{followed}) | Waiting {wait}s...")
                    time.sleep(wait)

                except Exception as e:
                    print(f"⚠️ Skipped one: {e}")
                    continue

        print(f"🎉 Finished following {followed} new members.")
        browser.close()

if __name__ == "__main__":
    follow_members()
