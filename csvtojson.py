import csv , json
import re
import pandas as pd 

file1 = csv.DictReader(open('data/Ftp_County_Data.csv', 'r'))
data = pd.read_csv('data/Ftp_County_Data.csv')
# new data frame with split value columns 
new = data["upload_time"].str.split(" ", n = 1, expand = True) 
  
# making seperate first name column from new data frame 
data["upload_date_sep"]= new[0] 
  
# making seperate last name column from new data frame 
data["upload_time"]= new[1] 
  
# Dropping old Name columns 
data.drop(columns =["upload_date"], inplace = True) 

data.to_csv('data/final.csv')

file2 = csv.DictReader(open('data/final.csv', 'r'))

output =[]
for each in file2:
    row = {}
    row['datetime'] = each['upload_date_sep']
    row['county'] = each['County']
    row['status'] = each['is_download_completed']
    row['uploadstatus'] = each['is_upload_completed']
    row['connectiontype'] = each['Connection_Type']
    row['timeofupload'] = each['upload_time']
    row['number_of_files_extracted'] = each['number_of_files_extracted']
    row['number_of_files_uploaded'] = each['number_of_files_uploaded']
    output.append(row)

json.dump(output,open('new_file.js','w'),indent=4,sort_keys=False)
original_file = open('new_file.js', 'r+')
original_file = original_file.read()
original_file = re.sub('"(.*?)"(?=:)', r'\1', original_file)
data_file = "var dataSet = "+original_file+";"
# write the data to a json file
f= open("data.js","w+")
f.write(data_file)