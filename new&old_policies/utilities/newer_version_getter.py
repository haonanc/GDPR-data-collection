# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu
# GDPR Project
# 6/5/2018

# This script uses Bing Search API get the URLs linked to the companies' current privacy policy.
# It generates a file with all URLs collected
# Input: list of companies
# Output: current policies in raw html files.

from pws import Bing # Bing Search API; install it by open terminal and enter "pip install pws"

#configuration
NAME_OUTPUT_FILE = "urls_new_polices2.txt"
NAME_ERRPR_LOG =  "log.txt"
KEYWORD = ' privacy policy' # Keyword we use to search
NUM_WEBSITES = 1000 # We only search top 1000 websites
START_FROM = 500
NUM_RESULT = 5 # We only store top 5 results from Bing search
NUM_MAX_ATTEMPTS = 5 # Maxium attempts allowed during search

#Variables
urls = []
search_result = []
search_failed = []

def filter(input_list):
    temp = list()
    for item in input_list:
        temp.append(item["link"])
    for i in range(0, NUM_RESULT):
        if (temp[i].find("Policy") == -1 and temp[i].find("policy") == -1 and temp[i].find("Policies") == -1and temp[i].find("policies") == -1 and temp[i].find("privacy") == -1 and temp[i].find("Privacy") == -1):
            if (i == NUM_RESULT - 1):
                print(temp, "got removed, because it did not pass the keyword filtering test")
            continue
        else:
            return temp[i]

file = open("websites.txt","r")
count = 0
for line in file:

    count = count + 1
    if count < START_FROM:
        continue
    urls.append(line.split()[1])
    if count == NUM_WEBSITES:
        break
total = len(urls)
a = 0
for item in urls:
    if(item == "Hidden"):
        continue
    x = 0
    while(x < NUM_MAX_ATTEMPTS):
        try:
            temp = Bing.search(item + KEYWORD, NUM_RESULT, 0)
            print(temp)
            search_result.append(filter(temp["results"]))
            a = a + 1
            print("Progress:",a,"/",total)
            break
        except:
            x = x+1
    if(x == NUM_MAX_ATTEMPTS):
        a = a + 1
        print("Progress:" , a , "/" , total)
        print(item + "--failed")
        search_failed.append(item)
file1 = open(NAME_OUTPUT_FILE, "w")
for url in search_result:
    file1.write(str(url) + '\n')
file2 = open(NAME_ERRPR_LOG, "w")
for url in search_failed:
    file2.write(str(url) + '\n')
print("Finished")


