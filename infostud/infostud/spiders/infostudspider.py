import scrapy

class InfoStudSpider(scrapy.Spider):
    name = 'infostud'
    start_urls = ['https://poslovi.infostud.com/oglasi-za-posao']

    def parse(self, response):
        for ad in response.css('div.uk-card.uk-card-small.uk-card-default.uk-card-body.uk-margin-bottom'):
            yield {
                'job_title': ad.css('h2.uk-h3.uk-margin-remove-bottom.uk-text-break::attr(title)').get(),
                'employer': ad.css('p.uk-h4.uk-margin-remove::text').get().strip(),
                'job_address': ad.css('p.uk-margin-remove-bottom::text').extract()[1].strip(),
                'job_details': ad.css('p.job__desc::text').get().strip(),
                'end_date': ad.css('p.uk-margin-remove.uk-text-bold::text').extract()[1].strip()
            }
    