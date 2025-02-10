from selenium.webdriver import Chrome, Firefox


class Browser:

    def get_browser(self, browser: str, time_wait = 10):
        browsers = {
        "firefox": Firefox,
        "chrome": Chrome
        }
        result = browsers.get(browser if browser == 'firefox' or browser == 'chrome' else None)
        self.browser = result()
        self.browser.implicitly_wait(time_wait)
        self.browser.maximize_window()
        return self.browser

    def quit(self):
        try:
            self.driver.quit()
        except:
            print({"erro": True, "Log": "Erro ao realizar realizar pesquisa no site"})