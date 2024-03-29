#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import json
import time
import urllib
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

class config:
	key = "7e28492c103df7e2c388e8847409d002" #go to https://numverify.com/



def main():

	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']




		print (color.BLUE + "[+] " + color.END + "Information Output")
		print ("--------------------------------------")
		print (" - Phone number: " +str(number))
		print (" - Country: " +str(country_code))
		print (" - Country Name: " +str(country_name))
		print (" - Location: " +str(location))
		print (" - Carrier: " +str(carrier))
		print (" - Device: " +str(line_type))
	else:
		print ("[TRACKER] Usage:")
		print ("./%s <phone-number>" % (sys.argv[0]))
		print ("./%s +919867498544" % (sys.argv[0]))

main()