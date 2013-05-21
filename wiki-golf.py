from browser import Browser

br = Browser(stealth_mode=True)
br.random_page()
print br.title
