from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# open mongo-express.
driver.get("http://localhost:8080/")
folder= driver.find_element("xpath", "//tbody//tr//td//h3//a[normalize-space()='user-account']")
folder.click()

# press on user-account database.
driver.get("http://localhost:8080/db/user-account/")
folder1= driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[5]/h3[1]/a[1]")
folder1.click()

# press on users collection.
driver.get("http://localhost:8080/db/user-account/users")
folder2= driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[2]/div[1]/div[4]/table[1]/tbody[1]/tr[1]/td[3]/div[1]")
folder2.click()

# open a new tab.
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
  
# open my web-app and press edit Button.
driver.get("http://localhost:3000/")
folder3 = driver.find_element("xpath", "/html[1]/body[1]/div[1]/button[1]")
folder3.click()

# add Gaming to the interests.
folder4 = driver.find_element("xpath", "/html[1]/body[1]/div[2]/input[3]")
folder4.send_keys(", Gaming.")

# click on Update Button.
folder5= driver.find_element("xpath", "/html[1]/body[1]/div[2]/button[1]")
folder5.click()
