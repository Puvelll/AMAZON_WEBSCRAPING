from selenium.webdriver.common.by import By

class GetElementHtml:
    tags = {
        "ID": By.ID,
        "XPATH": By.XPATH,
        "CLASS_NAME": By.CLASS_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME
    }

    def search_element(self, driver, tag: str, element: str):
        try:
            by = GetElementHtml.tags.get(tag.upper())
            result = driver.find_element(by, element)
            return result
        except:
            return{"erro": True, "Log": "Erro ao tentar encontrar elemento"}

    def search_elements(self, driver, tag, element):
        try:
            by = GetElementHtml.tags.get(tag.upper())
            result = driver.find_elements(by, element)
            return result 
        except:
            return{"erro": True, "Log": "Erro ao tentar encontrar elemento {}"}

    def scrol_element(self, element):
        try:
            element.location_once_scrolled_into_view(element)
        except Exception as e:
            return{"erro": True, "Motivo": "Erro ao descer a pagina site", "Log": {e}}
        
    def status_page_ok(self):
        try: 
            while True:
                if self.driver.execute_script("return document.readyState") == "complete":
                    return
        except:
            return{"erro": True, "Motivo": "Erro ao carregar a pagina, metodo JS", "Log": {e}}
