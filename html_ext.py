from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.headless = False  # True

driver = webdriver.Chrome(
    "/home/sagnik/Projects/gearScraperE7/chromedriver", options=opts)
# max size of list
listLen = 215
# link to go to
link_to_go_first = "https://epic7.smilegatemegaport.com/guide/wearingStatus?ptype=eqh&world=world_kor&lang=en&hero=c1100&equip="
# init xpath
xpath_start = "/html/body/div[1]/div/aside/ul/li["
path = xpath_start+str(1)+']'
small_xpath = '//*[@id="li_leftList"]/li['
initial_setup = "<html><head></head><body><div><ul>"
# retrieve the page from first position
driver.get(link_to_go_first)
print(initial_setup)
# loop to iterate over the herolist
for f in range(1, 4):  # put listlen later
    #click on the hero on the left side one by one
    select_hero = driver.find_element_by_xpath(small_xpath+str(f)+']')
    select_hero.click()
    delay = 5
    #select the equipment details
    stats = driver.find_element_by_id("li_rankList")
    print("Current hero data:")
    #click on the equipment details
    stats.click()
    #scroll down 30 key strokes
    for i in range(0, 30):
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        delay = 1
    stats_after = driver.find_element_by_xpath(small_xpath+str(f)+']')
    stats_after = stats
    #print the stats
    print(stats.get_attribute('innerHTML'))

    #go back to the hero list and scroll down with 3 keystrokes
    delay = 10
    #select_hero = driver.find_element_by_xpath(small_xpath)
    select_hero.click()
    for i in range(0, 3):
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        delay = 1

print("</ul></body></html>")
driver.quit()
