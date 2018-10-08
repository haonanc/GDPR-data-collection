# Neal Haonan Chen(hc4pa@virginia.edu)
# University of Virgina
# GDPR project
# 9/10/2018

# This file is used to collect clean plain data with the help of Boilerpipe
# dependency: boilerpipe-python-wraper(https://github.com/misja/python-boilerpipe)
# input: URLs that link to company's current privacy policy
# output: policies in plain texts with html elements removed


from boilerpipe.extract import Extractor

# Parameters
FILE = "master.txt"
OUTPUT_KEYWORD = 'output/'
KEY_WORDS = ['privacy','privacies','policy','policies']
NEGATIVE_KEY_WORDS = ['ru']
START = 2000
END = 10000


file = open(FILE,'r')
log = open("log.txt",'a')   # to store exceptions and handle them in future
found = False
count = 0
title = "Empty"

# a filter that filters out results that do not have given keywors
def check(text,KEY_WORDS,NEGATIVE_KEY_WORDS):
	for word in KEY_WORDS:
		if word in text:
			for nword in NEGATIVE_KEY_WORDS:
				if nword not in text:
					return True
	return False
if 
for line in file:
	if count == END:
		break
	if line[0] == "=":
		if found == False and count >= START:
			print("Critical Error:"+title+" has no url that passed the filter!")
			log.write(title+"\n")
		title = line.strip('\n').strip("=")
		count += 1
		found = False
	else:
		if not found and count >= START:
			if check(line,KEY_WORDS,NEGATIVE_KEY_WORDS):
				output = open(OUTPUT_KEYWORD+title+".txt",'w')
				try:
					extractor = Extractor(extractor='DefaultExtractor', url=line)
					txt = extractor.getText().encode('utf-8')
					print(len(txt))
					if len(txt) > 2500:
						output.write(txt)
						output.close()
						if len(txt) < 4000:
							print("Succeed,collecting another policy:"+title)
							title += "*"
						else:
							found = True
							print("Succeeded:"+title)
				except:
					print("Error:"+title+" request failed")





