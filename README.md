# Selenium-and-Browsermob-Instagram-Follower-s-IDs-Scraper
Follower's IDs scraper made with the use of Selenium and Browsermob-proxy
This code will scrape follower's IDs of an instagram profile by using Selenium and Browsermob-proxy, selenium is used to scroll on an instagram profile follower's page, while the browser scroll down, our machine will get https responses where inside there are all profiles datas, such as ids. 
This http/https traffic is caputred by the browsermob-proxy, saved in an .har and then processed in order to scrape all of the ids that have been fetched by api calls.

in order to make the code work you have to manually add the values of your own cookies, you can easily take them by logging in instagram using your own browser and then opening the inspector element; once you opened it you have to go in the memory window and look for "cookie", once there you will see all of the cookies that instagram use to log you in. In my code you are gonna find the set of cookies you have to add but you'll have to modify the values of them with your own valid cookies values. By the way in the code you are gonna find comments where I tell you where you have to add some values. Once you properly loaded your cookies (wich they have a long expire date so don't worry about updating them frequently), you will have to change the "Profile_link" variable with the link of the profile you want to scrape from, you will even have to put the correct path of browsermob-proxy in order to make it works.

Packages needed: pip install selenium, pip install browsermob-proxy

PS. Make sure to put your driver.exe in the same path of the code, or else to specify the path of the driver, or the selenium webdriver is not gonna work.
