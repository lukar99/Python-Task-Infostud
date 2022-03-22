import scrapy


class InfostudItem(scrapy.Item):

    job_title = scrapy.Field()
    employer = scrapy.Field()
    job_address = scrapy.Field()
    job_details = scrapy.Field()
    end_date = scrapy.Field()
