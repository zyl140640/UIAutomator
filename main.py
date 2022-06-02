import pytest

from common.init import AppStart

if __name__ == '__main__':
    # cc = AppStart.start()
    # print(cc)
    pytest.main(['-s', '-v'])
    # pytest.main(['-v', '-s', 'testcases/run.py'])
