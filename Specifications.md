# Specifications of the crawler

_Last updated: June 23, 2021 21:00_

## Task breakdown
- We need to implement Step 4 & 5 in the [workflow] (https://github.com/robbin647/web-crawler/help_files/crawler_workflow.png)
- - Step 4: The HTML Parser parse the HTML document and extract the required fields
- - Step 5: The Parser outputs data in comma separated format, one line for each book

- Taskforce:
- - Taskforce A: BeautifulSoup (Quentin, Xianlin)
- - Taskforce B: Scrapy (Robbin)

- The fields we need to extract: place of publication, publisher, year, subject, language  
 
An example:
  | Attribute name | Attribute value |
  | -------------- | ---------------- |
  | Place of publication | London |
  | Publisher | Harper |
  | Year | 2013 |
  | Subject | 	Poirot, Hercule (Fictitious character) -- Fiction;Orient Express (Express train) -- Fiction;Private investigators -- England -- Fiction;Detective and mystery stories|
  | Language | English |
  
 ## Miscellaneous
 - Please append ```&locale=en``` to each URL so that the default language is English.
 - For quick debugging, you may set the crawler to crawl only 50 URLs.
 - For the "Subject" field, let's put mutiple values in one column with a semicolon ```;``` separating each value. 
  
