# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "GDPR"

    def start_requests(self):
        urls = []
        file = open("urls_new_policies_3.txt","r")
        for line in file:
            if line != "None":
                urls.append(line)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[7]
        filename = 'new_policy_%s.html' % page
        with open("new/"+filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)