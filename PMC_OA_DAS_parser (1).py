import os
import xml.etree.ElementTree as ET
import pandas as pd
from lxml import etree
from io import StringIO, BytesIO

def parse_xml_directory(directory):

	xml_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.nxml')]
	print(xml_files)
	data = []



	for xml_file in xml_files:

		parser = etree.XMLParser(remove_comments=True)
		tree = etree.parse(xml_file)
		root = tree.getroot()

		# data_availability_sec_elems = root.xpath(".//*[local-name()='sec'][@sec-type='data-availability']")
		# for data_availability_elem in data_availability_sec_elems:
		# 	links = data_availability_elem.xpath(".//*[local-name()='ext-link'][@xlink:type='uri']/@xlink:href")
		# 	for link in links:
		# 		print(link)

		for article in root.xpath('//article'):


			title = article.xpath('//article-title/text()')[0]
			pmid = article.xpath('//article-id/text()')[0]
			DOI = article.xpath('//article-id[@pub-id-type = "doi"]/text()')
			PMC = article.xpath('//article-id[@pub-id-type = "pmc"]/text()')
			abstract = article.xpath('//abstract/p/text()')
			data_availability_notes = article.xpath('.//notes[@notes-type="data-availability"]/p/text()')
			data_availability_sec = article.xpath('.//sec[@sec-type = "data-availability"]/p/text()')

			data_availability_sec_elem = root.xpath('.//sec[@sec-type="data-availability"]')
			for elem in data_availability_sec_elem:
				if elem.text and elem.text.strip():
					content = elem.text.strip()
					print(content)

			#nsmap = {"xlink": 'http://www.w3.org/1999/xlink'}
			#url_links_sec = article.xpath(".//sec[@sec-type='data-availability']//*[local-name()='ext-link' and @xlink:type='uri']/@xlink:href")
			data_availability_meta = article.xpath('//custom-meta-group/custom-meta[meta-name[contains(text(), "Data Availability")]]/meta-value/text()')

			# urls =[]
			# nsmap = root.nsmap
			# nsmap['ext'] = 'http://www.w3.org/1999/xlink'

			# data_availability_sec_elem = article.xpath(".//sec[@sec-type='data-availability']")
			# if data_availability_sec_elem is not None:
			# 	links = data_availability_sec_elem.xpath('.//ext:link[@xlink:type="uri"]', namespaces=nsmap)
			# 	print(links)
				# for link in links:
				# 	href = link.get('{http://www.w3.org/1999/xlink}href')
				# 	if href:
				# 		urls.append(href)
				# print(urls)

		data.append({'Title': title, 'PubMed ID': pmid, 'PMC': PMC, "Abstract":abstract, 'Data Availability 1': data_availability_notes, 'Data Availability 2': data_availability_sec, "Data Availability 3" : data_availability_meta})

	
	df = pd.DataFrame(data)
	return df



xml_directory = '/Users/muthuku/Desktop/final_xmls'
df1 = parse_xml_directory(xml_directory)

print(df1)
