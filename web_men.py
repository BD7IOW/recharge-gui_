import requests
import json
import time
#上传数据到OneNet，解析接收到的数据

class _Device():
    def __init__(self, DEVICEID, APIKEY):
        self.DEVICEID = DEVICEID
        self.APIKEY = APIKEY
        self.url = 'http://api.heclouds.com/devices/%s/datapoints' % (self.DEVICEID)
        self.headers = {"api-key": self.APIKEY, "Connection": "close"}

    def upload_point(self, DataStreamName, VALUE):
        dict = {"datastreams": [{"id": "id", "datapoints": [{"value": 0}]}]}
        dict['datastreams'][0]['id'] = DataStreamName
        dict['datastreams'][0]['datapoints'][0]['value'] = VALUE
        if "succ" in requests.post( self.url, headers=self.headers, data=json.dumps( dict ) ).text:
            print( "Value:", VALUE, " has been uploaded to ", DataStreamName, " at ", time.ctime() )

    def get_point(self, DataStreamName):
        data = json.loads( requests.get( self.url, headers=self.headers, ).text )
        for i in data['data']['datastreams']:
            if i["id"] == DataStreamName:
                return int( i['datapoints'][0]['value'] )
        else:
            return "Not found DataStreamName - %s " % DataStreamName


#if __name__ == "__main__":
#    DeviceID = '516700209'  # 设备ID
#    ApiKey = 'r3TgWwbT=RgClmM=djjgWGe6AEM='  # APIKey管理中的默认APIKEY
#    DataStreamName = 'temperature'  # 数据流名称，没有则新建数据流
 #   device = Device( DeviceID, ApiKey )
 #   while True:
 #       device.upload_point( DataStreamName, 67 )  # 向数据流中添加新数据
 #       print( device.get_point( DataStreamName ) )  # 查询数据流中的最新数据
 #       time.sleep( 1 )
