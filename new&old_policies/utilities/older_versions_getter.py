# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu
# GDPR Project
# 6/5/2018

# This file uses regular expression to fetch URLs linked to companies' past privacy policies on WayBack Machine.
# It generates a file with all URLs collected
# Input: list of companies
# Output: past policies in raw html files, fetched from WayBack Machine (https://archive.org/web/)
import urllib.request,urllib.parse,http.cookiejar
import re

def urlencode(str):
  return urllib.parse.quote_plus(str)

#config
REG_EX = "\d{14}" ## capture all 14 digits string
EARLIST_CAPTURE = "20180401000000" ## format: year/month/day/hour/minute/second
INPUT_FILE = "urls_new_polices.txt"
NAME_ERRPR_LOG =  "log2.txt"
OUTPUT_FILE = "urls_old_policies.txt"

#variables
to_search = [] # url to search
search_result = [] # contains the search result
error_log = []  # log that contains errors
prefix="https://web.archive.org/__wb/calendarcaptures?url="
prefix_2 = "https://web.archive.org/web/"


try:
    file = open(INPUT_FILE, "r")
    for line in file:
        to_search.append(line)
except:
    print("Not able to open file")

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36')]
urllib.request.install_opener(opener)
# Set up header for the crawler

a = 0
file = open(OUTPUT_FILE, "w")
file2 = open(NAME_ERRPR_LOG, "w")
for item in to_search:
    print(a,"/",len(to_search))
    a = a+1
    encoded = urlencode(item)  ## encode originial url to URL format
    url = prefix + encoded + "&selected_year=2018"  ## make new url
    try:
        page = urllib.request.urlopen(url)
        html = page.read()
        html = html.decode("UTF-8")
        pattern = re.compile(REG_EX)
        matches_s = re.findall(pattern, html)
        if (len(matches_s) != 0):
            if (matches_s[0] > EARLIST_CAPTURE):
                print(item, " skipped, because no result found early than", EARLIST_CAPTURE)
                file2.write(url)
            else:
                url = prefix_2 + matches_s[0] + "/" + item
                search_result.append(url)
                file.write(url)
    except:
        print("An error occured with url:" + url)

print("finished")

