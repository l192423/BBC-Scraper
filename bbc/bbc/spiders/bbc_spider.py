# -*- coding: utf-8 -*-
import scrapy
from ..items import BbcItem


class BbcSpiderSpider(scrapy.Spider):
    name = 'bbc_spider'
    #allowed_domains = ['https://www.bbc.com/news/world/middle_east']
    start_urls = [
        'https://www.bbc.com/news/world-middle-east-53601710'
        ]

    def parse(self, response):
        items = BbcItem()
        #divs = response.css('.gs-u-box-size')
        
        #link = 'https://www.bbc.com' + divs.css('.gs-c-promo-body a::attr(href)')[6].extract() 

        description = response.css('.story-body__inner p::text').extract()
        htmlDescription = response.css('.story-body__inner p').extract()
        topics = response.css('.tags-container a::text').extract() 
        createdPublishDate = response.css('.date--v2::text').extract_first()   

        title = response.css('.story-body__h1::text').extract()
        url = response.css('.image-and-copyright-container img::attr(src)').extract_first()   
        alt = response.css('.image-and-copyright-container img::attr(alt)').extract_first()  
        caption = response.css('.media-caption__text::text').extract_first() 
        titleImage = {'url':url, 'alt': alt, 'caption': caption}
        leadtext = response.css('.story-body__introduction::text').extract_first() 
        author = response.xpath('//*[@id="responsive-news"]/head/meta[30]').extract()
        author = author[0][-10:-2]

        items['title'] = title
        items['titleImage'] = titleImage
        items['author'] = author
        items['createdPublishDate'] = createdPublishDate
        items['leadtext'] = leadtext
        items['description'] = description
        items['htmlDescription'] = htmlDescription
        #images = scrapy.Field()
        items['topics'] = topics

        yield items