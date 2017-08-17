import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	start_urls = [
		'http://quotes.toscrape.com/tag/humor'
	]

	def parse(self, response):
		for quote in response.css('div.quote'): #class=row/class=colmd8/class=quote
			yield {
				'text':quote.css('span.text::text').extract_first(),
				''
			}