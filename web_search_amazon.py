from browser import Browser
from get_element import GetElementHtml
from selenium.webdriver.common.keys import Keys
from collections import defaultdict


class WebSearchAmazon(Browser, GetElementHtml):

    def __init__(self, browser, name_product):
        self.driver = self.get_browser(browser)
        self.name_product = name_product
        self.driver.get('https://www.amazon.com.br/ref=nav_logo')


    def search_product(self):
        try:
            element = self.search_element(self.driver, "ID", "twotabsearchtextbox")
            element.send_keys(self.name_product)
            element.send_keys(Keys.ENTER)
        except:
            print({"erro": True, "Log": "Erro ao realizar realizar pesquisa no site"})

    def get_infos(self):
        try:
            elements = self.search_elements(self.driver, "XPATH", "//*[@class='a-section a-spacing-base']")

            dict_default = defaultdict(str)
            for element in elements:
                title = self.search_element(element, "XPATH", ".//*[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']").text
                price = self.search_element(element, "XPATH", ".//*[@class='a-price-whole']").text
                dict_default(title=title, price=price)

        except:
            print({"erro": True, "Log": "Erro ao realizar raspagem no site"})


app = WebSearchAmazon('chrome', 'RX 580')
app.search_product()
app.get_infos()