import re
import scrapy
from lxml import etree
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.selector import Selector
from bugzilla.items import BugzillaItem
from get_list import Get_list

class Myspider(scrapy.Spider):
    get = Get_list()
    bug_list = get.getlist()
    print('bug_list:')
    print(bug_list)
    name = 'mozilla'
    allowed_domains = ['bugzilla.mozilla.org']
    base_url = 'https://bugzilla.mozilla.org/show_bug.cgi?id='
    def start_requests(self):
        for i in range(len(self.bug_list)):
            url = self.base_url + self.bug_list[i]
            yield Request(url,self.parse)

    def parse(self, response):
        html = etree.HTML(response.text)
        soup = BeautifulSoup(response.text,"lxml")
        sel = Selector(response)
        item = BugzillaItem()
        # print(req.text)
        try:
            Bug_id = sel.xpath('//div[@id="field-value-bug_id"]/a/text()').extract()[0]
        except Exception as e:
            Bug_id = ''
        try:
            Bug_name = sel.xpath('//h1[@id="field-value-short_desc"]/text()').extract()[0]
        except Exception as e:
            Bug_name = ''
        try:
            Product = sel.xpath('//*[@id="product-name"]/text()').extract()[0]
        except Exception as e:
            Product = ''
        try:
            Component = sel.xpath('//*[@id="component-name"]/text()').extract()[0]
        except Exception as e:
            Component = ''
        try:
            Reported = sel.xpath('//*[@id="field-value-creation_ts"]/span/text()').extract()[0]
        except Exception as e:
            Reported = ''
        try:
            Modified = sel.xpath('//*[@id="field-value-delta_ts"]/span/text()').extract()[0]
        except Exception as e:
            Modified = ''
        try:
            Assinge = sel.xpath('//span[@id="field-value-assigned_to"]/div/a/span/text()').extract()[0]
        except Exception as e:
            Assinge = ''

        try:
            Reporter = sel.xpath('//span[@id="field-value-reporter"]/div/a/span/text()').extract()[0]
        except Exception as e:
            Reporter = ''
        try:
            TriageOwner = sel.xpath('//*[@id="field-value-triage_owner"]/div/a/span/text()').extract()[0]
        except Exception as e:
            TriageOwner = ''
        try:
            Description = sel.xpath('//*[@id="ct-0"]/text()').extract()[0]
        except Exception as e:
            Description = ''




        item['Bug_id'] = Bug_id
        item['Bug_name'] = Bug_name
        item['Product'] = Product
        item['Component'] = Component
        item['Reported'] = Reported
        item['Modified'] = Modified
        item['Assignee']= Assinge
        item['Reporter'] = Reporter
        item['TriageOwner'] = TriageOwner
        item['Description'] = Description
        print(item['Bug_id'])
        print(item['Bug_name'])
        print(item['Product'])
        print(item['Component'])
        print(item['Reported'])
        print(item['Modified'])
        print(item['Assignee'])
        print(item['Reporter'])
        print(item['TriageOwner'])
        print(item['Description'])
        # #people_list = driver.find_element_by_xpath('//div[@class="change-set"]')
        # people_list = html.xpath('//div[@class="change-set"]')
        # ps = soup.find_all("div", class_="change-set")
        # for p in ps:
        #     name = p.find(re.compile("^span")).text
        #     try:
        #         p.find(re.compile("^pre")).text
        #         comment = p.find(re.compile("^pre")).text
        #     except Exception as e:
        #         comment = ""
        #     try:
        #         p.find("div", class_="activity").text
        #         activity = p.find("div", class_="activity").text
        #     except Exception as e:
        #         activity = ""
        #     item['name'] = name
        #     item['comment'] = comment
        #     item['activity'] = activity
        #     name = ""
        #     comment = ""
        #     activity = ""
        yield item
