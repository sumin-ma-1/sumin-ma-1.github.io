from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge")
    page = browser.new_page(viewport={"width": 1000, "height": 480})
    page.goto("http://127.0.0.1:4174/", wait_until="networkidle")
    icon = page.locator(".material-symbols-outlined")
    box = icon.bounding_box()
    font = icon.evaluate("el => getComputedStyle(el).fontFamily")
    print("text", icon.inner_text())
    print("box", box)
    print("font", font)
    page.locator(".icons").screenshot(path=r"d:\sumin-ma-1\assets\preview-cv-icon.png")
    page.screenshot(path=r"d:\sumin-ma-1\assets\preview-home.png")
    browser.close()
print("ok")
