# GitLab-UI
## 迷姆消费端UI自动化

### common
>#### adb_util.py 文件用来获取测试设备的信息，包括测试设备ID和系统版本等内容
>#### appium_init.py Android设备初始化
>#### selenium_init.py web 浏览器初始化
>#### base_page.py 封装find_element, click，input，assert等基本方法
>#### yaml_util.py 封装yaml文件的读取，写入，删除操作
*******

### config
>#### driver文件夹下包含Chrome和Firefox浏览器驱动器
>#### env.yaml文件夹下存储环境变量
*******

### data
>#### page_element_v1.0文件夹下存储第一个版本的测试数据
*******

### logs
>####文件夹下存储日志
*******

### page
>#### Android文件夹下存储Android APP的操作方法，按照页面构建方法
>#### IOS文件夹下存储IOS APP的操作方法，按照页面构建方法
>#### WEB文件夹下存储Web APP的操作方法，按照页面构建方法
*******

### reports
>####文件夹下存储报告
*******

### testcases
>#### Android文件夹下存储Android APP的测试用例
>#### IOS文件夹下存储IOS APP的测试用例
>#### WEB文件夹下存储Web APP的测试用例
>#### conftest.py文件存储预请求用例
*******

### gitignore 
>#### 文件写入忽略的文件
*******

### main.py
>####执行用例的文件
*******

### pytest.ini
>####描述pytest框架的文件
*******

### main.py
>####执行用例的文件
*******

### README.md
>####本框架的解释文件，即你现在正在阅读的文件
*******

### requirements.txt
>####描述测试组件，测试库的文件