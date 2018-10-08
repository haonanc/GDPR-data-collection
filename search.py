# Neal Haonan Chen(hc4pa@virginia.edu)
# University of Virginia
# GDPR Project
# 9/15/2018

# Given the names of companies, this script utilizes yandex_search API to crawl the URLs that link to companies' privacy policies.
# Input: list of companies
# Output: list of urls that link to those companies' privacy policies.
# Dependency: yandex_search; need to set up your account on yandex search engine

import yandex_search
import datetime
import time

# Parameters
FILE_NAME = "sites"    # name of input file
NUM_OF_RESULTS = 5     # number of results kept for each search
OUTPUT_FILE_NAME = "output" # name of output file
KEYWORD =" Privacy Policy" # keyword to search; format = company_name + keyword
START = 8000 # start with # of company   
END = 8500 # terminate when reaches # of company 
API_KEY = ""


count = 0
file = open(FILE_NAME+".txt",'r')
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
output = open(OUTPUT_FILE_NAME+st+".txt",'w')
yandex = yandex_search.Yandex(api_user='nealchen', api_key=API_KEY)

for line in file:

	if count == END:
		break
	count += 1
	if count < START:
		continue
	if line.split()[1] == "Hidden":
		continue
	output.write("====="+str(count)+" "+line.split()[1]+"====="+"\n")
	try:
		results = yandex.search("'"+line.split()[1]+KEYWORD+"'").items
		print("Request#" + str(count) + " succeeded:" + line.split()[1])
	except:
		print("Request failed:" + line.split()[1])
	for i in range(NUM_OF_RESULTS):
		output.write(str(results[i]['url'])+"\n")

