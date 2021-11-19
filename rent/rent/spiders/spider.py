import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']



    def parse(self, response):
         with open("out.json","w") as file:
            file.write('[')
         all_rents = response.xpath('//a[@aria-label="Listing link"]/@href').getall()

         for link in all_rents:
            yield scrapy.Request('https://www.bayut.com'+link,callback=self.parse1)
            
    def parse1(self, response):
    

            

            reff_num=response.xpath('//li/span[@aria-label="Reference"]/text()').extract()[0]

            purpose=response.xpath('//li/span[@aria-label="Purpose"]/text()').extract()[0]

            type_r=response.xpath('//span[@aria-label="Type"]/text()').extract_first()

            added_on=response.xpath('//li/span[@aria-label="Reactivated date"]/text()').extract()[0]

            furnishing=response.xpath('//li/span[@aria-label="Furnishing"]/text()').extract()

            Price = response.xpath('//div/span[@aria-label="Price"]/text()').extract()[0]

            location=response.xpath('//div[@aria-label="Property header"]/text()').extract()[0]

            bed_bath_size=response.xpath('//div[@class="ba1ca68e _0ee3305d"]').extract()[0]

            permit_number=response.xpath('//div/span[@class="ff863316"]/text()').extract()[0]

            agent_name=response.xpath('//div/span[@aria-label="Agent name"]/text()').extract()[0]

            #image_url=self.start_urls[0] + ','.join(response.xpath('//img[@title="1 "]/@src')).extract()[0]

            breadcrumbs=response.xpath('//div[@aria-label="Breadcrumb"]').extract()

            amenities=response.xpath('//h3[@class="_9676c577"]').extract()

            description=response.xpath('//div/span[@aria-label="Property description"]').extract()
        
            yield {
              
              'reff_num':reff_num,
              'purpose':purpose,
              'type_r':type_r,
              'added on':added_on,
              'furnishing':furnishing,
              'Price':Price,
              'location':location,
              #'bed_bath_size':bed_bath_size,
              'permit_number':permit_number,
              'agent_name':agent_name,
              #'image_url':image_url,
              'breadcrumbs':breadcrumbs,
              'amenities':amenities,
              'description':description,
             }

         




