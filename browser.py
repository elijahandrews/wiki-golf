import mechanize
import random

class Browser:
    # (Right now the browser is built specifically to visit Wikipedia pages)
    def __init__(self, stealth_mode=False):
        self.br = mechanize.Browser()
        # TODO: Use Wikipedia API so I don't have to use stealth mode
        if stealth_mode:
            self.br.set_handle_robots(False)
            self.br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
                                  ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

    def random_page(self):
        while(True):
            self.br.open("http://en.wikipedia.org/wiki/Special:Random")
            # (try not to land on a stub)
            if len(self._get_links()) > 1:
                break

    def visit_random_page(self):
        links = self._get_links()
        self.br.follow_link(links[random.randint(0, len(links) - 1)])

    @property
    def title(self):
        return self.br.title().split(' - Wikipedia')[0]

    def _get_links(self):
        return list(self.br.links(url_regex='en.*wikipedia.org/wiki/(?!Wikipedia)'))
