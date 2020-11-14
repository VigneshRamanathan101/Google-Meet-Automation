from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-popup")
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

import time as Time
from datetime import *

cache_file=open("Untitled-1.txt", "r")
contents = cache_file.read()
x=contents.split('\n')
Credintials=[]
for i in x[0:-1]:Credintials.append(i.split(':'))

def print_no_of_times(n=0, x=''):
    for i in range(n):
        print()
    if len(str(x)) > 0:
        print(x)


def start_meeting():
    try:
        
        print('finding now in classes')
        next_class = driver.find_element_by_class_name('Ql1xRb')
        next_class.click()
        print_no_of_times(1,'joining meeting')
        driver.implicitly_wait(20)
        driver.implicitly_wait(100)
        '''
        try:
            print_no_of_times(1,'trying to find dismiss')
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')
        except:
            print_no_of_times(2,"couldn't find dismiss")
            pass
        '''
        #audio button
        try:
            driver.find_element_by_class_name('ZB88ed').click()
            print('disble mic')
        except:
            print_no_of_times(2,"mic object can't be found")

        #video button
        try:
            if Credintials[2][1]=='Y':
                raise RuntimeError
            driver.find_element_by_class_name('GOH7Zb').click()
            print('disble video')
        except:
            print_no_of_times(2,"video object can't be found")

        Time.sleep(20.0)
        '''
        try:
            print_no_of_times(1,'trying to find dismiss')
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')
        except:
            print_no_of_times(2,"couldn't find dismiss")
            pass
        '''
        #join now button
        try:
            print_no_of_times(2,'join now try block')
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/span/span').click()
        except:
            print_no_of_times(2,'join now except block')
            try:
                driver.find_element_by_id('Join now')
            except:
                pass

        now = datetime.now().time()
        #now = now.strftime("%H:%M:%S")
        print_no_of_times(2,'time now is: ')
        print(now.strftime("%H:%M:%S"),' hours=',now.hour,' minute=',now.minute)

        #no_of participants
        no_of_participants=driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]')
        print(no_of_participants)
        
        end_meeting(now)
    
    except Exception as e:
        print(e)

def end_meeting(now):
    print_no_of_times(2,'entering time ending setion')
    while True:
        print_no_of_times(2,'class not ended...')
        end_time = datetime.now().time()
        #end_time = end_time.strftime("%H:%M:%S")
        #print('time now is: ',end_time.strftime("%H:%M:%S"))
        class_alive_time=((end_time.hour)*3600+(end_time.minute)*60+(end_time.second))-((now.hour)*3600+(now.minute)*60+now.second)
        #print(class_alive_time,': in seconds')
        print(float(Credintials[3][1])-(class_alive_time/60), ': time left')
        Time.sleep(10.0)
        if class_alive_time/60 > float(Credintials[3][1]):
            #driver.find_elements_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div/div[1]').click()
            print_no_of_times(2,'time to end the class')
            driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div').click()
            break

try:
    driver.get('https://apps.google.com/meet/')
    driver.maximize_window()
    driver.implicitly_wait(15)

    google_sign_in_button = driver.find_element_by_class_name('cta-wrapper')
    google_sign_in_button.click()

    email_box = driver.find_element_by_id('identifierId')
    email_box.send_keys(Credintials[0][1])
    print_no_of_times(2,'email_box filled')
    driver.implicitly_wait(500)

    
    try:
        print_no_of_times(2,'try block excuted')
        next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        next_button.click()
    except:
        print_no_of_times(2,'except->try block')
        driver.find_element_by_id("next").click()
        next_button.click()

    sign_url = driver.current_url

    password_box = driver.find_element_by_name('password')
    password_box.send_keys(Credintials[1][1])

    sign_in_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    sign_in_button.click()

    #need to work on sign-failed element

    if sign_url==driver.current_url:
        print('Please check your mail ID or Password')

        '''
        sign_failed_msg=driver.find_element_by_xpath
        ('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span')
        if type(sign_failed_msg)
        '''
    else:
        print_no_of_times(2,'Login Sucessful..')
        start_meeting()

    driver.quit()
    print_no_of_times(2,'Session ended Successfully...')

        

except RuntimeError:
    print('Have a happy day...')
    driver.quit()
    print_no_of_times(2,'Session ended Successfully...')
except Exception as e:
    print(e)
    print_no_of_times(2,'Session failed due to ...')
    print_no_of_times(1,str(e))
    driver.quit()
    print_no_of_times(2,'Session ended Successfully...')