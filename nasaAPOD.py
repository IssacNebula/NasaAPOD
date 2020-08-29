#!/usr/bin/python2
import requests
import json
import random
import os, sys

'''
need API Key from https://api.nasa.gov/
'''




def welcome():
	print("#"*25)
	print("#\tNasa APOD\t#")
	print("#"*25)
	print("\nnasaAPOD.py -k 'apikey' -[ h | r ]\n")
	print("\t-h\tHelp panel")
	print("\t-r\tRandom Day")
	print("#"*25)
	print("\n\nExemple :")
	print("\t nasaAPOD.py -k dHcONxPz7************************ -r")
	print("\t nasaAPOD.py -k dHcONxPz7************************ 2019-1-9")
	print("\t nasaAPOD.py -k dHcONxPz7************************ 1999-6-9")
	print("#"*25)


def get(key,date):
	url = requests.get("https://api.nasa.gov/planetary/apod?date=" + date + "&api_key="+key)
	js = json.loads(url.text)

	if js.get('hdurl'):
		hd = js["hdurl"]
	else:
		hd = "Not Disponible !"
	print("#"*50)
	print("\nKey   : " + key)
	print("date  : " + date)
	print("url   : " + js["url"])
	print("hdurl : " + hd + "\n")
	print("#"*50)
	os.system("wget " + js["url"])



def randomDay():
	days = random.randint(1,28)
	month = random.randint(1,12)
	years =random.randint(1999,2019)

	Day = str(years) + "-" + str(month) + "-" + str(days)
	return Day







if sys.argv[1] in ["-h", "--help", "-help"]:
	welcome();

elif sys.argv[1] in ["-k", "-key"]:

	if sys.argv[3] in ["-r", "-random"]:
		get(sys.argv[2],randomDay())
	else:
		get(sys.argv[2],sys.argv[3])
else:
	welcome();

