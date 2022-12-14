import os
import warnings
import pytest

warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == '__main__':
    pytest.main(['-s', '-v'])
    os.system("allure generate ./temps -o ./reports --clean")
