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
# import hashlib
# #
# # str1 = '1234567890'
# # str2 = hashlib.sha1(str1.encode('utf8'))
# # str3 = hashlib.md5(str1.encode('utf8'))
# # print(str2.hexdigest(),str2.hexdigest())
# # print(len(str2.hexdigest()))
# # print(len(str3.hexdigest()))
# # print(type(str2))
# # print(type(str3))
# str1 = 'https://www.chathamhouse.org/research/topics/drugs-and-organized-crime?page=0'
# str2 = 'https://www.chathamhouse.org/research/topics/drugs-and-organized-crime?page=1'
# str3 = str1.split('=')[-1]
# # print(str3)
# str4 = str2[:-1] + str3
# print(str4)
# list1 = [1, 2, 3]
# list2 = [2, 3, 4]
# list3 = [3, 4, 5]
# list4 = []
# for a, b, c in list1, list2, list3:
#     list4.append(a)
#     list4.append(b)
#     list4.append(c)
# print(list4)
import re

# str1 = '/research/topics/european-union?page=16%2C0%2C0%2C15#fragment-3'
# print(str1.split('=')[-1].split('#')[0])
# print(str1.split('=')[-1].split('#')[0])
# res = re.findall(r'(\?page=.*C)',str1)[0]
# resl = re.findall(r'C(\d*?)#',str1)[0]
# print(res)
# print(resl)
'https://f1.media.brightcove.com/7/2848955551001/2848955551001_5838116276001_5838028051001.mp4?pubId=2848955551001&videoId=5838028051001'

'https://f1.media.brightcove.com/7/2848955551001/2848955551001_5838038336001_5838028051001.mp4?pubId=2848955551001&videoId=5838028051001'
'https://f1.media.brightcove.com/7/2848955551001/2848955551001_5838039042001_5838035577001.mp4?pubId=2848955551001&videoId=5838035577001'
'https://f1.media.brightcove.com/7/2848955551001/2848955551001_5838038423001_5838035577001.mp4?pubId=2848955551001&videoId=5838035577001'
'https://f1.media.brightcove.com/7/2848955551001/2848955551001_5851839821001_5850886043001.mp4?pubId=2848955551001&videoId=5850886043001'
str0 = 'https://brightcove.hs.llnwd.net/v1/unsecured/media/2848955551001/201811/1154/2848955551001_5859825770001_5858320218001-vs.jpg?pubId=2848955551001&videoId=5858320218001'
str1 = 'background-image: url("https://f1.media.brightcove.com/7/2848955551001/2848955551001_5838073418001_5838035577001-vs.jpg?pubId=2848955551001&videoId=5838035577001"); background-size: 100%; background-position: 0px 0px;'
str2 = str0.replace('jpg','mp4')
print(str2)