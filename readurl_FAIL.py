import itertools
import pandas as pd 
import numpy as np
import scipy
import urllib.request
from urllib.request import Request, urlopen
import requests

link = "https://doi.org/10.1007/978-1-0716-2768-6_12"
#req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
f= urllib.request.urlopen(link)
myfile = f.read()
print(type(myfile))

with open('/Users/muthuku/Desktop/Pragati2023/htmls/my_file.html', 'wb') as fo:
	fo.write(myfile)

#r = requests.get(link)
#print(r.text)