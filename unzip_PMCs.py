import os
import shutil
import tarfile
import zipfile

def extract_files(folder_path):
	# folder_path : path where all zipped PMC.tar.gz files exist 
	#loop through tar.gz files within folder
	for file_name in os.listdir(folder_path):
		#generate a file path with folder path and file name
		file_path = os.path.join(folder_path, file_name)
		#check if file ends with tar.gz and extract file contents 
		if file_name.endswith('.tar.gz'):
			with tarfile.open(file_path, 'r') as tar_ref:
				tar_ref.extractall(folder_path)
		os.remove(file_path)


def get_nxml(source_folder, target_folder, file_extension):
	#make target folder if it doesn't already exist 
	if not os.path.exists(target_folder):
		os.makedirs(target_folder)
	# loop through each PMC folder and make path to folder 
	for folder_name in os.listdir(source_folder):
		folder_path = os.path.join(source_folder, folder_name)
		if os.path.isdir(folder_path):
			#loop through each file and if file ends with .nxml, move to output folder
			for file_name in os.listdir(folder_path):
				file_path = os.path.join(folder_path, file_name)
				if file_name.endswith(file_extension):
					shutil.move(file_path, target_folder)

source_folder = '/Users/muthuku/Desktop/testPMC_OA'
target_folder = '/Users/muthuku/Desktop/final_xmls'
file_extension = '.nxml'




#folder = '/Users/muthuku/Desktop/testPMC_OA'
#extract_files(folder)
#get_nxml(source_folder,target_folder,file_extension)