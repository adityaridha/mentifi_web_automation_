import os

path = os.getcwd()
reporting_path = path + "\\test_report\\"

os.system("pytest -v -s {} --html={}report.html --self-contained-html".format(path, reporting_path))