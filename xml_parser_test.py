import itertools
import pandas as pd 
import numpy as np
import scipy
import xml.etree.ElementTree as ET
import nltk
from nltk.tokenize import sent_tokenize
import re
from lxml import etree
from io import StringIO, BytesIO

def clean_text(text):
	
	#Use this to remove any special characters and extra whitespaces
	cleaned_text = re.sub(r"\s+", " ", text)
	return cleaned_text.strip()

def extract_data_availability_statements(xml_file):
	#XML parsing with Element- works only for BioC xmls
	tree = ET.parse(xml_file)
	root = tree.getroot()



	#Textparsing

	article_text = ''
	for element in root.iter():
		if element.text is not None:
			article_text += element.text

	cleaned_text = re.sub('<.*?>', '', article_text)
	#cleaned_text = clean_text(cleaned_text)

	sentences = sent_tokenize(cleaned_text)
	data_availability_statements = []

	keywords = ["data availability", "data sharing", "availability statement", "availability of data"]

	for sentence in sentences:
		for keyword in keywords:
			if keyword in sentence.lower():
				data_availability_statements.append(sentence)
				break
	return data_availability_statements




xmlpath = "/Users/muthuku/Desktop/final_xmls/49.nxml"
statements = extract_data_availability_statements(xmlpath)
print(statements)