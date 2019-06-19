import scrapy

class PlayersalarySpider(scrapy.Spider):
    name = 'PlayerSalary'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.spotrac.com/nfl/rankings/']
        teams = ['arizona-cardinals', 'atlanta-falcons', 'baltimore-ravens', 'buffalo-bills', 'carolina-panthers', 'chicago-bears', 'cincinnati-bengals', 'cleveland-browns',
                 'dallas-cowboys', 'denver-broncos',  'detroit-lions',  'green-bay-packers',  'houston-texans',  'indianapolis-colts',  'jacksonville-jaguars',  'kansas-city-chiefs',
                 'los-angeles-chargers', 'los-angeles-rams',  'miami-dolphins',  'minnesota-vikings',  'new-england-patriots',  'new-orleans-saints',  'new-york-giants',  'new-york-jets',
                 'oakland-raiders',  'philadelphia-eagles',  'pittsburgh-steelers', 'san-diego-chargers', 'san-francisco-49ers',  'seattle-seahawks',  'tampa-bay-buccaneers',  'tennessee-titans',
                 'washington-redskins', 'st.-louis-rams', 'houston-oilers'
                 ]

        for i in range(2000, 2018):
            for j in range(35):
                send = url[0] + str(i) + '/' + teams[j] + "/tight-end"

                yield scrapy.Request(url = send, meta={'team' : teams[j]}, callback = self.parse)

    def parse(self, response):
        i = 0
        for row in response.xpath('//*[@class="datatable noborder"]//tbody//tr'):
            year = str(row.xpath('//*[@class="team-header"]//h2//text()').extract())
            yield{
                'year' : year[2:6],
                'name' : row.xpath('td//h3//a//text()')[0].extract(),
                'salary' : row.xpath('//*[@class="info"]//text()')[i].extract(),
                'team' : response.meta['team']
            }

            i += 1
