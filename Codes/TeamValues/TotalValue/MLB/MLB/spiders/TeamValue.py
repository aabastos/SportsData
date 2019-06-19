import scrapy

class PlayersalarySpider(scrapy.Spider):
    name = 'TeamValue'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.forbes.com/teams/']
        teams = ['arizona-diamondbacks', 'atlanta-braves', 'baltimore-orioles', 'boston-red-sox', 'chicago-cubs', 'chicago-white-sox', 'cincinnati-reds', 'cleveland-indians',
                 'colorado-rockies', 'detroit-tigers', 'houston-astros', 'kansas-city-royals', 'los-angeles-angels-of-anaheim', 'los-angeles-dodgers', 'miami-marlins', 'milwaukee-brewers',
                 'minnesota-twins', 'new-york-mets', 'new-york-yankees', 'oakland-athletics', 'philadelphia-phillies', 'pittsburgh-pirates', 'san-diego-padres', 'san-francisco-giants',
                 'seattle-mariners', 'st-louis-cardinals', 'tampa-bay-rays', 'texas-rangers', 'toronto-blue-jays', 'washington-nationals'
                 ]

        for j in range(30):
            send = url[0] + teams[j]

            yield scrapy.Request(url = send, meta={'team' : teams[j]}, callback = self.parse)

    def parse(self, response):
        i = 0
        row = response.xpath('//*[@class="playerExp"]')
        yield{
            'name' : response.meta['team'],
            'value' : row.xpath('text()').extract()
        }
