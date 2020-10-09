from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint


# signs in to instagram


chromedriver_path = 'chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('your_username') #replace with your username
password = webdriver.find_element_by_name('password')
password.send_keys('your_password') #replace with your password
sleep(3)

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications


# finds photos and likes


hashtag_list = ['gaintrain'] # here you can add/change hashtags format is 'HASHTAG' (put commas between each hashtag)

tag = -1

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    
    try:        
        for x in range(1,200):
            print('{}_{}'.format(hashtag, x))

            # Liking the picture
            button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                    
            button_like.click()
            sleep(randint(5,15))


            # Next picture
            webdriver.find_element_by_link_text('Next').click()
            sleep(randint(5,15))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue
