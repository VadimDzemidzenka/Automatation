from lesson7.calculator.Pages.Calcmainpage import CalcMain

def test_calculator_assert(chrome_browser):
    calsmain = CalcMain(chrome_browser)
    calsmain.insert_time()
    calsmain.clicking_buttons()
    assert "15" in calsmain.wait_button_gettext()