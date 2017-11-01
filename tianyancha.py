# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from datetime import datetime
import re
import time
import uuid
from DAO.tianyancha import tianyanchaDAO
import random
import csv
import os



class tianyanchaService(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
       
        self.tianyanchaDao = tianyanchaDAO()
      
        self.hotelItem = {}        
        self.commList = []
        self.hrefs = []
        self.urls = [

         'https://www.tianyancha.com/company/871276680\n',
         'https://www.tianyancha.com/company/871286084\n',
         'https://www.tianyancha.com/company/871323044\n',
         'https://www.tianyancha.com/company/871324900\n',
         'https://www.tianyancha.com/company/871397236\n',
         'https://www.tianyancha.com/company/871401623\n',
         'https://www.tianyancha.com/company/871567081\n',
         'https://www.tianyancha.com/company/871567864\n',
         'https://www.tianyancha.com/company/871567909\n',
         'https://www.tianyancha.com/company/871572837\n',
         'https://www.tianyancha.com/company/871576936\n',
         'https://www.tianyancha.com/company/871630257\n',
         'https://www.tianyancha.com/company/871645246\n',
         'https://www.tianyancha.com/company/871738964\n',
         'https://www.tianyancha.com/company/871758760\n',
         'https://www.tianyancha.com/company/871780212\n',
         'https://www.tianyancha.com/company/871857274\n',
         'https://www.tianyancha.com/company/871872852\n',
         'https://www.tianyancha.com/company/871965088\n',
         'https://www.tianyancha.com/company/871970489\n',
         'https://www.tianyancha.com/company/872036534\n',
         'https://www.tianyancha.com/company/872040835\n',
         'https://www.tianyancha.com/company/872047602\n',
         'https://www.tianyancha.com/company/872065383\n',
         'https://www.tianyancha.com/company/872069771\n',
         'https://www.tianyancha.com/company/872147454\n',
         'https://www.tianyancha.com/company/872159569\n',
         'https://www.tianyancha.com/company/872168397\n',
         'https://www.tianyancha.com/company/872271107\n',
         'https://www.tianyancha.com/company/872498429\n',
         'https://www.tianyancha.com/company/872656727\n',
         'https://www.tianyancha.com/company/873029439\n',
         'https://www.tianyancha.com/company/873034619\n',
         'https://www.tianyancha.com/company/873515427\n',
         'https://www.tianyancha.com/company/8736306\n',
         'https://www.tianyancha.com/company/87389771\n',
         'https://www.tianyancha.com/company/874029582\n',
         'https://www.tianyancha.com/company/874037352\n',
         'https://www.tianyancha.com/company/874059973\n',
         'https://www.tianyancha.com/company/874083261\n',
         'https://www.tianyancha.com/company/874256030\n',
         'https://www.tianyancha.com/company/874266885\n',
         'https://www.tianyancha.com/company/874715795\n',
         'https://www.tianyancha.com/company/874732710\n',
         'https://www.tianyancha.com/company/875593696\n',
         'https://www.tianyancha.com/company/875909189\n',
         'https://www.tianyancha.com/company/875916103\n',
         'https://www.tianyancha.com/company/875916142\n',
         'https://www.tianyancha.com/company/877224250\n',
         'https://www.tianyancha.com/company/877841497\n',
         'https://www.tianyancha.com/company/878019482\n',
         'https://www.tianyancha.com/company/878473174\n',
         'https://www.tianyancha.com/company/878658922\n',
         'https://www.tianyancha.com/company/879524\n',
         'https://www.tianyancha.com/company/879707095\n',
         'https://www.tianyancha.com/company/87971862\n',
         'https://www.tianyancha.com/company/879795660\n',
         'https://www.tianyancha.com/company/87989755\n',
         'https://www.tianyancha.com/company/87990834\n',
         'https://www.tianyancha.com/company/879961858\n',
         'https://www.tianyancha.com/company/880317604\n',
         'https://www.tianyancha.com/company/880678144\n',
         'https://www.tianyancha.com/company/88074945\n',
         'https://www.tianyancha.com/company/880765754\n',
         'https://www.tianyancha.com/company/880785349\n',
         'https://www.tianyancha.com/company/880788476\n',
         'https://www.tianyancha.com/company/882058046\n',
         'https://www.tianyancha.com/company/882127929\n',
         'https://www.tianyancha.com/company/882140181\n',
         'https://www.tianyancha.com/company/882143381\n',
         'https://www.tianyancha.com/company/8823567\n',
         'https://www.tianyancha.com/company/882556330\n',
         'https://www.tianyancha.com/company/882556529\n',
         'https://www.tianyancha.com/company/882591338\n',
         'https://www.tianyancha.com/company/882651523\n',
         'https://www.tianyancha.com/company/88273537\n',
         'https://www.tianyancha.com/company/883044892\n',
         'https://www.tianyancha.com/company/883092916\n',
         'https://www.tianyancha.com/company/883312866\n',
         'https://www.tianyancha.com/company/883568455\n',
         'https://www.tianyancha.com/company/883568518\n',
         'https://www.tianyancha.com/company/883568593\n',
         'https://www.tianyancha.com/company/883650555\n',
         'https://www.tianyancha.com/company/883786285\n',
         'https://www.tianyancha.com/company/884897970\n',
         'https://www.tianyancha.com/company/885134259\n',
         'https://www.tianyancha.com/company/885987027\n',
         'https://www.tianyancha.com/company/886406577\n',
         'https://www.tianyancha.com/company/886708568\n',
         'https://www.tianyancha.com/company/886710515\n',
         'https://www.tianyancha.com/company/886711386\n',
         'https://www.tianyancha.com/company/886726395\n',
         'https://www.tianyancha.com/company/887767558\n',
         'https://www.tianyancha.com/company/887767599\n',
         'https://www.tianyancha.com/company/887798157\n',
         'https://www.tianyancha.com/company/887835825\n',
         'https://www.tianyancha.com/company/887917974\n',
         'https://www.tianyancha.com/company/887947049\n',
         'https://www.tianyancha.com/company/887962805\n',
         'https://www.tianyancha.com/company/888316952\n',
         'https://www.tianyancha.com/company/888345337\n',
         'https://www.tianyancha.com/company/888799075\n',
         'https://www.tianyancha.com/company/889062629\n',
         'https://www.tianyancha.com/company/889075423\n',
         'https://www.tianyancha.com/company/889075547\n',
         'https://www.tianyancha.com/company/890908104\n',
         'https://www.tianyancha.com/company/892461177\n',
         'https://www.tianyancha.com/company/89855005\n',
         'https://www.tianyancha.com/company/90026683\n',
         'https://www.tianyancha.com/company/90427830\n',
         'https://www.tianyancha.com/company/9052288\n',
         'https://www.tianyancha.com/company/905611747\n',
         'https://www.tianyancha.com/company/905611837\n',
         'https://www.tianyancha.com/company/908386812\n',
         'https://www.tianyancha.com/company/90942935\n',
         'https://www.tianyancha.com/company/910856143\n',
         'https://www.tianyancha.com/company/913490121\n',
         'https://www.tianyancha.com/company/920321486\n',
         'https://www.tianyancha.com/company/923177522\n',
         'https://www.tianyancha.com/company/923478086\n',
         'https://www.tianyancha.com/company/925109846\n',
         'https://www.tianyancha.com/company/929508293\n',
         'https://www.tianyancha.com/company/929508431\n',
         'https://www.tianyancha.com/company/931005682\n',
         'https://www.tianyancha.com/company/93213991\n',
         'https://www.tianyancha.com/company/9329232\n',
         'https://www.tianyancha.com/company/934832919\n',
         'https://www.tianyancha.com/company/935310188\n',
         'https://www.tianyancha.com/company/937275606\n',
         'https://www.tianyancha.com/company/937302026\n',
         'https://www.tianyancha.com/company/937303366\n',
         'https://www.tianyancha.com/company/938870000\n',
         'https://www.tianyancha.com/company/942307907\n',
         'https://www.tianyancha.com/company/942439626\n',
         'https://www.tianyancha.com/company/9424721\n',
         'https://www.tianyancha.com/company/944302966\n',
         'https://www.tianyancha.com/company/94605915\n',
         'https://www.tianyancha.com/company/947944005\n',
         'https://www.tianyancha.com/company/94942910\n',
         'https://www.tianyancha.com/company/951708473\n',
         'https://www.tianyancha.com/company/953824997\n',
         'https://www.tianyancha.com/company/9578499\n',
         'https://www.tianyancha.com/company/964476137\n',
         'https://www.tianyancha.com/company/96762942\n',
         'https://www.tianyancha.com/company/969109012\n',
         'https://www.tianyancha.com/company/9719138\n',
         'https://www.tianyancha.com/company/973746532\n',
         'https://www.tianyancha.com/company/9743650\n',
         'https://www.tianyancha.com/company/97465513\n',
         'https://www.tianyancha.com/company/975145186\n',
         'https://www.tianyancha.com/company/982424094\n',
         'https://www.tianyancha.com/company/98533979\n',
         'https://www.tianyancha.com/company/9872836\n',
         'https://www.tianyancha.com/company/987465104\n',
         'https://www.tianyancha.com/company/993648475\n',
         'https://www.tianyancha.com/company/995041681\n',
         'https://www.tianyancha.com/company/9973938\n',
         'https://www.tianyancha.com/company/999271057\n',
         'https://www.tianyancha.com/company/999325380\n',
         'https://www.tianyancha.com/company/999999195'







        ]





    
    def getdata(self):

        
        print len(self.urls)
        for lianjie_data in self.urls:
            self.intocompany(lianjie_data)




     # 进入企业
    def intocompany(self,Links):
        username = "*********"#登录账户名
        password = "1234444"#password
        url = Links
        print url
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(80)
        time.sleep(4)
        response = HtmlResponse(url="my HTML string", body=self.driver.page_source, encoding="utf-8")
        company = response.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[1]/span[1]/text()').extract()
        print company
        if(len(company)==0):
                cookie1 = self.driver.get_cookies()
                print cookie1

                time.sleep(3)
                elem = self.driver.find_element_by_xpath(
                        '//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input');

                elem.send_keys(username)
                elem = self.driver.find_element_by_xpath(
                        '//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input');
                elem.send_keys(password)

                self.driver.find_element_by_xpath(
                        '//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]').click()
                time.sleep(random.uniform(3, 6))
               
                cookie2 = self.driver.get_cookies()
                # 将获得cookie的信息打印
                print cookie2

        self.crawlcommentinfo()





    def crawlcommentinfo(self):
        response = HtmlResponse(url="my HTML string", body=self.driver.page_source, encoding="utf-8")
       
        loopNum = 0
        
        ifHandle = False

        #pageNum = pagenum
        pageNum = 100
        while(pageNum>=1):
            # 循环次数加1
            loopNum = loopNum + 1
          

            if u"对外投资" in self.driver.page_source:
                pageNum = pageNum - 1
            # 对未解析过的页面进行解析
                #print ifHandle==False
                print "第"+str(loopNum)+"页"
                if ifHandle==False:
                    self.getcommentinfo(self.driver.page_source)
                    ifHandle = True
                try:
                    #//*[@id="_container_invest"]/div/div[2]/div
                    num = response.xpath('//*[@id="_container_invest"]/div/div[2]/div/text()').extract()
                    if (num):
                      
                        print num[0]
                        print "loopNum :" + str(loopNum)
                        if (loopNum + 1 > 1):
                            break
                     
                        target2 = self.driver.find_element_by_xpath('//*[@id="_container_invest"]/div/div[2]')
                        y2 = target2.location['y']
                        print y2
                        target = self.driver.find_element_by_css_selector(
                                '#_container_invest > div > div.company_pager > ul > li.pagination-next > a')
                        target1 = self.driver.find_element_by_css_selector(
                         '#_container_changeinfo > div > div.company_pager > ul')

                        # //*[@id="nav-main-inverstCount"]#nav-main-inverstCount
                        y = target.location['y']
                        y1 = target1.location['y']
                        print y,y1
                        y = y - 100

                        js = "var q=document.documentElement.scrollTop=" + str(y)
                        #print js
                        self.driver.execute_script(js)
                      
                        self.driver.find_element_by_xpath('//*[@id="_container_invest"]/div/div[2]/ul/li[@class="pagination-next "]/a').click()

                        #self.driver.find_element_by_partial_link_text("下一页").click()
                        ifHandle = False
                        # 单页循环次数置为零
                        #loopNum = 0
                        time.sleep(random.uniform(4,7))
                    else:
                            break

                except:
                    pass

        return False if pageNum>1 else True


    # 解析评论页面
    def getcommentinfo(self, page_sourse):
        response = HtmlResponse(url="my HTML string", body=page_sourse, encoding="utf-8")
        #print response
        company = response.xpath('//*[@id="company_web_top"]/div[2]/div[2]/div[1]/span[1]/text()').extract()[0]
        code = response.xpath('//*[@id="_container_baseInfo"]/div/div[@class="base0910"]/table/tbody/tr[1]/td[4]/text()').extract()
        if(code):
         code = code[0]
        else:
         code = 'null'

        category = response.xpath('//*[@id="_container_baseInfo"]/div/div[@class="base0910"]/table/tbody/tr[3]/td[4]/text()').extract()
        if(category):
         category = category[0]
        else:
         category = 'null'
        address = response.xpath('//*[@id="_container_baseInfo"]/div/div[@class="base0910"]/table/tbody/tr[5]/td[4]/text()').extract()
        if(address):
         address = address[0]
        else:
         address = 'null'
        range1 = response.xpath('//*[@id="_container_baseInfo"]/div/div[@class="base0910"]/table/tbody/tr[7]/td[2]/span/span/span[1]/text()').extract()
        if(range1):
         range1 = range1[0]
        else:
         range1 = 'null'
        tocompanys = response.xpath('//div[@id="_container_invest"]/div/div/table/tbody/tr')
        for i in tocompanys:
                tocompany = i.xpath('td[1]/a/span/text()').extract()[0]

                href = 'https://www.tianyancha.com' + i.xpath('td[1]/a/@href').extract()[0]
                a = i.xpath('td[1]/a/@href').extract()[0]
                ID = code + '_' + a.split("/")[2]
                name = i.xpath('td[2]/span/a/text()').extract()
                if(name):
                  name = name[0]
                else:
                  name = 'null'
                zhuce_money = i.xpath('td[3]/span/text()').extract()
                if(zhuce_money):
                        zhuce_money = zhuce_money[0]
                else:
                        zhuce_money = 'null'
                touzi = i.xpath('td[4]/span/text()').extract()
                if(touzi):
                        touzi = touzi[0]
                else:
                        touzi = 'null'

                percent = i.xpath('td[5]/span/text()').extract()
                if(percent):
                        percent = percent[0]
                else:
                        percent = 'null'
                time = i.xpath('td[6]/span/text()').extract()
                if(time):
                   time = time[0]
                else:
                   time = 'null'
                state = i.xpath('td[7]/span/text()').extract()[0]



                #print ID,tocompany,name,zhuce_money,touzi,percent,time,state,href

                self.commList.append({"company":company,"code":code,"category":category,"address":address, "range1":range1, "ID":ID,
                                  "tocompany":tocompany,"name":name,"zhuce_money":zhuce_money,"touzi":touzi,"percent":percent,
                                  "time":time,"state":state,"href":href})
        xiechenghotelService.saveListCommentInfo()
        print len(self.commList)
        self.commList = []
    def saveListCommentInfo(self):
        self.tianyanchaDao.saveCompanyCommentinfo1(self.commList)

    def depose(self):
        self.driver.close()

if __name__=="__main__":
    tianyanchaService = tianyanchaService()
    tianyanchaService.getdata()
    tianyanchaService.depose()
