import scrapy

from pictures.items import PicturesItem
class PicturesSpider(scrapy.Spider):
    name = "pictures"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.ctopgirl.com/pic/136.html",
        "http://www.ctopgirl.com/pic/141.html"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        """

        :param response:
        :return:
        ("/html/body/div[@class='container']/div[@class='bigimg']/p/img")

        xpath 解析的重要性
        """

        print(response.xpath('/html/body/div/div/p/img'))

        item = PicturesItem()
        for sel in response.xpath('/html/body/div/div/p/img'):
            item['title'] = "ypp"
            item['link'] = sel.re('//.*.jpg')[0]
            item['desc'] = "ypp-pics"
            print("\n<===========================")
            print (item['title'], item['link'], item['desc'])
            print("===========================>\n")

            yield item