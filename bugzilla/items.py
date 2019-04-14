# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BugzillaItem(scrapy.Item):
    Bug_id = scrapy.Field()
    Bug_name = scrapy.Field()
    Product = scrapy.Field()
    Component = scrapy.Field()
    Reported = scrapy.Field()
    Modified = scrapy.Field()
    Assignee = scrapy.Field()
    Reporter = scrapy.Field()
    TriageOwner = scrapy.Field()
    Description = scrapy.Field()
    StepsToReproduce = scrapy.Field()
    ActualResults = scrapy.Field()
    ExpectedResults = scrapy.Field()
    # name = scrapy.Field()
    # comment = scrapy.Field()
    # activity = scrapy.Field()



