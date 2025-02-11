from selenium.webdriver import Chrome, Firefox


class Browser:

    browsers = {
    "firefox": Firefox,
    "chrome": Chrome
    }

    def get_browser(cls, browser: str, time_wait = 2):
        result = Browser.browsers.get(browser if browser == 'firefox' or browser == 'chrome' else None)
        cls.driver = result()
        cls.driver.implicitly_wait(time_wait)
        cls.driver.maximize_window()
        return cls.driver

    def quit(self):
        try:
            self.driver.quit()
        except:
            print({"erro": True, "Log": "Erro ao realizar realizar pesquisa no site"})