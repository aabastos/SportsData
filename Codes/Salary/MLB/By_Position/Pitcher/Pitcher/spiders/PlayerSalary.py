import scrapy


class PlayersalarySpider(scrapy.Spider):
    name = 'PlayerSalary'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.spotrac.com/mlb/rankings/']
        teams = ['arizona-diamondbacks', 'atlanta-braves', 'baltimore-orioles', 'boston-red-sox', 'chicago-cubs', 'chicago-white-sox', 'cincinnati-reds', 'cleveland-indians',
                 'colorado-rockies', 'detroit-tigers', 'houston-astros', 'kansas-city-royals', 'los-angeles-angels', 'los-angeles-dodgers', 'miami-marlins', 'milwaukee-brewers',
                 'minnesota-twins', 'new-york-mets', 'new-york-yankees', 'oakland-athletics', 'philadelphia-phillies', 'pittsburgh-pirates', 'san-diego-padres', 'san-francisco-giants',
                 'seattle-mariners', 'st.-louis-cardinals', 'tampa-bay-rays', 'texas-rangers', 'toronto-blue-jays', 'washington-nationals', 'florida-marlins', 'montreal-expos'
                 ]

        for i in range(2000, 2018):
            for j in range(12, 13):
                send = url[0] + str(i) + '/' + teams[j] + "/pitching"

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
