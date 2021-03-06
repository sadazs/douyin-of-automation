from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome(executable_path='/Users/tangyong/Application/chromedriver')

#  新开一个窗口，通过执行js来新开一个窗口
# js='window.open("https://www.youtube.com/");'
# browser.execute_script(js)
browser.get('https://www.youtube.com/')
# input = browser.find_element_by_id('search-input')
# input.click()
browser.find_element_by_xpath('//input').send_keys('data is beautiful')
search = browser.find_element_by_id('search-icon-legacy')
search.click()
main_link = browser.find_element_by_id('main-link')
main_link.click()
time.sleep(5)
# video = browser.find_element_by_xpath('//div[contains(text(),"视频")]')
video = browser.find_elements_by_class_name('paper-tab')[1]
# print('video:', video)
video.click()
time.sleep(10)
# order = browser.find_element_by_xpath('//div[text()="排序方式"]')
# order = browser.find_element_by_link_text('排序方式')
# order = browser.find_elements_by_class_name('yt-sort-filter-sub-menu-renderer')[0]
# print('order:', order)
# print(len(browser.find_elements_by_link_text('//div[text()="排序方式"]')))
# order.click()
# hot = browser.find_element_by_xpath('//div[text()="最热门"]')
# hot.click()
# target = browser.find_element_by_class_name('ytd-thumbnail')
total_num_element = len(browser.find_elements_by_id('thumbnail'))
url_list = []
for index in range(total_num_element):
    target = browser.find_elements_by_id('thumbnail')[index]
    target_url = target.get_attribute("href")
    if target_url != None:
      url_list.append(target_url)

total_num_video = len(url_list)

print('已经爬到的视频个数:', total_num_video)
print('链接地址如下:', url_list)

num = 1
while num < total_num_video:
  try:
      browser.get('https://en.savefrom.net/18/')
      WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH,"//input"))
      )
      time.sleep(1)
      browser.find_element_by_xpath('//input').send_keys(url_list[num])
      video_compile = browser.find_element_by_xpath('//button[contains(text(),"Download")]')
      video_compile.click()
      WebDriverWait(browser, 300).until(
        EC.presence_of_element_located((By.CLASS_NAME,"def-btn-box"))
      )
      time.sleep(1)
      download = browser.find_element_by_class_name('def-btn-box')
      download.click()
      #   关闭广告页面
      handles = browser.window_handles
      if len(handles) > 1:
        browser.switch_to.window(handles[1])
        browser.close()
        browser.switch_to.window(handles[0])
      browser.get('https://en.savefrom.net/18/')
      print('当前视频下载进度:', num, '/', total_num_video)
      num = num + 1
  except ZeroDivisionError as e:
      print('error:', e)
  finally:
      print('搞定一个！')