import scrapy

class PlayersalarySpider(scrapy.Spider):
    name = 'TeamValue'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.forbes.com/teams/']
        teams = ['anaheim-ducks', 'arizona-coyotes', 'boston-bruins', 'buffalo-sabres', 'calgary-flames', 'carolina-hurricanes', 'chicago-blackhawks', 'colorado-avalanche',
                'columbus-blue-jackets', 'dallas-stars', 'detroit-red-wings', 'edmonton-oilers', 'florida-panthers', 'los-angeles-kings', 'minnesota-wild', 'montreal-canadiens',
                'nashville-predators', 'new-jersey-devils', 'new-york-islanders', 'new-york-rangers', 'ottawa-senators', 'philadelphia-flyers', 'pittsburgh-penguins', 'san-jose-sharks',
                'st-louis-blues', 'tampa-bay-lightning', 'toronto-maple-leafs', 'vancouver-canucks', 'vegas-golden-knights', 'washington-capitals', 'winnipeg-jets', 'phoenix-coyotes']

        for j in range(32):
            send = url[0] + teams[j]

            yield scrapy.Request(url = send, meta={'team' : teams[j]}, callback = self.parse)

    def parse(self, response):
        i = 0
        row = response.xpath('//*[@class="playerExp"]')
        yield{
            'name' : response.meta['team'],
            'value' : row.xpath('text()').extract()
        }
