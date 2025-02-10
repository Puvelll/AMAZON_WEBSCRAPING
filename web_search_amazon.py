from browser import Browser
from get_element import GetElementHtml
from selenium.webdriver.common.keys import Keys

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

            for element in elements:
                self.scrol_element(element)
                title = self.search_element(element, "XPATH", ".//*[@class='a-size-base-plus a-spacing-none a-color-base a-text-normal']")
                print(type(title))
                price = self.search_element(element, "XPATH", ".//*[@class='a-price-whole']")
                dict_ = {"title":title.text if title else None, "price":price.text if price else None}
                print(dict_)

        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao realizar raspagem no site", "Log": {e}})

    def scrol_element(self, element):
        try:
            element.location_once_scrolled_into_view
        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao descer a pagina site", "Log": {e}})


app = WebSearchAmazon('chrome', 'RX 580')
app.search_product()
app.get_infos()