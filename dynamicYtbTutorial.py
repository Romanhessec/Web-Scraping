from selenium import webdriver
import pandas as pd

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()
driver.get(url)

agreeButton = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
agreeButton.click()

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

video_list = []

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    
    vid_item = {
            'title': title,
            'views': views,
            'whenPosted': when
    }
    
    video_list.append(vid_item)

df = pd.DataFrame(video_list)
print(df)

