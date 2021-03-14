import re, os, sys, argparse
from urllib.parse import urlparse
import requests
#import logging

import scrapy
from scrapy.utils.project import get_project_settings as Settings
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.http.response.html import HtmlResponse
from scrapy.exceptions import IgnoreRequest

from termcolor import colored
os.system('color')

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("url", help="Url of website to scrap",
                    type=str)
args = parser.parse_args()

# base src - https://www.linode.com/docs/development/python/use-scrapy-to-extract-data-from-html-tags/
class LinkCheckerSpider(scrapy.Spider):
    name = 'link_checker'
    # For production usage specify delay to not hit performance of website
    download_delay = 0.0
    # Set the HTTP error codes that should be handled
    handle_httpstatus_list = [404]
    valid_url = []
    invalid_url = []
    # Set the maximum depth
    maxdepth = 100;
    domain = ''

    def __init__(self, url='http://www.example.com', *args, **kwargs):
        super(LinkCheckerSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(LinkCheckerSpider, cls).from_crawler(crawler, *args, **kwargs)
        # Register the spider_closed handler on spider_closed signal
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_closed(self):
        """ Handler for spider_closed signal."""
        print('----------')
        print('There are', len(self.valid_url), 'working links and',
              len(self.invalid_url), 'broken links.', sep=' ')
        if len(self.invalid_url) > 0:
            print('Broken links are:')
            for invalid in self.invalid_url:
                print(invalid)
        print('----------')

    def parse(self, response):
        """ Main method that parse downloaded pages. """
        # Set defaults for the first page that won't have any meta information
        from_url = ''
        from_text = ''
        depth = 0;
        # Extract the meta information from the response, if any
        if 'from' in response.meta: from_url = response.meta['from']
        if 'text' in response.meta: from_text = response.meta['text']
        if 'depth' in response.meta: depth = response.meta['depth']

        # If first response, update domain (to manage redirect cases)
        if len(self.domain) == 0:
            parsed_uri = urlparse(response.url)
            self.domain = parsed_uri.netloc

        # 404 error, populate the broken links array
        if response.status == 404:
            self.invalid_url.append({'url': response.url,
                                     'from': from_url,
                                     'text': from_text})

            print("%s %s %s" % (colored(response.url, 'red'), from_url, from_text))
        else:
            # Populate the working links array
            self.valid_url.append({'url': response.url,
                                   'from': from_url,
                                   'text': from_text})
            print("%s %s %s" % (colored(response.url, 'green'), from_url, from_text))


            # ----------------------------------
            # Here you are getting a flag
            r=requests.get(response.url, headers={"secure-auth":"t0p_S3cReT_k3y"})
            print("%s %s" % (r.status_code, r.text))

            # ----------------------------------

            # Extract domain of current page
            parsed_uri = urlparse(response.url)
            # Parse new links only:
            #   - if current page is not an extra domain
            #   - and depth is below maximum depth
            if parsed_uri.netloc == self.domain and depth < self.maxdepth:
                # Get all the <a> tags
                a_selectors = response.xpath("//a")
                # Loop on each tag
                for selector in a_selectors:
                    # Extract the link text
                    text = selector.xpath('text()').extract_first()
                    # Extract the link href
                    link = selector.xpath('@href').extract_first()
                    # Create a new Request object
                    request = response.follow(link, callback=self.parse)
                    request.meta['from'] = response.url;
                    request.meta['text'] = text
                    # Return it thanks to a generator
                    yield request

            return self.valid_url

# https://blog.scrapinghub.com/2016/08/25/how-to-crawl-the-web-politely-with-scrapy
settings = Settings()
# Add filtering
settings.set('[project_name].middlewares.FilterResponses', 999)
process = CrawlerProcess(settings)
process.crawl(LinkCheckerSpider, url=args.url)
process.start()
print(dir(process))
print(dir(process.spiders))
print(str(process.spiders.list))
#print(process.valid_url)'''