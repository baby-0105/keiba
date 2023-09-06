from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
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

    def get_horse_info_of_main_race(self):
        self.driver.find_element(By.LINK_TEXT, "特別登録").click()
        horse_list = self.driver.find_elements(By.CLASS_NAME, "HorseList")
        ele_len = len(horse_list)

        for i in range(ele_len):
            horse_info =horse_list[i].text
            print(horse_info)

if __name__ == "__main__":
    net_keiba = NetKeibaScraping()
    net_keiba.get_horse_info_of_main_race()
    net_keiba.driver.quit()
