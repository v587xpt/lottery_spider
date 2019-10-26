from scrapy import cmdline

cmdline.execute("scrapy crawl lottery".split())
#等价于 ↓
# cmdline.execute(["scrapy","crawl","xiaoshuo"])