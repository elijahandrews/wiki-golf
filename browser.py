import mechanize

class Browser:
    # (Right now the browser is built specifically to visit Wikipedia pages)
    def __init__(self, stealth_mode=False):
        self.br = mechanize.Browser()
        if stealth_mode:
            self.br.set_handle_robots(False)
            self.br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
                                  ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

    def random_page(self):
        self.br.open("http://en.wikipedia.org/wiki/Special:Random")

    @property
    def title(self):
        return self.br.title().split(' - Wikipedia')[0]

