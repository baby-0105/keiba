from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class NetKeibaScraping():
    driver = None

    def __init__(self):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = Chrome(options=options)
        self.driver.get("https://www.netkeiba.com/")

    def get_title(self):
        title = self.driver.title
        print(title)

if __name__ == "__main__":
    net_keiba_scraping = NetKeibaScraping()
    net_keiba_scraping.get_title()
    net_keiba_scraping.driver.quit()
