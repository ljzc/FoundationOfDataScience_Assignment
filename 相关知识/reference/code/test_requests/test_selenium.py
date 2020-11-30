from selenium import webdriver

def get_page_code():
    browser = webdriver.Chrome()
    browser.get("https://www.gdtv.cn/article/d8ce76c698be50c3411aa199a3e871ab")
    print(browser.page_source)
    browser.close()

if __name__ == '__main__':
    get_page_code()