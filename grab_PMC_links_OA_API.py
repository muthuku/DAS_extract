import itertools
import pandas as pd 
import numpy as np
import scipy

def isolate_rows_by_PMID(source_file, database, output_file):
	'''
    Function to isolate rows from a DataFrame based on PMIDs and save the result to a CSV file.
    
    Parameters:
        - source_file (str): Path to the source file containing the PMIDs.
        - target_file (str): Path to the target file to save the isolated rows.
        - data_file (str): Path to the data file (CSV) containing the rows to be isolated.
	'''
	# Read the source file containing the PMIDs
	df_pmids = pd.read_csv(source_file)
	# Read the data file
	df_database = pd.read_csv(database)
	# Convert the PMIDs to a list and convert type to integers

	pmid_list = df_pmids['PMIDs'].astype(int).tolist()
	# Isolate the rows based on PMIDs

	isolated_rows = df_database[df_database['PMID'].isin(pmid_list)]
	# Save the isolated rows to a new CSV file

	isolated_rows.to_csv(output_file, index=False)

isolate_rows_by_PMID('/Users/muthuku/Desktop/Pragati2023/pmids2022.txt', '/Users/muthuku/Desktop/Pragati2023/oa_file_list.csv', 'output1_2022_PMC.csv')



'''

df = pd.read_csv('/Users/muthuku/Desktop/Pragati2023/pmids2022.txt')
df2 = pd.read_csv('/Users/muthuku/Desktop/Pragati2023/oa_file_list.csv')
list_data = df.values.tolist()

print(list(df2.columns))

isolated_rows = []
for i in list_data:
	pmid = i[0]
	pmid_int = int(pmid)
	rows = df2[df2['PMID'] == pmid_int]
	isolated_rows.append(rows)

isolated_df = pd.concat(isolated_rows)

isolated_df.to_csv('output1_2022_PMC.csv', index=False)
'''