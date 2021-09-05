import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['neqdilek.com']
    start_urls = ['http://neqdilek.com/']

    def parse(self, response):
        pass
