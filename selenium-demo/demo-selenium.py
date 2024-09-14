from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul time")
event_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")

event_tuple = list(zip(time_list, event_list))

events_dict = {}
i = 0
for time,event in event_tuple:
    i+1
    events_dict[i] = {time.text,event.text}

print(events_dict)
# for e in events_list:
#     print(e.text)
# events = {}
# for x in range(1,6):
#   events[x] = x

# driver.close()  


# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close()


test_eight_components()
