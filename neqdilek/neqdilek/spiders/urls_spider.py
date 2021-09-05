import scrapy


class UrlsSpider(scrapy.Spider):

    name = 'urls'
    start_urls = [
        'https://neqdilek.com/categorie/cremerie/',
        'https://neqdilek.com/categorie/epicerie/',
        'https://neqdilek.com/categorie/biscuiterie/',
        'https://neqdilek.com/categorie/surgele/',
        'https://neqdilek.com/categorie/boisson/',
        'https://neqdilek.com/categorie/drogerie/',
        'https://neqdilek.com/categorie/hygiene/',
        'https://neqdilek.com/categorie/bebe/',
        'https://neqdilek.com/categorie/animaux/',
        'https://neqdilek.com/categorie/marche/',
    ]

    def parse(self, response):
        print(response)
        post_url = 'https://neqdilek.com/wp-admin/admin-ajax.php/?action=yith_load_product_quick_view&product_id='
        IDs = response.css('a.button.yith-wcqv-button.tbay-tooltip::attr(data-product_id)').getall()
        for id in IDs:
            product_url = post_url+str(id)
            yield {
                'id': id,
                'url': product_url
            }

        # scrape next page if exists
        next_page = response.css('a.next.page-numbers::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page)