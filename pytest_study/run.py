import pytest
import os


if __name__ == '__main__':
    # python.main()会自动扫描当前目录下的pytest.ini文件中的配置，根据配置执行测试
    pytest.main()
    os.system("allure generate report/data -o report/html --clean")
