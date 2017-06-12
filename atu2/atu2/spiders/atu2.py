import scrapy
from scrapy.conf import settings

class WordsSpider(scrapy.Spider):
	name = "atu2" 
	
	custom_settings = { # scrape pages in order
		'DOWNLOAD_DELAY': 2, 
		'CONCURRENT_REQUESTS_PER_DOMAIN': 1
	}
	

	def start_requests(self):
		urls = []
		for i in range(0, 1260): #1260
			urls.append('https://forum.atu2.com/index.php/topic,432.'+str(i*15)+'.html')

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		for item in response.xpath('//div[contains(@class,"windowbg")]'):
			word = item.xpath('normalize-space(div/div/div/div[contains(@id, "msg_")]/text())').extract() 
			author = item.xpath('div/div/h4/a/text()').extract_first()

			yield {
			'word': word,
			'author': author 
			}


