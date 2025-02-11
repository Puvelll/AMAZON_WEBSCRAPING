from browser import Browser
from get_element import GetElementHtml
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Soup
from BeautifulSoup import Find

class WebSearchAmazon(Browser, GetElementHtml, Find):

    def __init__(self, browser, name_product):
        self.driver = self.get_browser(browser)
        self.name_product = name_product
        self.driver.get('https://www.amazon.com.br/ref=nav_logo')
        self.result = []

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
                page = Soup(element.get_attribute('outerHTML'), features='html.parser')

                var = self.find_class(page, name_element="a-size-base-plus a-spacing-none a-color-base a-text-normal", price_element="a-price-whole", cents_element="a-price-fraction")
                print(f"{var}\n")
                self.result.append(var)

            self.next_page()

        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao realizar raspagem no site", "Log": {e}})

    def next_page(self):
        try:
            element = self.search_element(self.driver, "XPATH", f"//*[text()='Próximo']")
            if element.accessible_name == "Próximo":
                print("Raspagem finalizada")
                print(len(self.result))
                self.quit()
            element.click()
            
            self.get_infos()
        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao realizar raspagem no site", "Log": {e}})


app = WebSearchAmazon('chrome', 'Fogão')
app.search_product()
app.get_infos()