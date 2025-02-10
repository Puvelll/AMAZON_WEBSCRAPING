from selenium.webdriver.common.by import By


class GetElementHtml:
    elements = {
        "ID": By.ID,
        "XPATH": By.XPATH,
        "CLASS_NAME": By.CLASS_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME
    }

    def search_element(self, driver, element, value):
        try:
            by = GetElementHtml.elements.get(element.upper())
            return driver.find_element(by, value)
        except:
            print({"erro": True, "Log": "Erro ao tentar encontrar elemento"})

    def search_elements(self, driver, element, value):
        try:
            by = GetElementHtml.elements.get(element.upper())
            return driver.find_elements(by, value)
        except:
            print({"erro": True, "Log": "Erro ao tentar encontrar elemento"})
          