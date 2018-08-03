
import requests

url='https://api.64clouds.com/v1/'
methods=[
    'start', #0
    'stop', #1
    'restart', #2
    'migrate/getLocations', # 3 
    'migrate/start',  #4
]
locations=['USCA_3','USCA_8']

veid=''
apikey=''

data={
    'veid':veid,
    'api_key':apikey,
}

r=requests.post(url+methods[3],data)
if(r.json()['currentLocation']==locations[0]):
    data['location']=locations[1]
else:
    data['location']=locations[0]
requests.post(url+methods[4],data)

