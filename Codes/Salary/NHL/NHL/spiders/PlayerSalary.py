import scrapy

class PlayersalarySpider(scrapy.Spider):
    name = 'PlayerSalary'
    REDIRECT_MAX = 50

    def start_requests(self):
        url = ['https://www.spotrac.com/nhl/rankings/']
        teams = ['anaheim-ducks', 'arizona-coyotes', 'boston-bruins', 'buffalo-sabres', 'calgary-flames', 'carolina-hurricanes', 'chicago-blackhawks', 'colorado-avalanche',
                'columbus-blue-jackets', 'dallas-stars', 'detroit-red-wings', 'edmonton-oilers', 'florida-panthers', 'los-angeles-kings', 'minnesota-wild', 'montreal-canadiens',
                'nashville-predators', 'new-jersey-devils', 'new-york-islanders', 'new-york-rangers', 'ottawa-senators', 'philadelphia-flyers', 'pittsburgh-penguins', 'san-jose-sharks',
                'st-louis-blues', 'tampa-bay-lightning', 'toronto-maple-leafs', 'vancouver-canucks', 'vegas-golden-knights', 'washington-capitals', 'winnipeg-jets', 'atlanta-thrashers',
                'phoenix-coyotes']

        for i in range(2000, 2018):
            for j in range(33):
                send = url[0] + str(i) + '/' + teams[j]

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
