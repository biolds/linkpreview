from bs4 import BeautifulSoup
from linkpreview.link import Link


class PreviewBase(object):  # pragma: nocover
    """
    Base for all web preview.
    """

    def __init__(self, link: Link, parser: str, soup: 'BeautifulSoup'):
        self.link = link
        if soup:
            self._soup = soup
        else:
            self._soup = BeautifulSoup(self.link.content, parser)

    @property
    def title(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def image(self):
        raise NotImplementedError
