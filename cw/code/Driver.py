from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return cls.instance

dvr = Driver()