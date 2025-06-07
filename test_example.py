class TestExample:


    def test_title(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://skillbox.ru")
        assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title


    def test_title_pass_1(self, set_up_browser):
        pass


    def test_title_pass_2(self, set_up_browser):
        pass

