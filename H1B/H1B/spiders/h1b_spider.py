from scrapy import Spider, Request
from H1B.items import H1BItem
import re

class H1B(Spider):

	name = 'h1b_spider'
	allowed_urls = ['https://h1bdata.info/']
	start_urls = ['https://h1bdata.info/index.php?em=&job=&city=New+York&year=2018']

	def parse(self, response):
		# Find all the table rows
		rows = response.xpath('//*[@id="myTable"]/tbody/tr') 
		
		# The movie title could be of different styles so we need to provide all the possibilities.
		for row in rows:
			# extract() will return a Python list, extract_first() will return the first element in the list
			# If you know the first element is what you want, you can use extract_first()
			employer = row.xpath('./td[1]/a/text()').extract_first()
			# Relative xpath for all the other columns
			title = row.xpath('./td[2]/a/text()').extract_first()
			salary = row.xpath('./td[3]/text()').extract_first()
			location = row.xpath('./td[4]/a/text()').extract_first().strip()
			submit_date = row.xpath('./td[5]/text()').extract_first()
			start_date = row.xpath('./td[6]/text()').extract_first()
			case_status = row.xpath('./td[7]/text()').extract_first()

			# Initialize a new WikiItem instance for each movie.
			item = H1BItem()
			item['employer'] = employer
			item['title'] = title
			item['salary'] = salary
			item['location'] = location
			item['submit_date'] = submit_date
			item['start_date'] = start_date
			item['case_status'] = case_status
			yield item