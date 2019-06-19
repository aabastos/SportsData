import scrapy

class PlayersalarySpider(scrapy.Spider):
    name = 'TeamValue'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.forbes.com/teams/']
        teams = ['arizona-cardinals', 'atlanta-falcons', 'baltimore-ravens', 'buffalo-bills', 'carolina-panthers', 'chicago-bears', 'cincinnati-bengals', 'cleveland-browns',
                 'dallas-cowboys', 'denver-broncos',  'detroit-lions',  'green-bay-packers',  'houston-texans',  'indianapolis-colts',  'jacksonville-jaguars',  'kansas-city-chiefs',
                 'los-angeles-chargers', 'los-angeles-rams',  'miami-dolphins',  'minnesota-vikings',  'new-england-patriots',  'new-orleans-saints',  'new-york-giants',  'new-york-jets',
                 'oakland-raiders',  'philadelphia-eagles',  'pittsburgh-steelers', 'san-francisco-49ers',  'seattle-seahawks',  'tampa-bay-buccaneers',  'tennessee-titans', 'washington-redskins'
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
