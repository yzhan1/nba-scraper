import os
import json
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'static', "data.json")
        self.urls = self.get_urls()
        open(json_url, 'w').close()
        self.file = open(json_url, 'w')

    # def main():
    #     urls = get_urls(self)
    #     file = open("data.json", "w")
    #     scrape(self, urls, file)

    @staticmethod
    def get_urls():
        urls = ['https://voice.hupu.com/nba/{}'.format(str(i)) for i in range(1, 100, 1)]
        return urls

    def scrape(self):
        print('Begin scraping')
        res = []
        for url in self.urls:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            lst = soup.select('div.news-list ul li')
            for li in lst:
                tag_class = li.get('class')
                if tag_class is None:
                    other_info = li.find('div', {'class': 'otherInfo'})
                    other_left = other_info.find('span', {'class': 'other-left'})
                    time_tag = other_left.find('a', {'class': 'time'})
                    from_tag = other_left.find('span', {'class': 'comeFrom'})
                    item = {
                        'text': li.div.h4.a.text,
                        'link': li.div.h4.a['href'],
                        'time': time_tag.text,
                        'from': from_tag.text
                    }
                    res.append(item)
        json.dump(res, self.file, ensure_ascii=False)
        self.file.close()
        print('Done scraping')
        return res

if __name__ == '__main__':
    scraper = Scraper()
    scraper.scrape()