from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# options = Options()
# options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome("C:/Users/AbOd/Downloads/chromedriver.exe")
# open mongo-express and press on user-account database.
driver.get("https://www.booking.com")
#driver.fullscreen_window()


# -----------------VARIABLES---------------------#
city = input("Enter destenation city : ")
check_in_date = input('check-in date: write in this format year-month-day (2022-10-07) \n check-in date: ')
check_out_date = input('check-out date: write in this format year-month-day (2022-10-08) \n check-out date: ')
adults_count = int(input("Adults Count: "))
child_ages = []
children_count = int(input('Children Count:  '))

for i in range(1, children_count+1):
    child_ages_input= int(input(f'Enter the age of {i} child '))
    child_ages.append(child_ages_input)

rooms_count = int(input("Rooms Count: "))

# -----------------END---------------------------#

print (child_ages)
currency_select=driver.find_element(By.CSS_SELECTOR, "button[data-tooltip-position='bottom']")
currency_select.click()
driver.implicitly_wait(30)

currency_select_usd=driver.find_element(By.CSS_SELECTOR, "a[data-modal-header-async-url-param='changed_currency=1&selected_currency=USD&top_currency=1']")
currency_select_usd.click()

where_to_go = driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
where_to_go.send_keys(f"{city}")

first_result = driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/span[2]")
first_result.click()

check_in = driver.find_element(By.CSS_SELECTOR, f"td[data-date='{check_in_date}']")
check_in.click()

check_out = driver.find_element(By.CSS_SELECTOR, f"td[data-date='{check_out_date}']")
check_out.click()

guests__count = driver.find_element(By.CLASS_NAME, "xp__guests__count")
guests__count.click()

adult_minus = driver.find_element(By.CSS_SELECTOR, "button[data-bui-ref='input-stepper-subtract-button']")
adult_plus = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]")

if adults_count == 1:
    adult_minus.click()
else:
    for _ in range(2,adults_count):
        adult_plus.click()


children_plus = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/button[2]/span[1]")
for count, element in enumerate (child_ages):
    children_plus.click()
    driver.implicitly_wait(15)
    child_age_push = driver.find_element(By.XPATH, f"/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[3]/select[{count+1}]")
    child_age_push.click()
    driver.implicitly_wait(15)
    for i in range (0, element+1):
        child_age_push.send_keys(Keys.ARROW_DOWN)
    child_age_push.send_keys(Keys.ENTER)


room_plus = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/button[2]/span[1]")
for _ in range(1, rooms_count):
    room_plus.click()
 


# # open a new tab.
# driver.execute_script("window.open('about:blank', 'secondtab');")
# driver.switch_to.window("secondtab")
  
