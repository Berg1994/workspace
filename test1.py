# from fake_useragent import UserAgent
# import requests
#---
# from lxml import etree
#
# url = 'https://www.brookings.edu/blog/africa-in-focus/2018/07/03/capitalizing-on-industry-4-0-in-africa/'
# # //div[@class="content-column"]//p//text()
#
# useragent = UserAgent()
#
# headers = {
#     'User-Agent': useragent.random
# }
#
# res = requests.get(url=url, headers=headers)
# html_content = etree.HTML(res.text)
# content = html_content.xpath('//div[@class="post-body post-body-enhanced"]//p//text()')
# for i in content:
#     i.encode('utf8')
#     print(i)
# print(len(content)

# import pandas as pd
# url = 'https://www.brookings.edu/experts/henry-j-aaron/'
# data = pd.read_html(url)[0]
# print(data)