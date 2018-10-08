# Neal Chen
# University of Virginia
# hc4pa@virginia.edu

# This is a simple python program that takes an URL and then prints the HTML to the console.

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, http.cookiejar

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36')]
urllib.request.install_opener(opener)
url = input("Enter the URL")
print("Please wait")
page = urllib.request.urlopen(url)
html = page.read()
html = html.decode("UTF-8")
soup = BeautifulSoup(html, "lxml")
print(html)


