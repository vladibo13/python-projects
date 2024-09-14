from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CSS_SELECTOR, value="form button")

fname.send_keys("fname")
lname.send_keys("lname")
email.send_keys("email@email.com")

button.click()



# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # print(article_count.text)
# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python", Keys.ENTER)

