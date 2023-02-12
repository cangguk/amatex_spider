import scrapy


class testSpider(scrapy.Spider):
    name = 'amatex_spider'
    allowed_domains = ['amatex.pl']
    start_urls = ['https://www.amatex.pl/second-hand-machinery']

    def parse(self, response):
        category_url = response.xpath('//a[contains(text(),"DETAIL")]/@href').extract() 
        for url1 in category_url:
            url_desc = response.urljoin(url1)
            yield scrapy.Request(url=url_desc, callback = self.parse_item)

   
    def parse_item(self, response):
        Url = response.url
        #Reference = Url[-5:]
        #Url = test.replace('https','http')
        #UR = response.meta['URL']
        #Description = response.xpath('//h1[@class="et_pb_column et_pb_column_1_2 et_pb_column_4_tb_body  et_pb_css_mix_blend_mode_passthrough et-last-child"]/text()|'
                                     #'//div[@class="LibDetailCaract"]/p[2]/text()|'
                                     #'//div[@class="woocommerce-product-details__short-description"]/p[3]/text()|'
                                     #'//div[@class="left_p"]/p[4]/text()|'
                                     #'//div[@class="post-content"]/p[5]/text()|'
                                     #'//h1[@class="price"]/strong/text()').extract()  
        #Description = response.xpath('//div[@class="article__wrap used-article"]/p/span[string-length(text()) > 0]/text()').extract()
        Description = response.xpath('//div[@class="bk-content-text js-text-content   wysihtml-editor-content"]/h1/text()').extract()

        yield {'description': Description,
               #'model': Model,#
               #'reference': Reference,
               #'priceee': Pricee,
               #'year': Year,
               #'price': Price,
               #'image': Img,
               #'urlreal': response.url,
               'url': Url}
             #yield scrapy.Request(item_url, callback=self.parse_cat)
