
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options




options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=options,executable_path='chromedriver.exe')

web.get("https://osmphp.000webhostapp.com/views/login.php")

try:
    # create a field object
    email = WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/form/div[1]/input")))
    # click on it to enable the input field
    email.click()
    # insert the input using send_keys function
    email.send_keys("johndoe@gmail.com")
    
    # follow similar steps for password as well
    password = WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/form/div[2]/input")))
    password.click()
    password.send_keys("123123")

    # Select the button
    loginButton = WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/form/div[3]/button")))
    # click the button and wait
    loginButton.click()


    # select the name and print it
    data = WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/h5/i")))
    print(data.text)


    # select logout button
    logoutLink = WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/span/a")))
    logoutLink.click()
except:
    pass