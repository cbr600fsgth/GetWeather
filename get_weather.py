#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import urllib
import urllib2
import json
import pprint
import types
import datetime
import commands
from get_weather_setting import api_key

import pytz	# タイムゾーン関連のモジュール

argv = sys.argv
argc = len(argv)

if argc==1 or not(os.path.isfile("weather.json")):	# 引数なしもしくはファイルがない場合、ファイルを作成する
	location = "Yokohama-shi,jp"
	mode = "json"
	metric = "metric"
	url = "http://api.openweathermap.org/data/2.5/forecast?q={a}&mode={b}&units={c}&APPID={d}".format(a=location, b=mode, c=metric, d=api_key)
	response = urllib2.urlopen(url)
	line = response.readline() #内容を取得
	# print(type(line)) # 型はstr型
	weather_data = json.loads(line)
	json.dump(weather_data, open("weather.json","w"), ensure_ascii=False)
	# print(type(weather_data)) # 型はdict型
	#pprint.pprint(weather_data) # インデントして出力
elif argv[1]=='GET_DATA_FROM_FILE':
	pass # No process
else:
	print("Invalid parameters.")
	sys.exit()

weather = json.load(open('weather.json', 'r'))
pprint.pprint(weather) # インデントして出力

timezone = pytz.timezone("Asia/Tokyo")
#print(type(timezone)) # <class 'pytz.tzfile.Asia/Tokyo'>
#print(timezone) # Asia/Tokyo

term = 24 # [Hour]
part_weather = weather['list'][:term/3]

rain = 0
for item in part_weather:
	icon = item['weather'][0]['icon'][:2]
	if icon=='04' or icon=='09' or icon=='10' or icon=='11' or icon=='13':
		rain = rain+1

#print(commands.getoutput("echo $PATH"))
		
if rain>0:
#	print(rain)
	check = commands.getoutput("/home/pi/aquestalkpi/AquesTalkPi \"雨がふるかもしれません。狸より。\" | aplay")
else:
	check = commands.getoutput("/home/pi/aquestalkpi/AquesTalkPi \"雨はふりません。狸より。\" | aplay")
	
"""
for item in part_weather:
	item_datetime = str(datetime.datetime.fromtimestamp(item['dt'], tz=timezone)) #<type 'datetime.datetime'> -> str
	item_date = item_datetime[5:10]
	item_time = item_datetime[11:13]
	print(item_date),	
	print(item_time),	
	print(item['weather'][0]['icon']),			#<type 'unicode'>
	print(round(item['main']['temp'],0)),	#<type 'float'>
	print(item['main']['humidity']),				#<type 'int'>
	print(item['weather'][0]['description'])	#<type 'unicode'>
	
	print("<tr>")
for item in weather['list']:
	item_datetime = str(datetime.datetime.fromtimestamp(item['dt'], tz=timezone)) #<type 'datetime.datetime'> -> str
	item_date = item_datetime[5:10]
	print("<td>" + item_date + "</td>")
print("</tr>")

print("<tr>")
for item in weather['list']:
	item_datetime = str(datetime.datetime.fromtimestamp(item['dt'], tz=timezone)) #<type 'datetime.datetime'> -> str
	item_time = item_datetime[11:13]
	print("<td>" + item_time + "</td>")
print("</tr>")

print("<tr>")
for item in weather['list']:
	print("<td><img src=images/" + item['weather'][0]['icon'] + ".png></td>")
print("</tr>")

print("<tr>")
for item in weather['list']:
	print("<td>" + str(round(item['main']['temp'],0)) + "</td>")
print("</tr>")

"""






