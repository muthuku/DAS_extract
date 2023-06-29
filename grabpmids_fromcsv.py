import itertools
import pandas as pd 
import numpy as np
import scipy
import urllib.request

def grab_PMIDs_from_csv(source_file, target_file):
	'''
	Function to extract URLs from a DataFrame column and save them to a target file.
    
    Parameters:
        - source_file (str): Path to the source file (CSV) containing the URLs.
        - target_file (str): Path to the target file (TXT) where the extracted URLs will be saved.
       '''
	# Read the source file
	df1 = pd.read_csv(source_file)
	# Extract the URLs from the DataFrame
	extracted_PMID = df["official_url"].str[-8:]

	# Remove empty strings and drop NaN values
	extracted_PMID.replace('', np.nan, inplace=True)
	extracted_PMID.dropna(inplace=True)
	# Save the extracted URLs to the target file
	extracted_PMID.to_csv(target_file, header=None, index=None)


'''
df1 = pd.read_csv('/Users/muthuku/Desktop/2022_CSHL_IR_articles.csv')
df2 = df1["official_url"].str[-8:]

df2.replace('', np.nan, inplace=True)
df2.dropna(inplace =True)

print(df2)

df2.to_csv('/Users/muthuku/Desktop/Pragati2023/pmids2022.txt', header=None, index=None)
'''