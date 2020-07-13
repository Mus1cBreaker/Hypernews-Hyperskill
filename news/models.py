from django.db import models
from hypernews.settings import NEWS_JSON_PATH
from collections import OrderedDict
import json, random
# Create your models here.


# class News(models.Model):
#     created = models.DateField()
#     text = models.CharField(max_length=50)
#     title = models.CharField(max_length=50)
#     link = models.IntegerField(max_length=7, prim


class News:
    with open(NEWS_JSON_PATH, 'r') as news_json:
        news = json.load(news_json)
    links = []

    def add_news(self, _news):
        self.news.append(_news)
        return

    def get_sorted_by_date(self):
        sorted_by_date = OrderedDict()
        for element in sorted(self.news, key=lambda k: k['created'], reverse=True):
            self.links.append(element["link"])
            if not sorted_by_date.get(element["created"].split()[0]):
                sorted_by_date[element["created"].split()[0]] = []
            sorted_by_date[element["created"].split()[0]].append(element)
        return sorted_by_date

    def get_desired_news(self, title):
        _sorted = self.get_sorted_by_date()
        for key in _sorted:
            for element in _sorted.get(key):
                if title in element["title"]:
                    _desired = OrderedDict()
                    _desired[key] = []
                    _desired[key].append(element)
                    return _desired
        return

    def get_link(self):
        for i in range(len(self.links)):
            if i not in self.links:
                return i
        while True:
            i = random.randint()
            if i not in self.links:
                return i