import itertools
import pandas as pd 
import numpy as np
import scipy
import urllib.request

df1 = pd.read_csv('/Users/muthuku/Desktop/Pragati2023/pmids2022.txt')

list_data = df1.values.tolist()
print(list_data)


num = 0
for i in list_data:
	pmid = i[0]
	print(pmid)
	num = num + 1
	link = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/" + str(pmid) + "/unicode"
	try:
		f= urllib.request.urlopen(link)
	except urllib.error.HTTPError as http_err:
		print("Error: %s" % http_err)
	else:
		myfile = f.read()
		print(myfile)
		with open('/Users/muthuku/Desktop/Pragati2023/xml2022_Bioc/' + str(pmid) + '.xml', 'wb') as fo:
			fo.write(myfile)