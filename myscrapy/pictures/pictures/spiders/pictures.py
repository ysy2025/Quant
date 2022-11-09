import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from pictures.items import PicturesItem


class PicturesSpider(scrapy.Spider):
    name = "pictures"
    # allowed_domains = ["dmoz.org"]
    # start_urls = [
    #     "http://www.ctopgirl.com/pic/136.html",
    #     "http://www.ctopgirl.com/pic/141.html"
    # ]
    # 自定义构建start_urls
    def start_requests(self):
        names = ["闫盼盼", "杨晨晨"]

        for name in names:
            url = "http://www.ctopgirl.com/so/so.aspx?key={0}".format(name)
            yield Request(url=url)
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # def parse_get_urls(self, response:HtmlResponse):
    #     hrefs_selector = response.xpath("/html/body/div[@class='container']/ul/li/p")
    #
    #     for sel in hrefs_selector:
    #         temp = sel.re('href="(.*)"')[0]
    #         print(temp)
    #
    #         url = response.urljoin(temp)
    #         print(url)
    #
    #         yield Request(url = url)
        pass
    def parse(self, response:HtmlResponse, **kwargs):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        """

        :param response:
        :return:
        ("/html/body/div[@class='container']/div[@class='bigimg']/p/img")

        xpath 解析的重要性

        可以实例化一个selector
        sel = Selector(response)
        然后利用selecotr的方式解析
        """
        # sel = Selector(response)
        # items = sel.css("#body")
        #
        # print("\n<===========================")
        # print(items)
        # print("===========================>\n")

        print(response.xpath('/html/body/div/div/p/img'))
        selectors = response.xpath('/html/body/div/div/p/img')
        item = PicturesItem()
        for sel in selectors:
            item['title'] = "ypp"
            item['link'] = sel.re('//.*.jpg')[0]
            item['desc'] = "ypp-pics"
            print("\n<===========================")
            print (item['title'], item['link'], item['desc'])
            print("===========================>\n")
            yield item

        hrefs_selector = response.xpath("/html/body/div[@class='container']/div[@class='page']/ul/li/a")

        for sel in hrefs_selector:
            temp = sel.re('href="(.*)"')[0]
            print(temp)

            url = response.urljoin(temp)
            print(url)

            yield Request(url = url)