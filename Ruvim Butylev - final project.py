import requests
import json
APPID = '780ebeaf90ee70836c71fc164346ad42'
def get_forecasturl_zipcode(zipcode):
   url = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&appid=%s' % (zipcode, APPID)
   return url
def get_forecasturl_city(city):
  url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s' % (city, APPID)
  return url
def main():
  user_input = input('Enter zip code or city: ')
  if user_input.isdecimal():
      url = get_forecasturl_zipcode(user_input)
  else :
        url = get_forecasturl_city(user_input)
  response = requests.get(url) 
  try:
          response.raise_for_status()
          print('Connection was successful')
  except:
    print('Connection was not succesful')
  weathers = json.loads(response.text)['list']
  print('Weather today is ' + weathers[0]['weather'][0]['main'])
  print('Weather tomorrow is ' + weathers[1]['weather'][0]['main'])
if __name__ == "__main__":
   main()
