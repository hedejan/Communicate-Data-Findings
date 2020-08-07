# import all packages required to read, download and save dateset
import pandas as pd
import glob, os, io
import requests as r
import zipfile as zip

# create a folder name
mydir = 'trip_data_files'

# create the folder to which all data will be saved in
os.makedirs(mydir, exist_ok=True)

# loop to read from links by month
for month in range(1,13):
    month_string = str(month)
    month_leading_zero = month_string.zfill(2)
    
    bike_data_url = 'https://s3.amazonaws.com/fordgobike-data/2018' + month_leading_zero + '-fordgobike-tripdata.csv.zip'
    response = r.get(bike_data_url)
        
    # code below opens zip file; BytesIO returns a readable and writeable view of the contents;
    unzipped_file = zip.ZipFile(io.BytesIO(response.content))
        
    # puts extracted zip file into folder trip_data_files
    unzipped_file.extractall(mydir)

# concat all csv files into a single DataFrame
list_csvs = []
for file_name in os.listdir(mydir):
    list_csvs.append(pd.read_csv(mydir+'/'+file_name))
df = pd.concat(list_csvs)

# save all data to a new csv
df.to_csv('data.csv', index=False);