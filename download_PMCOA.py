import itertools
import pandas as pd 
import numpy as np
import scipy

import urllib.request
import os

def download_PMC(source_file, output_folder):

	'''
	Function to download files from a list of URLs and save them to a destination folder.
    
    Parameters:
        - source_file (str): Path to the file containing the URLs.
        - output_folder (str): Path to the folder where the downloaded files will be saved.
    '''

	# Read the file containing the URLs
	df1 = pd.read_csv(source_file)
	# Extract the URLs from the DataFrame
	urls = df1["File"]
	# Create the destination folder if it doesn't exist
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	
	# Loop through each URL and download the file

	for url in urls:
		link = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/" + str(url)
		file_name = os.path.basename(link)
		destination_path = os.path.join(output_folder, file_name)
		urllib.request.urlretrieve(link, destination_path)

download_PMC('/Users/muthuku/Desktop/Pragati2023/output1_2022_PMC.csv', "test")


'''
base_url = "https://ftp.ncbi.nlm.nih.gov/pub/pmc"

df = pd.read_csv('/Users/muthuku/Desktop/Pragati2023/output1_2022_PMC.csv')

df1 = df["File"]
print(df1)

for i in df1:
	link = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/" + str(i)
	destination_folder = "/Users/muthuku/Desktop/testPMC_OA"
	file_name = os.path.basename(link)
	destination_path = os.path.join(destination_folder, file_name)
	urllib.request.urlretrieve(link, destination_path)
'''

