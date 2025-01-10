from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.firefox import GeckoDriverManager


class Parser:
    def __init__(self):
        self.driver = self.init_driver()
        self.url = "https://samokat.ru/product/7aa34600-651a-11e9-80c5-0cc47a817925"

    def init_driver(self):
        options = Options()
        options.add_argument("--headless")  # Фоновый режим
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        return driver

    def get_data(self):
        try:
            self.driver.get(self.url)

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Text_text__7SbT7"))
            )

            # Получение страницы через BeautifulSoup
            soup = BeautifulSoup(self.driver.page_source, "html.parser")

            # Поиск по классам
            product_name = soup.find(
                "h1",
                class_="Text_text--type_h3Bold__MrLyt",
            )

            return product_name.text if product_name else "Продукт не найден"
        except Exception as e:
            return f"Ошибка: {e}"
        finally:
            self.driver.quit()

    def send_data(self):
        pass


if __name__ == "__main__":
    parser = Parser()
    print(parser.get_data())
