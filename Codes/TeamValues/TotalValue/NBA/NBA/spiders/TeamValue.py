import scrapy

class PlayersalarySpider(scrapy.Spider):
    name = 'TeamValue'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.forbes.com/teams/']
        teams = ['new-york-knicks', 'los-angeles-lakers', 'golden-state-warriors', 'chicago-bulls', 'boston-celtics', 'brooklyn-nets', 'houston-rockets', 'los-angeles-clippers',
                  'dallas-mavericks', 'miami-heat', 'san-antonio-spurs', 'toronto-raptors', 'sacramento-kings', 'washington-wizards', 'cleveland-cavaliers', 'portland-trail-blazers',
                  'phoenix-suns', 'oklahoma-city-thunder', 'orlando-magic', 'utah-jazz', 'philadelphia-76ers', 'indiana-pacers', 'atlanta-hawks', 'denver-nuggets',
                  'detroit-pistons', 'milwaukee-bucks', 'minnesota-timberwolves', 'charlotte-hornets', 'memphis-grizzlies', 'new-orleans-pelicans'
                 ]

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
