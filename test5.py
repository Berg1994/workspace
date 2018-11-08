# # str1 = 'https://www.rand.org/pubs/research_briefs/RB190.html'
# # str2 = str1.split('/')[3]
# # print(str2)
# import re
#
# str1 = """
# 联系
#
# 			电子邮件
#
# 				202.797.6414
#
# 			 -  Shannon Meraw
# 话题
# 收入不平等与社会流动
# 劳动政策与失业
# 美国经济
# 程式
# 经济研究
# 经验
# 过去的位置
# 联邦储备委员会研究和统计司助理主任（2014-2018）
# 联邦储备委员会宏观经济分析主任（2012-2014）
# 财政部宏观经济政策副助理部长（2011-2012）
# 耶鲁大学经济系访问学者（2010年）
# 教育
# 博士
# 经济学 - 哥伦比亚大学
# 历史上的AB  - 哥伦比亚大学"""
# str_items = ''.join(str1)
# print(str_items)
# str_content = re.sub(r'\r|\n|\t\xa0', '', str_items)
# print(str_content)
import hashlib

str1 = '1234567890'
str2 = hashlib.sha1(str1.encode('utf8'))
str3 = hashlib.md5(str1.encode('utf8'))
print(str2.hexdigest(),str2.hexdigest())
print(len(str2.hexdigest()))
print(len(str3.hexdigest()))
print(type(str2))
print(type(str3))