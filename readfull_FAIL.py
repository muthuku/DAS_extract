import itertools
import pandas as pd 
import numpy as np
import scipy
import urllib.request
#Although read_full does compile- grab articles from the doi website, it is in a badly structured XML format that is not able to be parsed using element, maybe another parser may work
df1 = pd.read_csv('/Users/muthuku/Desktop/Pragati2023/2022_CSHL_IR_articles.csv')

df2 = df1["id_number"]

print(df2)

count = 0
for i in df2:
	count = count + 1
	link = "https://doi.org/" + str(i)
	try:
		f= urllib.request.urlopen(link)
	except urllib.error.HTTPError as http_err:
		print("Error: %s" % http_err)
	else:
		myfile = f.read()
		print(myfile)
		with open('/Users/muthuku/Desktop/Pragati2023/htmls2022/' + str(count) + '.html', 'wb') as fo:
			fo.write(myfile)