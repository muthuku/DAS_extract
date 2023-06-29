import os
import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml_directory(directory):

	xml_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.nxml')]
	data = []


	for xml_file in xml_files:
		try:
			tree = ET.parse(xml_file)
			root = tree.getroot()
			print(root)

			for article in root.findall('article'):
				title = article.find('.//article-title').text
				authors = [author.find('name').text for author in article.findall('.//contrib[@contrib-type="author"]')]
				pmid = article.find('.//article-id[@pub-id-type="pmid"]').text
				data_availability_elem = article.find('.//notes[@notes-type="data-availability"]/p')

				if data_availability_elem is not None:
					data_availability = data_availability_elem.text
				else:
					data_availability = ''
				data.append({'Title': title, 'Authors': ', '.join(authors), 'PubMed ID': pmid, 'Data Availability': data_availability})

		except Exception as e:
			print(f"Error processing XML file: {xml_file}")
			print(f"Error message: {str(e)}")
			continue
	
	df = pd.DataFrame(data)
	return df



xml_directory = '/Users/muthuku/Desktop/final_xmls/Pragati2023/xml2022_Bioc'
df_2 = parse_xml_directory(xml_directory)

print(df_2)