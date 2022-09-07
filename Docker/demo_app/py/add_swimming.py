from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# open mongo-express and press on user-account database.
driver.get("http://localhost:8080/")
user_account= driver.find_element("xpath", "//tbody//tr//td//h3//a[normalize-space()='user-account']")
user_account.click()

# press on users collection.
driver.get("http://localhost:8080/db/user-account/")
users_collection= driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[5]/h3[1]/a[1]")
users_collection.click()

# press to see updates.
driver.get("http://localhost:8080/db/user-account/users")
updates= driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[2]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[3]/div[1]")
updates.click()

# open a new tab.
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
  
# open my web-app and press edit Button.
driver.get("http://localhost:3000/")
edit_button = driver.find_element("xpath", "/html[1]/body[1]/div[1]/button[1]")
edit_button.click()

# add Gaming to the interests.
swimming = driver.find_element("xpath", "/html[1]/body[1]/div[2]/input[3]")
swimming.send_keys(", Swimming.")

# click on Update Button.
update_button= driver.find_element("xpath", "/html[1]/body[1]/div[2]/button[1]")
update_button.click()
