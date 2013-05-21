from browser import Browser

br = Browser(stealth_mode=True)
print "test"
br.random_page()
for _ in range(10):
    print br.title
    br.visit_random_page()

