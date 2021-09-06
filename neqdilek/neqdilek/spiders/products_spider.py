import scrapy
import pandas as pd


class ProductsSpider(scrapy.Spider):

    name = 'products'
    
    df_urls = pd.read_csv(r'urls.csv')
    df_urls.drop_duplicates(inplace=True)
    start_urls = list(df_urls.url)

    def parse(self, response):
        title = response.css('h1.product_title.entry-title::text').get()
        tagged_as = response.css('span.tagged_as').css('a::text').get()
        brand = response.xpath('//span[@itemprop="brand"]/a/text()').get()
        image_url = response.css('img.attachment-woocommerce_single.size-woocommerce_single.wp-post-image::attr(src)').get()
        price = response.xpath('//p[@class = "price"]/span/bdi').css('::text').get()
        categories = response.xpath('//span[@class="posted_in"]/a/text()').getall()
        categories = ', '.join(categories)

        yield {
            "titre": title,
            "étiquette": tagged_as,
            "marque": brand,
            "prix": price,
            "categories": categories,
            "image_url": image_url
        }

