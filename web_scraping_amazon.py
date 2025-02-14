from browser import Browser
from get_element import GetElementHtml
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Soup
from BeautifulSoup import Find

class WebSearchAmazon(Browser, GetElementHtml, Find):

    def __init__(self, browser, name_product):
        self.driver = self.get_browser(browser)
        self.name_product = name_product.replace(' ', '+')
        self.driver.get(f'https://www.amazon.com.br/s?k={self.name_product}')
        self.result = []
        self.qtd_items = 0

    def get_infos(self):
        try:
            self.status_page_ok()
            elements = self.search_elements(self.driver, "XPATH", "//*[@class='a-section a-spacing-base']")
            
            for element in elements:
                page = Soup(element.get_attribute('outerHTML'), features='html.parser')

                var = self.find_class(page, img_element="s-image", name_element="a-size-base-plus a-spacing-none a-color-base a-text-normal", price_element="a-price-whole", cents_element="a-price-fraction")
                self.result.append(var)
                self.qtd_items +=1
                print(self.qtd_items)

            self.next_page()

        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao realizar raspagem no site", "Log": {e}})

    def next_page(self):
        try:
            element = self.search_element(self.driver, "XPATH", f"//*[text()='Próximo']")
            if element.accessible_name == "Próximo":
                print("Raspagem finalizada")
                print(self.result)
                self.quit()
            element.click()
            self.load_screen()
            
            self.get_infos()
        except Exception as e:
            print({"erro": True, "Motivo": "Erro ao acessar a proxima pagina", "Log": {e}})

    def load_screen(self):
        try:
            self.search_element(self.driver, "XPATH", "//*[@class='s-result-list-placeholder sg-row aok-hidden']")
        except Exception as e:
            print({"erro": True, "Motivo": "Indicador de load não encontrado", "Log": {e}})


app = WebSearchAmazon('firefox', 'Rx 580')
app.get_infos()
