import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    # def start_requests(self):
    #     url=['https://www.bayut.com/to-rent/property/dubai/?furnishing_status=furnished']
    #     yield scrapy.Request(url='all_rents', callback=self.parse)

    # def parse1(self,response):
    #     return scrapy.request("https://www.bayut.com/to-rent/property/dubai/?furnishing_status=furnished",callback=self.parse)

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

            print(title)
            print(reff_num)
            print(purpose)
            print(type_r)
            print(added_on)
            print(furnishing)
            print(price)
            print(location)
            print(bed_bath_size)
            print(permit_number)
            print(agent_name)
            print(image_url)
            print(breadcrumbs)
            print(amenities)
            print(description)


         




