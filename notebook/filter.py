# filter.py

import csv

'''
Global variables
'''
source_data = 'Tianxia.csv' #This is the path to your data file. Change it to your case!
read_encoding = 'utf8'
write_encoding = 'utf8'

'''
Open the data file
'''
csvfile = open(source_data,'rt',encoding=read_encoding,newline='')

reader = csv.reader(csvfile)

all_groups = []

'''
Jump over the 1st line. Uncomment this line if your first line is the titles.
'''
#reader.__next__() 

for row in reader:
    group_values = row[12].split(';')
    for category in group_values:
        category = category.strip() #strip off the leading and trailing blanks
        if category not in all_groups:
            all_groups.append(category)

'''
Close the file
'''
csvfile.close()

all_groups.sort()

print('All distinct groups:(total {} groups)'.format(len(all_groups)))
for c in all_groups:
    print(c)