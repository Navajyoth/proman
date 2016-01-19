import urllib2
from bs4 import BeautifulSoup

from .models import Article


class ParseData(object):

    def __init__(self, item):
        self.url = item.url
        self.target_tags = item.TAGS
        self.item = item
        self._fetch_page()

    def _fetch_page(self):
        req = urllib2.Request(self.url, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        soup = BeautifulSoup(con.read(), "html5lib")
        self.meta = soup.findAll('meta')
        self.title_tag = soup.findAll('title')[0]
        self.short_description = ""

    def add_title(self):
        title_lines = [str(line) for line in self.meta if 'property="og:title"' in line]
        if title_lines:
            line = title_line[0]
            start = line.find('content="') + len('content="')
            heading = line[start: ][: line[start: ].find('"')]
            title = heading.decode('utf-8')
        else:
            title = str(self.title_tag)
            start = title.find('<title>') + len('<title>')
            heading = title[start: ][: title[start: ].find('</title>')]
            title = heading.decode('utf-8')
        self.item.title = title

    def add_short_description(self):
        description_lines = [str(line) for line in self.meta if 'property="og:description"' in line]
        if description_lines:
            line = description_lines[0]
            start = line.find('content="') + len('content="')
            description = line[start: ][: line[start: ].find('"')]
            self.item.short_description = description.decode('utf-8')

    def add_image(self):
        image_lines = [str(line) for line in self.meta if 'property="og:image"' in line]
        if image_lines:
            line = image_lines[0]
            start = line.find('content="') + len('content="')
            image_url = line[start: ][: line[start: ].find('"')]
            self.item.image_url = image_url
        else:
            self.item.image_url = ""

    def add_tags(self):
        tag_lines = [str(line) for line in self.meta if 'name="keywords"' in line]
        if tag_lines:
            line = tag_lines[0]
            start = line.find('content="') + len('content="')
            tags = line[start: ][: line[start: ].find('"')]
            tags = self.find_tags_from_keywords(tags[: 64].decode('utf-8'))
        else:
            tags = self.find_tags_from_data(
                str(self.title_tag).decode('utf-8')+" "+self.short_description.decode('utf-8')
            )
        self.item.tags = tags

    def find_tags_from_keywords(self, tag_str):
        article_tags = [t.strip().lower() for t in tag_str.split(',')]
        result = list(set(self.target_tags) & set(article_tags))
        return ','.join(result)

    def find_tags_from_data(self, str_data):
        result = []
        article_words = [s.strip().lower() for s in str_data.split(' ')]
        result = list(set(self.target_tags) & set(article_words))
        return ','.join(result)

    def update_article(self):
        self.add_title()
        self.add_short_description()
        self.add_tags()
        self.add_image()
        self.item.save()
