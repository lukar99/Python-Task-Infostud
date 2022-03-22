import scrapy

class InfoStudSpider(scrapy.Spider):
    name = 'infostud'
    page_number = 2
    start_urls = ['https://poslovi.infostud.com/oglasi-za-posao']

    def parse(self, response):
        for ad in response.css('div.uk-card.uk-card-small.uk-card-default.uk-card-body.uk-margin-bottom'):
            try:
                yield {
                    'job_title': ad.css('h2.uk-h3.uk-margin-remove-bottom.uk-text-break::attr(title)').get(),
                    'employer': ad.css('p.uk-h4.uk-margin-remove::text').get().strip(),
                    'job_address': ad.css('p.uk-margin-remove-bottom::text').extract()[1].strip(),
                    'job_details': ad.css('p.job__desc::text').get().strip(),
                    'end_date': ad.css('p.uk-margin-remove.uk-text-bold::text').extract()[1].strip()
                }
            except:
                yield {
                    'job_title': ad.css('h2.uk-h3.uk-margin-remove-bottom.uk-text-break::attr(title)').get(),
                    'employer': ad.css('p.uk-h4.uk-margin-remove::text').get().strip(),
                    'job_address': ad.css('p.uk-margin-remove-bottom::text').extract()[1].strip(),
                    'job_details': '',
                    'end_date': ad.css('p.uk-margin-remove.uk-text-bold::text').extract()[1].strip()
                }

            
        
        next_page = 'https://poslovi.infostud.com/oglasi-za-posao?page=' + str(InfoStudSpider.page_number)
        if InfoStudSpider.page_number <= 50:
            InfoStudSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
    
     