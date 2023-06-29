import os
import xml.etree.ElementTree as ET
import pandas as pd
from lxml import etree
from io import StringIO, BytesIO

def parse_xml_directory(directory):

	xml_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.nxml')]
	print(xml_files)
	data = []
	urls = []


	for xml_file in xml_files:
		parser = etree.XMLParser(remove_comments=True)
		tree = etree.parse(xml_file)
		root = tree.getroot()

		nsmap = root.nsmap
		nsmap['ext'] = 'http://www.w3.org/1999/xlink'

		for article in root.xpath('//article'):
			title = article.xpath('//article-title/text()')[0]
			pmid = article.xpath('//article-id/text()')[0]
			data_availability = article.xpath('.//sec[@sec-type = "data-availability"]/p/text()')
			
			data_availability_elems = article.xpath('.//sec[@sec-type = "data-availability"]')
			if data_availability_elems:
				data_availability_elem = data_availability_elems[0]
			else:
				data_availability_elem = None
			
			if data_availability_elem is not None:
				links = data_availability_elem.xpath('.//ext:link[@xlink:type="uri"]', namespaces=nsmap)
				for link in links:
					href = link.get('{http://www.w3.org/1999/xlink}href')
					if href:
						urls.append(href)
			else:
				data_availability = ''
			data.append({'Title': title, 'PubMed ID': pmid, 'Data Availability':data_availability , 'URLS': urls})

	
	df = pd.DataFrame(data)
	return df, urls



xml_directory = '/Users/muthuku/Desktop/final_xmls'
df_2, url_list = parse_xml_directory(xml_directory)
df_2.to_csv("fail1.csv")