# #
# # str = 'https://www.brookings.edu/experts/page/2/'
# #
# # print(str.split('/')[-2])
#
# from io import BytesIO
#
import base64
import os
from io import BytesIO, StringIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.PhantomJS()
# # browser.maximize_window()
# browser.set_window_size(1400,700)
# url = 'https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&tn=SE_Pclogo_6ysd4c7a&sa=ire_dl_gh_logo&rsv_dl=igh_logo_pc'
# browser.get(url)
# wait = WebDriverWait(browser, 10)
# element_image = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'index-logo-src')))
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#
#
#
# top = element_image.location['y']
# bottom = element_image.location['y'] + element_image.size['height']
# left = element_image.location['x']
# right = element_image.location['x'] + element_image.size['width']
#
# image = browser.get_screenshot_as_png()
#
# picture = Image.open(BytesIO(image))
# picture = picture.crop((top, bottom, left, right))
# picture.save('./2.png')

from selenium import webdriver
from PIL import Image

broswer = webdriver.PhantomJS()
broswer.maximize_window()
broswer.get(
    "https://www.brookings.edu/research/a-policy-at-peace-with-itself-antitrust-remedies-for-our-concentrated-uncompetitive-economy/")
wait = WebDriverWait(broswer, 10)
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'nvd3-svg')))
broswer.save_screenshot(r'./photo.png')
svg_image = broswer.find_elements_by_css_selector('.nv-chart > .nvd3-svg')
for image in svg_image:
    left = image.location['x']
    top = image.location['y']
    elementWidth = image.location['x'] + image.size['width']
    elementHeight = image.location['y'] + image.size['height']
    picture = Image.open(r'./photo.png')
    picture = picture.crop((left, top, elementWidth, elementHeight))
    picture.save('./' + image.id.split(':')[-1] + '.png')

# os.remove('./photo2.png')