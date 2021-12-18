from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import csv
# import pyautogui

options = webdriver.ChromeOptions()
file_path = "C:/Users/it/Desktop/test.csv"

standard_name = []
name_cn_list = []
name_en_list = []

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def login():
    print("尝试登录")
    try:
        url = 'http://deming.dp.yiducloud.cn/qc/#/standard/version?layerCurrent=DP'
        driver.get(url)
        time.sleep(10)
    except TimeoutException:
        login()


def crawl():
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/dl/dd/ul/li[1]/div[1]')
    except:
        pass
    temp_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/h3/a').text
    test_list = driver.find_elements_by_css_selector("[class='name cn']")
    for i in range(0, len(test_list)):
        standard_name.append(temp_name)
        name_cn_list.append(test_list[i].text)
    test_list = driver.find_elements_by_css_selector("[class='name en']")
    for i in range(0, len(test_list)):
        name_en_list.append(test_list[i].text)


def insert():
    with open(file_path, 'w', newline='', encoding='utf-8-sig')as f:
        fieldnames = ["标准名称", "中文表名", "英文表名"]
        f_csv = csv.DictWriter(f, fieldnames=fieldnames)
        f_csv.writeheader()
        for i in range(0, len(name_cn_list)):
            f_csv.writerow(
                {
                    "标准名称": standard_name[i],
                    "中文表名": name_cn_list[i],
                    "英文表名": name_en_list[i]
                }
            )
    f.close()


def main():
    login()
    url = 'http://deming.dp.yiducloud.cn/qc/#/standard/version?layerCurrent=DP'
    driver.get(url)
    time.sleep(1)
    a = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div/div/div/div[3]/div/div/div[1]/div/i')
    a.click()
    count = driver.find_elements_by_xpath('//div[@class="ivu-select ivu-select-visible ivu-select-single ivu-select-default"]//li[@class="ivu-select-item"]')
    count = len(count)
    count1 = count
    target = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div/div/div/div[3]/div/div/div[2]/ul[2]/li[' + str(count1) + ']')
    driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
    time.sleep(1)
    a = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/table/tbody/tr[3]/td[5]/a[1]')
    a.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    print("正在爬取第 1 个表数据，还剩", str(count), "个！")
    crawl()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    i = 2
    # while i != 10:
    while True:
        try:
            a = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div/div/div/div[3]/div/div/div[1]/div/i')
            a.click()
            time.sleep(1)
            # if i % 7 == 0:
            #     pyautogui.click(1405, 780, clicks=1, interval=0.0, button='left')
            a = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/form/div/div/div/div[3]/div/div/div[2]/ul[2]/li['+str(i)+']')
        except:
            break
        a.click()
        time.sleep(1)
        try:
            a = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/table/tbody/tr/td[5]')
        except:
            i = i+1
            time.sleep(1)
            print("第 ", str(i), " 个规则无标准")
            continue
        a.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        count = count1 - i + 1
        print("正在爬取第", str(i), "个表数据，还剩", str(count), "个！")
        crawl()
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        i = i+1
    insert()


if __name__ == '__main__':
    main()
