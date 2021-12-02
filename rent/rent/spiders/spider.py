import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']
    


    def parse(self, response):
         
        all_rents = response.xpath('//a[@aria-label="Listing link"]/@href').getall()

        for link in all_rents:
            yield scrapy.Request('https://www.bayut.com'+link,callback=self.parse1)

        Next = response.xpath('//a[@title="Next"]/@href').get()
            
        if Next is not None:
                  pg_url = f"https://www.bayut.com{Next}"
                  request=scrapy.Request(url=pg_url,callback=self.parse1) 
                  yield request 
             
            
    def parse1(self, response): 
    

            reff_num=response.xpath('//span[@aria-label="Reference"]/text()').extract() 

            purpose=response.xpath('//li/span[@aria-label="Purpose"]/text()').extract()

            type_r=response.xpath('//span[@aria-label="Type"]/text()').extract_first()

            added_on=response.xpath('//li/span[@aria-label="Reactivated date"]/text()').extract()

            furnishing=response.xpath('//li/span[@aria-label="Furnishing"]/text()').extract()

            Price =response.xpath('//div/span[@aria-label="Price"]//text()').extract()

            currency=response.xpath('//div/span[@aria-label="Currency"]/text()').extract()

            location=response.xpath('//div[@aria-label="Property header"]/text()').extract()

            bed= response.xpath('//span[@aria-label="Beds"]//text()').extract()

            bath=response.xpath('//span[@aria-label="Baths"]//text()').extract()

            size=response.xpath('//span[@aria-label="Area"]//text()').extract()

            permit_number=response.xpath('//div/span[@class="ff863316"]/text()').extract()

            agent_name=response.xpath('//div/span[@aria-label="Agent name"]/text()').extract()

            image_url=response.xpath('//img[@title="1 "]/@src').extract()

            breadcrumbs='>'.join(response.xpath('//span[@aria-label="Link name"]//text()').extract()) 

            amenities=response.xpath('//div[@class="ef5bd664"]//text()').extract()

            description=response.xpath('//div[@aria-label="Property description"]//text()').extract()
            
            
            yield {
              
              'ref_num':reff_num,
              'purpose':purpose,
              'type_r':type_r,
              'added on':added_on,
              'furnishing':furnishing,
              'Price':{'Price':Price,
                       'currency':currency},
              'location':location,
              'bed_bath_size':{'bed' :bed,
                               'bath':bath,
                               'size':size},
                                          
              'permit_number':permit_number,
              'agent_name':agent_name,
              'image_url':image_url,
              'breadcrumbs':breadcrumbs,
              'amenities':amenities,
              'description':description,

            }
            
             

            



