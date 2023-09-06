from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
driver = Chrome(options=options)

driver.get("http://selenium.dev")

driver.quit()

class NetKeibaScraping():
    pass
