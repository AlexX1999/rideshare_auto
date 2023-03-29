import requests
import random
import math

class GaodeGeo:
    def __init__(self):
        self.key = '7b1694e4e39645fe00c2ff3e2737b780'

    def requestApi(self, url):
        re = requests.get(url).json()
        return re

    # 根据经纬坐标获取地址等信息
    def getInverseGeoCode(self, location):
        url = f'https://restapi.amap.com/v3/geocode/regeo?parameters&key={self.key}&location={location}'
        json_data = self.requestApi(url)
        if json_data['status'] == '1':
            area= json_data['regeocode']['formatted_address']
            return area
        else:
            return '获取失败'
gd = GaodeGeo()
 
# base_log：经度基准点， 
# base_lat：维度基准点， 
# radius：距离基准点的半径
def generate_random_gps(base_log=eval(input()), base_lat=eval(input()), radius=eval(input())):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    loga = '%.6f' % longitude
    lata = '%.6f' % latitude
    return loga, lata

lst=[]
for i in range(20):
    longitude_, latitude_ = generate_random_gps()
    string=[str( longitude_),str(latitude_)]
    place=','.join(string)
    area = gd.getInverseGeoCode(place)
    lst.append(area)
    print(area)  
