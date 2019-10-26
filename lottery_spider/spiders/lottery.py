# -*- coding: utf-8 -*-
import scrapy
from lottery_spider.items import LotterySpiderItem

class LotterySpider(scrapy.Spider):
    name = 'lottery'
    allowed_domains = ['gov.cn']        #允许爬虫爬取目标网站的域名，此域名之外的不会爬取；
    start_urls = ['http://www.lottery.gov.cn/historykj/history_1.jspx?_ltype=dlt']  #起始页；从合格web开始爬取；

    def parse(self, response):
        #使用xpath获取数据前的路径，返回一个list的格式数据；
        results = response.xpath("//div[@class='yylMain']//div[@class='result']//tbody//tr")
        for result in results:  #results数据需要for循环遍历；
            qihao = result.xpath(".//td[1]//text()").get()
            bule_ball_1 = result.xpath(".//td[2]//text()").get()
            bule_ball_2 = result.xpath(".//td[3]//text()").get()
            bule_ball_3 = result.xpath(".//td[4]//text()").get()
            bule_ball_4 = result.xpath(".//td[5]//text()").get()
            bule_ball_5 = result.xpath(".//td[6]//text()").get()
            red_ball_1 = result.xpath(".//td[7]//text()").get()
            red_ball_2 = result.xpath(".//td[8]//text()").get()

            bule_ball_list = []     #定义一个列表，用于存储五个蓝球
            bule_ball_list.append(bule_ball_1)
            bule_ball_list.append(bule_ball_2)
            bule_ball_list.append(bule_ball_3)
            bule_ball_list.append(bule_ball_4)
            bule_ball_list.append(bule_ball_5)

            red_ball_list = []      #定义一个列表，用于存储2个红球
            red_ball_list.append(red_ball_1)
            red_ball_list.append(red_ball_2)

            print("===================================================")
            print("❤期号："+ str(qihao) + " ❤" + "蓝球："+ str(bule_ball_list) + " ❤" + "红球" + str(red_ball_list))

            item = LotterySpiderItem(qihao = qihao,bule_ball = bule_ball_list,red_ball = red_ball_list)
            yield item

        next_url = response.xpath("//div[@class='page']/div/a[3]/@href").get()
        if not next_url:
            return
        else:
            last_url = "http://www.lottery.gov.cn/historykj/" + next_url
            yield scrapy.Request(last_url,callback=self.parse)  #这里调用parse方法的时候不用加();