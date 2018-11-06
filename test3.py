import hashlib
import re
#
# list1 = ["For the past seven years, our scholars and other Africa experts have ", "contributed their thoughts", " on the top priorities for Africa for the upcoming year.  Again, this year, the Brookings Africa Growth Initiative team would like to open the floor and hear from you: Specifically, what do you think should be the top priority for Africa in 2018?", "To take the poll, click the image below:", "If we didn’t capture your priority, we invite you to tell us what it is in our comments section or tweet to @BrookingsGlobal using #ForesightAfrica.", "The results will be revealed at the Foresight Africa event on January 17. We invite you to attend or tune into the webcast. ", "You can register for the event here.", "\n", "\n\t\t\t", "\n\t\t\t", "Related Content", "\n\t\t", "\n\t\t", "\n\t\t", "\n\t", "\n\t\t", "\n\t\t\t", "\n\t\t\t\t", "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", "\n\t\t", "\n\t", "\n\t", "\n\t\t\n\t\t\t\t\t", "Africa in focus", "\n\t\t\t\t", "Foresight Africa: Join the conversation on the top priorities for Africa in 2018", "\n\t\t", "\n\t\t\t\t\t\t\t", "Brahima Sangafowa Coulibaly", "\n\t\t\t\t\t\t\t\t\t\t\t\t\t", "Thursday, January 11, 2018", "\n\t\t\t\t\t", "\n\n\t\t\n\t\t\t", "\n", "\n", "\n\t", "\n\t\t", "\n\t\t\t", "\n\t\t\t\t", "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", "\n\t\t", "\n\t", "\n\t", "\n\t\t\n\t\t\t\t\t", "Economic Development", "\n\t\t\t\t", "Foresight Africa: Top priorities for the continent in 2018", "\n\t\t", "\n\t\t\t\t\t\t\t\t\t\t\t\t\t", "Thursday, January 11, 2018", "\n\t\t\t\t\t", "\n\n\t\t\n\t\t\t", "\n", "\n\n", "\n\t\n\t", "\n\t\t\t\t\t", "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t", "2018", "\n\t\t\t\t\t\t\t\t\t\t", "Jan", "\n\t\t\t\t\t", "17", "\n\t\t\t\t\t\t\t", "\n\t\t\n\t\t", "\n\t\t\t\t\t\t\t", "Past Event", "\n\t\t\t\n\t\t\t", "Foresight Africa: Top priorities for Africa in 2018", "\n\n\t\t\t\t\t\t\t", "\n\t\t\t\t\t", "10:00 AM", " -\n\t\t\t\t\t", "\n\t\t\t\t\t\t11:30 AM EST\t\t\t\t\t", "\n\t\t\t\t", "\n\t\t\t\t\t\t\t\t\t", "\n\t\t\t\t\t\tWashington, DC\t\t\t\t\t", "\n\t\t\t\t\t\t\t\t\t", "\n\t", "\n\n\t\n\t", "\n\t", "\n\t", "\n", "\t"]
#
# list2 = ''.join(list1)
# list3 = re.sub(r'\n|\r|\t','',list2)
# # list3 = list2.split(r'[\n|\t|\r]')
#
# # print(list3)
#
# str1 = '"isn\'t," they said.'
# print(re.sub(r'\'','',str1))
#
# str2 = "AuthorsElaine KamarckFounding Director - Center for Effective Public ManagementSenior Fellow - Governance StudiesTwitterEKamarckAlexander R. PodkulPh.D. Candidate in Political Science - Georgetown UniversityTwitterapodkulWe also asked primary voters about various issues. There is, of course, a long-standing consensus on the importance of economic conditions to election results. But as others have commented, the controversial nature of the Trump presidency and the uneven rewards of the economic recovery have called into doubt how much a generally good economy will help Republicans this year. As Figure 17 indicates, the vast majority of Republican voters think the economy is good or excellent. Democrats divide between good and not so good. As Figure 18 shows, the voters also split on who should get the credit for the country’s economic situation. Republicans who think the economy is good say President Trump deserve credit; Democrats who think the economy is good say President Obama deserves credit.if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;We next asked primary voters about immigration. An overwhelming number of Democratic voters are in favor of offering illegal immigrants a chance to apply for legal status. But, as Figure 19 shows, a surprising majority of Republican primary voters—57 percent—also think immigrants should be offered a chance to apply for legal status. This represents a 10-point increase from the survey we conducted of 2016 congressional primary voters, and is especially surprising given that our Republican sample included four districts characterized as R+18 or greater. Given that getting tough on immigration has been a standard feature of Mr. Trump’s rhetoric and policy over the past two years, this comes as a surprise and is, perhaps, one more data point indicating that Mr. Trump’s takeover of the Republican Party is not as complete as some think. Further, these findings suggest that—like among partisan general election voters—Republican primary voters are not as consistently anti-immigration as Democratic primary voters are pro-immigration.1if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;While Mr. Trump may not be having the effect he intended on attitudes toward immigration, he is impacting attitudes on foreign policy and trade. While voters in both parties support the interests of U.S. allies by large margins, there is a significant portion of Republican voters who advocate having the U.S. “follow its own national interests.”if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;But of all the issues we tracked, the findings on trade are the most surprising. The two parties seem to have traded places during the Trump years. For many years, the Democratic Party was the party most suspicious of trade agreements and most fearful that they would take away American jobs. The labor movement worked hard against a series of trade agreements in the 1990s, including NAFTA and China’s Most Favored Nation.2 But, as Figure 21 shows, while primary voters in both parties say trade creates more U.S. jobs, this view is more popular among Democrats than Republicans by 10 percentage points. And the view that trade takes away jobs is more popular among Republicans than Democrats by 14 percentage points!if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;One explanation for this is the rapid deterioration in union membership in the United States. The rate of union membership in 2015 was about half the rate it was in 1983. Moreover, union membership today is about evenly split between the public sector and the private sector and public sector jobs are not threatened by trade agreements in the way private sector jobs were and are.3 This probably explains why, even among union members, there are slightly more voters who think trade creates more U.S. jobs than voters who think it takes away jobs, as Figure 22 illustrates. Nonetheless this portends a sea change in Democratic Party politics toward trade.if ( ! document.getElementById( 'simplechart-widget-js' ) ) {window.__simplechart_public_path__ = window.__simplechart_public_path__ ||\"https:\\/\\/www.brookings.edu\\/wp-content\\/plugins\\/wordpress-simplechart\\/js\\/app\\/\";}// We need d3 v3 for NVD3.  // We need D3 v4 for Annotations.window.d3v4 = d3;Continue to the next section, “Exploring California’s top-two primary.“"
# str3 = re.sub(r'\\','',str2)
# print(str3)

# str1 = 'Up Front'
#
# print(str1 == 'The Avenue' or 'Report')

# def Create_fingerprint(url):
#     hash_md5 = hashlib.md5(url.encode('utf'))
#     return hash_md5.hexdigest()
#
# print(Create_fingerprint('https://www.brookings.edu/blog/fixgov/2018/01/20/the-2018-shutdown-reopening-the-government-will-be-a-heavy-lift/'))
# print(Create_fingerprint('https://www.brookings.edu/blog/fixgov/2018/01/20/the-2018-shutdown-reopening-the-government-will-be-a-heavy-lift/'))
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.PhantomJS()
# browser.maximize_window()
# browser.set_window_size(1400,700)
url = 'https://www.brookings.edu/research/a-policy-at-peace-with-itself-antitrust-remedies-for-our-concentrated-uncompetitive-economy/'
browser.get(url)
wait = WebDriverWait(browser, 10)
element_images = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'nv-chart')))
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

for element_image in element_images:

    top = element_image.location['y']
    bottom = element_image.location['y'] + element_image.size['height']
    left = element_image.location['x']
    right = element_image.location['x'] + element_image.size['width']

    image = browser.get_screenshot_as_png()

    picture = Image.open(BytesIO(image))
    picture = picture.crop((left, top, right, bottom))
    picture.save('./' + element_image.id.split(':')[-1] + '.png')