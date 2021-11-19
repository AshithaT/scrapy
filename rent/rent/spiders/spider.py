import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']



    def parse(self, response):
         all_rents = response.xpath('//a[@aria-label="Listing link"]/@href').getall()

         for link in all_rents:
            yield scrapy.Request(link,callback=self.parse1)
            
    def parse1(self, response):
            title = response.xpath('//div/@title').extract_first()
            reff_num=response.xpath('//li/span[@aria-label="Reference"]').extract()
            purpose=response.xpath('//li/span[@aria-label="Purpose"]').extract()
            type_r=response.xpath('//li/span[@aria-label="Type"]').extract_first()
            added_on=response.xpath('//li/span[@aria-label="Reference"]').extract()
            furnishing=response.xpath('//li/span[@aria-label="Furnishing"]').extract()
            price = response.xpath('//div/span[@aria-label="Price"]/text()').extract()
            location=response.xpath('//div[@aria-label="Property header"]').extract()
            bed_bath_size=response.xpath('//div/span[@class="fc2d1086"]').extract()
            permit_number=response.xpath('//div/span[@class="ff863316"]').extract()
            agent_name=response.xpath('//div/span[@aria-label="Agent name"]').extract()
            image_url=self.start_urls[0] + response.xpath('//img[@title="1 "]/@src').extract()
            breadcrumbs=response.xpath('//div[@aria-label="Breadcrumb"]').extract()
            amenities=response.xpath('//h3[@class="_80d7dffa"]').extract()
            description=response.xpath('//div/span[@class="cf44e740"]').extract()

            yield
            {
              'title':title,
              'reff_num':reff_num,
              'purpose':purpose,
              'type_r':type_r,
              'added on':added_on,
              'furnishing':furnishing,
              'price':price,
              'location':location,
              'bed_bath_size':bed_bath_size,
              'permit_number':permit_number,
              'agent_name':agent_name,
              'image_url':image_url,
              'breadcrumbs':breadcrumbs,
              'amenities':aminities,
              'description':description,
             }

         




