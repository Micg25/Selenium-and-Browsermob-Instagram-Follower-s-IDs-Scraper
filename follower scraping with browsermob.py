from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from browsermobproxy import Server
profile_link=" " #Put the link of the profile you want to scrape from
server = Server(" ") #Put the complete path where browsermob-proxy is in, usually: \Browsermob\bin\browsermob-proxy
server.start()
time.sleep(1)
proxy = server.create_proxy() #creating the proxy with browsermob
time.sleep(1)
#setting up firefox browser proxy with the browsermob proxy
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", str(proxy.proxy).split(':')[0])
profile.set_preference("network.proxy.http_port", int(str(proxy.proxy).split(':')[1]))
profile.set_preference("network.proxy.ssl", str(proxy.proxy).split(':')[0])
profile.set_preference("network.proxy.ssl_port", int(str(proxy.proxy).split(':')[1]))
profile.update_preferences()
options=webdriver.FirefoxOptions()
options.profile = profile
browser = webdriver.Firefox(options=options)

#setting the proxy in order to make it receive http/https traffic
proxy.new_har("LOG:", options={'captureHeaders': True, 'captureContent': True})

#logging on instagram by manually adding the cookies
browser.get("https://www.instagram.com/")
browser.delete_all_cookies()
browser.add_cookie({
    'name': 'csrftoken',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})

browser.add_cookie({
    'name': 'datr',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ds_user_id',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ig_did',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'mid',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ps_l',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'ps_n',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'rur',
    'value': '" "', #add value here
    'domain': '.instagram.com',
    'path': '/', 
    'expires': 'Session',
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'sessionid',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'shbid',
    'value': '" "', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'shbts',
    'value': '" "', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': True,
    'secure': True,
    
})
browser.add_cookie({
    'name': 'wd',
    'value': '', #add value here
    'domain': '.instagram.com',
    'path': '/',
    'expires': '', #add value here
    'httponly': False,
    'secure': True,
    
})
time.sleep(2)
#getting to the profile
browser.get(profile_link)
time.sleep(2)
#finding the "follower" element in order to click on it
elem=browser.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd']")
time.sleep(1)
elem.click()
time.sleep(3)
follower_scroll=browser.find_element(By.XPATH,"//div[@class='x7r02ix xf1ldfh x131esax xdajt7p xxfnqb6 xb88tzc xw2csxc x1odjw0f x5fp0pe']")   
chunk=1
while True:
    if(chunk==5):
        break
          
    usernames = browser.find_elements(By.XPATH,"//span[starts-with(@class, '_ap3a')]")   
    if(chunk!=1 and pivot[len(pivot)-1].text==usernames[len(usernames)-1].text):   #if the last element of the usernames fetched is the same as 
        break                                                                      #the last element of the previous usernames fetched (pivot)
                                                                                   #there are no more followers left to fetch
        
    print("\n Taking chunk number ",chunk) 
    chunk+=1
    #scrolling through the follower's list
    try: 
        pivot = browser.find_elements(By.XPATH,"//span[starts-with(@class, '_ap3a')]")
        browser.execute_script('arguments[0].scrollIntoView({block: "center", behavior: "smooth"});', usernames[len(usernames)-1])
    except:
        pass
    time.sleep(3)

result = proxy.har

user_ids_values = []

# Searching ids in the log results catched with browsermob
for entry in proxy.har['log']['entries']:
    # Checking if the request has a body (postData)
    if 'postData' in entry['request']:
        postData = entry['request']['postData']
        # Checking if the body has parameters
        if 'params' in postData:
            # Extracting parameters from the body
            postData_params = postData['params']
            # Checking and extracting user_id values 
            for param in postData_params:
                if param['name'] == 'user_ids':
                    user_ids_values.append(param['value'])
ids=[]
for elem in user_ids_values:
    ids.extend(elem.split(','))

ids_set=set(ids)

#saving the id set in a .txt file
with open("followers.txt","w") as file:
    for id in ids_set:
        file.write(str(id)+"\n")
#saving all browsermob logs in a .har file
with open("risultati.har","w",encoding="utf-8") as file:
    file.write(str(result))







