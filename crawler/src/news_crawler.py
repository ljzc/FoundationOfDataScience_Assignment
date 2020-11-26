class NewsCrawler(object):

    def __init__(self):
        self.__crawl_strategies = dict()
        self.__news = dict()

    '''
    用来在__craw_strategies属性中添加相应的爬取策略,格式为:
    {strategy_name: strategy}
    '''
    def __set_up_strategies(self):
        pass

    def crawl(self, url, strategy):
        pass

    def export_news(self, abs_path):
        pass



#
# import requests
#
#
# # 我这里是将经纬度转换为地址，所以选用的是逆地理编码的接口。
# # https://restapi.amap.com/v3/geocode/regeo?
# # output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all
#
# # 高德地图
# def geocode1(location):
#     parameters = {'output': 'json', 'location': location, 'key': 'b65ac7bac54ed07220e8d05ab93ad469',
#                   'extensions': 'all'}
#     base = 'https://restapi.amap.com/v3/geocode/regeo'
#     response = requests.get(base, parameters)
#     answer = response.json()
#     print('url:' + response.url)
#     print(answer)
#     # return answer['regeocode']['formatted_address'], answer['regeocode']['roads'][0]['id'], answer['regeocode']['roads'][0]['name']
#
# if __name__ == '__main__':
#     geocode1("天安门")
#
