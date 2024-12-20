from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie_button = driver.find_element(By.ID, value = "cookie")

#Get upgrade items ids.
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
items_ids = [item.get_attribute("id") for item in items]

# Get all upgrade <b> tags
all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
item_prices = []

for price in all_prices:
     # cost = price.text.split("-")[1].strip().replace(",","")
     if price.text != "":
         cost = price.text.split("-")[1].strip().replace(",","")
         item_prices.append(cost)

#                   create dictionary
cookie_upgrades = {}
for i in range(len(item_prices)):
    cookie_upgrades[items_ids[i]] = int(item_prices[i])

#print(cookie_upgrades)

timeout = time.time() + 5
end_session = time.time() + 20*60


while True:
    cookie_button.click()
    if time.time() > timeout:

        #Get current cookie count
        my_score = driver.find_element(by=By.ID, value="money").text
        if "," in my_score:
            my_score = my_score.replace(",","")
        my_score = int(my_score)

        #Get list of affordable upgrades
        affordable_upgrades = {}
        for product,value in cookie_upgrades.items():
            if value <= my_score:
                affordable_upgrades[product] = value

        #Get most expensive affordable upgrade
        most_expensive_upgrade = max(affordable_upgrades)

        print(f"my_score: {my_score} affordable_upgrades: {affordable_upgrades}")
        print(most_expensive_upgrade)

        driver.find_element(By.ID, value=most_expensive_upgrade).click()


        # print(affordable_upgrades)
        timeout = time.time()+5

    if time.time() > end_session:
        cookies_second = driver.find_element(By.ID, value="cps")
        print(cookies_second.text)
        break





