# web-crawler
Web crawler for Hong Kong Public Libraries website. Implemented with python.

<hr/>

## Explanation
We are to implement a crawler + parser (thereafter *crawler* for short) to achieve the following functionalities:
1. When we feed the crawler with a list of ***N*** URLs, the crawler is able to extract the desired data fields on that web page, and should output in comma-separated-format with all fields on one line.
2. For any dummy data field on a web page, the crawler should detect it and mark it with a special value (e.g. ```0``` for numeric field or ```NULL``` for string field).
3. The ***N*** rows in the output CSV file should match exactly the ***N*** URLs in the list.

<hr/>

## Crawler workflow explained
- I explained the workflow in this [video] (https://github.com/robbin647/web-crawler/tree/main/help_files/crawler_workflow.webm) 
- A [photo] (https://github.com/robbin647/web-crawler/tree/main/help_files/crawler_workflow.png) of the workflow 

<hr/>

## Useful sources
1. Perkovic, L. “11.2 Python WWW API”, in Introduction to Computing Using Python, 2nd Edition. John Wiley & Sons, Inc: USA. 2012. The website for this [book] (https://ucsb-cs8.github.io/textbooks/Perk2e/)
2.	[scrapy, w3lib, extruct] (https://www.scrapingbee.com/blog/crawling-python/). [Scrapy documentation] (https://docs.scrapy.org/en/latest/)
3.	[How to use Scrapy] (https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python#compare)
4.	BeautifulSoup: Beautiful Soup is also widely used for web scraping. It is a Python package for parsing HTML and XML documents and extract data from them. [Tutorial] (https://www.datacamp.com/community/tutorials/tutorial-python-beautifulsoup-datacamp-tutorials)
