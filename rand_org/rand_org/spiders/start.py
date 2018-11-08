from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'rand', '-s', 'FEED_EXPORT_ENCODING=UTF-8'])
