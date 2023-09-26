import datetime

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
        today = datetime.date.today()

        # 今日が土日なら
        if today.weekday() in [5, 6]:
            self.driver.find_element(By.LINK_TEXT, "出馬表")
        else:
            self.driver.find_element(By.LINK_TEXT, "特別登録").click()

        self.driver.find_element(By.LINK_TEXT, "馬柱(5走)").click()

        # 父
        horse1 = self.driver.find_elements(By.CLASS_NAME, "Horse01")
        for h1 in horse1:
            print(h1.text)

        # 馬名
        horse2 = self.driver.find_elements(By.CLASS_NAME, "Horse02")
        for h2 in horse2:
            print(h2.text)

        # 母
        horse3 = self.driver.find_elements(By.CLASS_NAME, "Horse03")
        for h3 in horse3:
            print(h3.text)

        # 母父
        horse4 = self.driver.find_elements(By.CLASS_NAME, "Horse04")
        for h4 in horse4:
            print(h4.text)

        # トレセン・調教師
        horse5 = self.driver.find_elements(By.CLASS_NAME, "Horse05")
        for h5 in horse5:
            print(h5.text)

        # 間隔
        horse6 = self.driver.find_elements(By.CLASS_NAME, "Horse06")
        for h6 in horse6:
            print(h6.text)

        # オッズ（人気）
        horse7 = self.driver.find_elements(By.CLASS_NAME, "Horse07")
        for h7 in horse7:
            print(h7.text)

        # 馬齢
        barei = self.driver.find_elements(By.CLASS_NAME, "Barei")
        for b in barei:
            print(b.text)

if __name__ == "__main__":
    net_keiba = NetKeibaScraping()
    net_keiba.get_horse_info_of_main_race()
    net_keiba.driver.quit()
