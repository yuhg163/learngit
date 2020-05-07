# -*- coding:utf-8 -*-
#from Scripts.HTMLTestRunner import HTMLTestRunner
#####################################
#作者：邹辉《自动化平台测试开发》书
#日期：2018年1月
#版本：autotestplat V1.0
#####################################
import requests, time, sys, re
import urllib, zlib 
import pymysql 
import HTMLTestRunner

import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from apitest.celery_tasks import app

from time import sleep

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from autotest.settings import getDatabases
#from appium import webdriver

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                           
)

global driver

@app.task       
def webauto_testcase(self):            #流程 的 相关接口
    options = Options()
    #关掉沙盒，让Chrome在root权限下跑
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #不打开浏览器
    #options.add_argument('--headless')
    #指定浏览器分辨率
    #options.add_argument('window-size=1920x1680')
    #谷歌文档提到需要加上这个属性来规避bug
    options.add_argument('--disable-gpu')
    #不加载图片
    options.add_argument('blink-settings=imagesEnabled=false')
    self.driver2=webdriver.Chrome(chrome_options=options)
    self.driver2.get("http://192.168.0.91:85")
    sql="SELECT id,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata,`webtestresult` from webtest_webcasestep where webtest_webcasestep.Webcase_id=1 ORDER BY id ASC " 
    coon = pymysql.connect(user=getDatabases('user'),passwd=getDatabases('passwd'),db=getDatabases('db'),port=getDatabases('port'),host=getDatabases('host'),charset=getDatabases('charset'))
    cursor = coon.cursor()
    aa=cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:   
        case_list = []
        case_list.append(ii)
        webtestcase(self,case_list)
    sql2="select webtestresult from webtest_webcasestep where webtest_webcasestep.Webcase_id=1"
    bb=cursor.execute(sql2)
    info2 = cursor.fetchmany(bb)
    n=0
    caseWriteCaseResult('1','1')
    for jj in info2:
        if info2[n][0] == 1:
            n=n+1
        else:
            caseWriteCaseResult('1','0')
            break
    coon.commit()
    cursor.close()
    coon.close()
    self.driver2.quit()

# coon = pymysql.connect(user=getDatabases('user'),passwd=getDatabases('passwd'),db=getDatabases('db'),port=getDatabases('port'),host=getDatabases('host'),charset=getDatabases('charset'))
# cursor = coon.cursor()
# sql2="select webtestresult from webtest_webcasestep where webtest_webcasestep.Webcase_id=1"
# aa=cursor.execute(sql2)
# info = cursor.fetchmany(aa)
# n=0
# for ii in info:
#     print (n)
#     print (info[n][0])
#     n=n+1

# def webtest_report(self):
#     suite=unittest.TestSuite()
#     suite.addTest(webtestcase(self,case_list))
#     filename="webtest/templates/"+"webtest_report.html"
#     fp=open(filename,'wb')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"web自动化测试报告",description=u"搜索测试用例")
#     runner.run(suite)
#     fp.close()

@app.task
def webauto_testcase2(self):            #流程 的 相关接口
    options = Options()
    #关掉沙盒，让Chrome在root权限下跑
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #不打开浏览器
    #options.add_argument('--headless')
    #指定浏览器分辨率
    #options.add_argument('window-size=1920x1680')
    #谷歌文档提到需要加上这个属性来规避bug
    #options.add_argument('--disable-gpu')s
    #不加载图片
    #options.add_argument('blink-settings=imagesEnabled=false')
    self.driver2=webdriver.Chrome(chrome_options=options)
    self.driver2.get("http://www.baidu.com")
    sql="SELECT id,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata,`webtestresult` from webtest_webcasestep where webtest_webcasestep.Webcase_id=2 ORDER BY id ASC "
    coon = pymysql.connect(user=getDatabases('user'),passwd=getDatabases('passwd'),db=getDatabases('db'),port=getDatabases('port'),host=getDatabases('host'),charset=getDatabases('charset'))
    cursor = coon.cursor()
    aa=cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        webtestcase(self,case_list)
    coon.commit()
    cursor.close()
    coon.close()
    self.driver2.quit()

def webtestcase(self,case_list):  
    for case in case_list:
        try:   
            case_id = case[0]
            findmethod = case[1] 
            evelement = case[2]
            optmethod = case[3]
            testdata = case[4]
            assertdata = case[5]
        except Exception as e:
            print('测试用例格式不正确！%s'%e)
            return '测试用例格式不正确！%s'%e
        print (case)
        time.sleep(3)
        if optmethod=='sendkeys':
            if findmethod=='find_element_by_id':
                print (evelement)
                try:
                    self.driver2.find_element_by_id(evelement).send_keys(testdata)
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_name':
                print (evelement)
                try:
                    self.driver2.find_element_by_name(evelement).send_keys(testdata)
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_class_name':
                print (evelement)
                try:
                    self.driver2.find_element_by_class_name(evelement).send_keys(testdata)
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_xpath':
                print (evelement)
                try:
                    self.driver2.find_element_by_xpath(evelement).send_keys(testdata)
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            else:
                caseWriteStepResult(case[0],'0')
                print('定位方式不支持！')
                return '定位方式不支持！'
            caseWriteStepResult(case[0],'1')
            return True
        elif optmethod=='click':
            if findmethod=='find_element_by_id':
                print (evelement)
                try:
                    self.driver2.find_element_by_id(evelement).click()
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_name':
                print (evelement)
                try:
                    self.driver2.find_element_by_name(evelement).click()
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_class_name':
                print (evelement)
                try:
                    self.driver2.find_element_by_class_name(evelement).click()
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_xpath':
                print (evelement)
                try:
                    self.driver2.find_element_by_xpath(evelement).click()
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            else:
                caseWriteStepResult(case[0],'0')
                print('定位方式不支持！')
                return '定位方式不支持！'
            caseWriteStepResult(case[0],'1')
            return True
        elif optmethod=='check':
            if findmethod=='find_element_by_id':
                print (evelement)
                try:
                    t=self.driver2.find_element_by_id(evelement).text
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_name':
                print (evelement)
                try:
                    t=self.driver2.find_element_by_name(evelement).text
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_class_name':
                print (evelement)
                try:
                    t=self.driver2.find_element_by_class_name(evelement).text
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            elif findmethod=='find_element_by_xpath':
                print (evelement)
                try:
                    t=self.driver2.find_element_by_xpath(evelement).text
                except Exception as e:
                    caseWriteStepResult(case[0],'0')
                    return '无法定位到元素！%s'%e
            else:
                caseWriteStepResult(case[0],'0')
                print('用例ID为%d的定位方式不支持！'%(case_id))
                return '定位方式不支持！'
            if assertdata in t:
                caseWriteStepResult(case_id,'1')
                return True
            else:
                caseWriteStepResult(case_id,'0')
                return False
        else:
            return '操作方法不支持！'

        # if optmethod=='sendkeys' and findmethod=='find_element_by_id':
        #     print (evelement)
        #     self.driver2.find_element_by_id(evelement).send_keys(testdata)
        # elif optmethod=='sendkeys' and findmethod=='find_element_by_name':
        #     print (evelement)
        #     self.driver2.find_element_by_name(evelement).send_keys(testdata)
        # elif optmethod=='click' and findmethod=='find_element_by_name':
        #     print (evelement)
        #     self.driver2.find_element_by_name(evelement).click()
        # elif optmethod=='click' and findmethod=='find_element_by_id':
        #     print (evelement)
        #     self.driver2.find_element_by_id(evelement).click()
        # elif optmethod=='check' and findmethod=='find_element_by_id':
        #     print (evelement)
        #     t=self.driver2.find_element_by_id(evelement).text
        #     if assertdata in t:
        #         caseWriteStepResult(case_id,'1')
        #     else:
        #         caseWriteStepResult(case_id,'0')
        # elif optmethod=='check' and findmethod=='find_element_by_name':
        #     print (evelement)
        #     t=self.driver2.find_element_by_name(evelement).text
        #     if assertdata in t:
        #         caseWriteStepResult(case_id,'1')
        #     else:
        #         caseWriteStepResult(case_id,'0')
        # elif optmethod=='check' and findmethod=='find_element_by_class_name':
        #     print (evelement)
        #     t=self.driver2.find_element_by_class_name(evelement).text
        #     if assertdata in t:
        #         caseWriteStepResult(case_id,'1')
        #     else:
        #         caseWriteStepResult(case_id,'0')
        # else:
        #     return '测试用例格式不正确！'

def caseWriteStepResult(case_id,result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE webtest_webcasestep set webtest_webcasestep.webtestresult=%s,webtest_webcasestep.create_time=%s where webtest_webcasestep.id=%s;"
    param = (result,now,case_id)
    coon = pymysql.connect(user=getDatabases('user'),passwd=getDatabases('passwd'),db=getDatabases('db'),port=getDatabases('port'),host=getDatabases('host'),charset=getDatabases('charset'))
    cursor = coon.cursor()
    cursor.execute(sql,param)
    print ('webcasestep result is '+result.decode())
    coon.commit()
    cursor.close()
    coon.close()

def caseWriteCaseResult(case_id,result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE webtest_webcase set webtest_webcase.webtestresult=%s,webtest_webcase.create_time=%s where webtest_webcase.id=%s;"
    param = (result,now,case_id)
    coon = pymysql.connect(user=getDatabases('user'),passwd=getDatabases('passwd'),db=getDatabases('db'),port=getDatabases('port'),host=getDatabases('host'),charset=getDatabases('charset'))
    cursor = coon.cursor()
    cursor.execute(sql,param)
    print ('webcase result is '+result.decode())
    coon.commit()
    cursor.close()
    coon.close()