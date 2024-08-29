from Lesson_7.bonigarcia.Pages.Datafields import DataFild
from Lesson_7.bonigarcia.Pages.Mainpage import Mainpages

def test_assertion(chrome_browser):
        main_page = Mainpages(chrome_browser)
        main_page.find_fields()
        main_page.filling_in_the_fields()
        main_page.click_sumbit_button()
        
        data_fild = DataFild(chrome_browser)
        data_fild.find_fields()
        data_fild.get_class_first_mane()
        data_fild.get_class_last_mane()
        data_fild.get_class_address()
        data_fild.get_class_email()
        data_fild.get_class_phone()
        data_fild.get_class_city()
        data_fild.get_class_country()
        data_fild.get_class_job_position()
        data_fild.get_class_company()
        data_fild.get_class_zip_code()
        
        assert "success" in data_fild.get_class_first_mane()
        assert "success" in data_fild.get_class_last_mane()
        assert "success" in data_fild.get_class_address()
        assert "success" in data_fild.get_class_email()
        assert "success" in data_fild.get_class_phone()
        assert "success" in data_fild.get_class_city()
        assert "success" in data_fild.get_class_country()
        assert "success" in data_fild.get_class_job_position()
        assert "success" in data_fild.get_class_company()
        assert "danger" in data_fild.get_class_zip_code()