# NopCommercePytest


Run from root folder:

pytest -v -s .\test_cases\Test_admin_login.py

pytest -v -s .\test_cases\test_admin_login_data_driven.py


pytest -v -s -n=2 .\test_cases\Test_admin_login.py


pytest -v -s -n=3 --html=reports\report.html --browser chrome .\test_cases\Test_admin_login.py