import datetime
from time import sleep
import requests
import json

headers={
    #浏览器标识
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
#使用fidder抓到的url地址
url='https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/9636bf85-6af6-4137-88ab-0901d3377332'
#对url发送请求
resopnse=requests.get(url,headers=headers)
#将json格式数据转换为字典
dictionary=json.loads(resopnse.text)

#拿到字典里的变量
def getProductMessage():
    #商品名称
    market_name=dictionary['data']['name']
    #规格
    spec=dictionary['data']['spec']
    #折扣价
    discount_price=dictionary['data']['price']/100
    #原价
    price=dictionary['data']['market_price']/100
    #详细内容
    content=dictionary['data']['share_content']
    print('---------------------------------------商品:'+market_name+'---------------------------------------')
    print('规格:'+spec)
    print('价格:'+str(discount_price))
    print('原价/折扣价:'+str(price)+"/"+str(discount_price))
    print('详细内容:'+content)
    print('---------------------------------------"'+market_name+'"的价格波动---------------------------------------')

#创建实时刷新的函数
def nowTime():
    while(True):
        #循环多次爬取
        resopnse=requests.get(url,headers=headers)
        dictionary=json.loads(resopnse.text)

        #当前价格
        nowPrice=dictionary['data']['price']/100
        #获取当前时间
        now=datetime.datetime.now()
        print('当前时间为:'+now.strftime("%Y/%m/%d %H:%M")+',价格为'+str(nowPrice))
        #3秒刷新一次
        sleep(3)


if __name__ == '__main__':
    getProductMessage()
    nowTime()

