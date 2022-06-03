# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:26:09 2022

@author: SahleEza
"""

import requests, csv, io, os
from zipfile import ZipFile
import numpy as np
import pandas as pd

# Make sure current directory is here: 
os.chdir('C:\\Users\\SahleEza\\Coding\\statscan_package')

# Save the base URL to a variable
baseurl = 'https://www150.statcan.gc.ca/t1/wds/rest'

# Check to see when the table was updated as at a particular date 
date= '2017-12-07'
changed_date = '{}/getChangedCubeList/{}'.format(baseurl,date)

# Extract Data from a particular table on StatsCan
tableid = '14100287'
extract_data = '{}/getFullTableDownloadCSV/{}/en'.format(baseurl,tableid)

# Create a session and extract data from URL above 
with requests.Session() as s:
    download = s.get(extract_data)
    # Download content
    decoded_content = download.content.decode('utf-8')
    # Read CSV
    csv_obj = csv.reader(decoded_content.splitlines(), delimiter=',')
    csv_list = list(csv_obj)
    # Print rows 
    for row in csv_list:
        print(row)
        
# Extract the link from the list
zip_list = csv_list[0][1].split('"')
zip_link = zip_list[1]

# Request the zip folder from the URL and extract the files from the zip
r = requests.get(zip_link)
z = ZipFile(io.BytesIO(r.content))
z.extractall(os.getcwd())

# Extract the folder name from zip_link
foldername = zip_link.split('/')[-1]

# Extract the file name from the folder name
filename = foldername.split('-')[0] + '.csv'   
print(foldername,filename)

# Convert CSV into a Pandas DataFrame, data types are floats
data = pd.read_csv(filename, dtype='a')
    
    

