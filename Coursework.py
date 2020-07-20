# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:37:19 2019

@author: jessg
"""

#Task 1.1

#create a function called listReader with one input parameter for the filename
#def listReader(filename):
#    #make the csv module available in Python
#    import csv
#    #call the open function with three inputs(parameters): the file name, a space means a new line
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.reader(csvfile)
#        my_list = []
#        for row in reader:
#            my_list.append(row)
#    return my_list
#
#listReader('bl_printed_music_500.csv')

#
#Task 1.2
#import csv
#def dictReader(filename):
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        #print a sample to see what it looks like
#        for row in reader:
#            print(row)
#        #add the reader to memory
#        return reader
##call the dictionary reader function using the name of the csv file as the argument
#dictReader('bl_printed_music_500.csv')    

#
#Task 1.3

#def recordSearch(filename, composer):
#    import csv
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            #if the composer's name appears in the composer column
#            if row['Composer'] == composer:
#                #return the Bl record IDs as tuples as the values are protected
#                return tuple(row['BL record ID'])
##call the dictionary reader function using the name of the csv file and the name of a composer as the two arguments
#recordSearch('bl_printed_music_500.csv', 'Aarons, Alfred E.')
#
#
#Task 1.4
#
#def recordSearch(filename, composer):
#    import csv
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        #create an empty dictionary named data_dict
#        data_dict = {}
#        #if the composer name appears in the composer column, update the dictionary with the key as the composer and the values as the BL record IDs
#        for row in reader:
#            if row['Composer'] == composer:
#                data_dict.update({row['Composer']: row['BL record ID']})
#        return data_dict
##call the dictionary reader function using the name of the csv file and the name of a composer as the two arguments
#dictReader('bl_printed_music_500.csv', 'Hofhaimer, Paul')


#Task 1.5                     

#def valueCounter(filename, column_name, value):
#    import csv
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        count = 0
#        for row in reader:
#            if row[column_name] == value:
#                count += 1
#        return count
#valueCounter('bl_printed_music_500.csv', 'Publisher', 'Penguin Books')


#Task 1.6 

#def countInstances(filename, col, v1, v2, v3):
#    import csv
#    data_dict = {}
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        count_v1 = 0
#        count_v2 = 0
#        count_v3 = 0
#        for row in reader:
#            if row[col] == v1:
#                count_v1+=1
#                data_dict[row[col]] = data_dict.get(row[col],count_v1)
#            elif row[col] == v2:
#                count_v2+=1
#                data_dict[row[col]] = data_dict.get(row[col],count_v2)
#            elif row[col] == v3:
#                count_v3+=1
#                data_dict[row[col]] = data_dict.get(row[col],count_v3)
#    return data_dict
#
#new_dict = countInstances('bl_printed_music_500.csv','Place of publication','London','Milano','New York')
#
#
##Task 1.7 
#    
#import matplotlib.pyplot as plt
#plt.bar(list(new_dict.keys()), list(new_dict.values()))
#plt.show()
       

#Task 1.8

#def countMissing(filename, column_name):
#    import csv
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        count = 0
#        for row in reader:
#            if row[column_name] == "":
#                count += 1
#    return count
#
#countMissing('bl_printed_music_500.csv', 'Composer')

#Task 1.9

#def dateLister(filename):
#    import csv
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        date_list = []
#        for row in reader:
#            if row['Publication date (not standardised)'] == "":
#                date_list.append(row['Publication date (standardised)'])
#            else:
#                date_list.append(row['Publication date (not standardised)'])
#        return date_list
#        
#dateLister('bl_printed_music_500.csv')
    

#Task 1.10

#def percentageCalc(filename, column_name, value):
#    datasize = 0
#    import csv
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        count = 0
#        count_empty = 0
#        for row in reader:
#            if row[column_name] == value:
#                count+= 1
#                datasize+=1
#            elif row[column_name] == '':
#                count_empty+= 1
#                datasize+=1
#            else:
#                datasize+=1
#    #return the value name, the percentage of the dataset for that value without considering empty cells and round the result to 2 decimal points, do the same but considering empty cells
#        return value, round(float(count/datasize * 100),2), round(float(count/(datasize + count_empty) * 100),2)
#                
#percentageCalc('bl_printed_music_500.csv', 'Publication date (not standardised)', '1857')


##Task 1.11
#
#def searchTitle(filename, value):
#    import csv
#    count = 0
#    with open(filename, newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            #if the value appears in the title column
#            if value in row['Title']:
#                count+=1
#            else:
#                print('False')
#        return count
##call the record count function using the name of the csv file and a title as the two arguments
#searchTitle('bl_printed_music_500.csv', 'the')


#Task 1.12

#def getData(c1,c2,c3):
#    import csv
#    templist = [[c1, c2, c3]]
#    with open('bl_printed_music_500.csv', newline='', encoding="utf-8-sig") as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            if row[c1].startswith('A') and row[c2]<'1900' and row[c2]>'1600' and row[c3]!='':
#                templist.append([row[c1],row[c2],row[c3]])
#        return templist
#
#def writeData(c1,c2,c3):
#    data = getData(c1,c2,c3)
#    import csv
#    with open('newdata.csv', 'w+', encoding='utf-8',newline='') as myfile:
#        wr = csv.writer(myfile, delimiter=',')
#        wr.writerows(data)
#
#writeData('Composer','Publication date (standardised)','Place of publication')
        

#3.1 SQL command to create a new database called 'Task3'; create new table...

#CREATE DATABASE "Task3";

#
#CREATE TABLE composers(
#	BL_record_ID INTEGER PRIMARY KEY,
#	Composer VARCHAR(54) NOT NULL, 
#	Composer_life_dates VARCHAR(24), 
#	Title VARCHAR(54) NOT NULL, 
#	Publication_date_standardised INTEGER NOT NULL, 
#	Publication_date_not_standardised INTEGER NOT NULL, 
#	Place_of_publication VARCHAR(24), 
#	Publisher VARCHAR(54)
#)
#
##3.2 SQL command to insert data into the table
#INSERT INTO composers(
#	bl_record_id, composer, composer_life_dates, title, publication_date_standardised, publication_date_not_standardised, place_of_publication, publisher) 
#VALUES (416244, 'S. A.','', 'Short Pieces and Hymn Tunes.', 1915, 1915, 'London', 'Joseph Williams'),
#(4162459, 'Aarons, Alfred E.', '', 'A China Doll. Act i', 1904, 1904, 'New York', 'M Witmark & Sons'),
#(4162460, 'Aarons, Alfred E.', '', 'A China Doll.', 1904, 1904, 'New York', 'M Witmark & Sons'),
#(4162461, 'Aarons, Alfred E.', '', 'The butterfly and the clover.', 1904, 1904, 'New York', 'M Witmark & Sons'),
#(4162494, 'Aarons, Alfred E.', '', 'Its a andy thing to ave about the ouse ... ', 1900, 1900, 'New York, Chicago', 'M Witmark & Sons'),
#(4162495, 'Aarons, Alfred E.', '', 'Rob Roy Tam OShanter OBrien ... [Song.]', 1900, 1900, 'New York, Chicago', 'M Witmark & Sons'),
#(4162510, 'Aarons, Sam', '', 'The East End Aristocracy...', 1907, 1907, 'London', 'London Printing Press'),
#(4162545, 'Abadie, Louis', '', 'LAmoureux de Pontoise.', 1850, 1850, 'Paris', 'F Gauvin'),
#(4162578, 'Abbate, Charles', '', 'Southern Nights. [Song.]', 1915, 1915, 'New York', 'Shapiro, Bernstein & Co'),
#(4162621, 'Abbott, Jane Bingham', '', 'Alone with God. [Song.]', 1903, 1903, 'Chicago', 'C F Summy Co'),
#(4162622, 'Abbott, Jane Bingham', '', 'Just for today. Sacred Song', 1894, 1894, 'Chicago', 'C F Summy Co'),
#(4162651, 'Abdey, Alfred William', '', 'Pam the Wonder-Child.', 1926, 1926,	'London', '"The Stage" Play Publishing Bureau'),
#(4162652, 'Abdey, Alfred William', '', 'Te Deum in G', 1908, 1908, '', ''),
#(4162653, 'Abecket, Percy', '', 'I was there with', 1894, 1894, 'London', 'Francis, Day & Hunter'),
#(4162654, 'Abecket, Thomas', '', 'Columbia, the Gem of the Ocean.', 1948, 1948, 'New York', 'Harold Flammer'),
#(4162611, 'Abbott, Edwin B.', '1881 or 1882-1956', 'Harbour of Dreams …', 1919, 1919, 'Saint Paul, Minn', 'W J Dyer & Bro'),
#(4162612, 'Abbott, Edwin B.', '1881 or 1882-1956', 'Loves Voice divine …', 1919, 1919, 'Saint Paul, Minn', 'W J Dyer & Bro'),
#(4162779, 'Abel, Karl Friedrich', '1723-1787', 	'Six Simphonies ...', 1780,	1780, 'London', 'Printed for the Author'),
#(4162780, 'Abel, Karl Friedrich', '1723-1787', 'Six Simphonies ...' , 1780,	1780, 'London',	'Printed for the Author');
#
##3.3
#SELECT * FROM composers WHERE publication_date_standardised=1900;
#
##3.4
#SELECT * FROM composers WHERE place_of_publication='London' OR place_of_publication='Basel';
#
##3.5
#SELECT COUNT(DISTINCT composer) FROM composers;
#
##3.6
#SELECT AVG(publication_date_standardised) FROM composers;
#
##3.7
#SELECT COUNT(publication_date_standardised) FROM composers WHERE publication_date_standardised=1976;
#
##3.8
#SELECT COUNT(title), publication_date_standardised
#	FROM composers
#	GROUP BY publication_date_standardised;
#    
##3.9
#SELECT * FROM composers WHERE place_of_publication='New York';
#
##3.10
#SELECT * FROM composers WHERE publisher like 'M%';
#
##3.11
#SELECT COUNT(composer_life_dates) FROM composers WHERE composer_life_dates='';
#
##3.12
#UPDATE composers SET place_of_publication='Munich' WHERE bl_record_id=4162652;

#Task 3 Part 2

#Task 3.13 b

#CREATE TABLE publications(
#	record_id INTEGER PRIMARY KEY,
#	title VARCHAR(54) NOT NULL, 
#	publication_date_standardised INTEGER, 
#	publication_date_not_standardised INTEGER
#)
#
#CREATE TABLE publishers(
#	id INTEGER PRIMARY KEY,
#	record_id INTEGER REFERENCES publications(record_id),
#	Place_of_publication VARCHAR(24), 
#	Publisher VARCHAR(54) NOT NULL
#)
#
#CREATE TABLE composers(
#	id INTEGER PRIMARY KEY,
#	record_id INTEGER REFERENCES publications(record_id),
#	Composer VARCHAR(54) NOT NULL, 
#	Composer_life_dates VARCHAR(24) 
#)

#Task4

#Task 4.1

#import psycopg2
#
#import csv
#
#conn = psycopg2.connect("dbname=Task4 user=postgres password=****")
#cursor = conn.cursor()
#
#bl_record_ids, composers, composer_life_dates, titles, publication_dates_standardised, publication_dates_not_standardised, places_of_publication, publishers = [], [], [], [], [], [], [], []
#with open('data_for_sql_task.csv', encoding="utf-8-sig", newline='') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        bl_record_ids.append(row['BL record ID'])
#        composers.append(row['Composer'])
#        composer_life_dates.append(row['Composer life dates'])
#        titles.append(row['Title'])
#        publication_dates_standardised.append(row['Publication date (standardised)'])
#        publication_dates_not_standardised.append(row['Publication date (not standardised)'])
#        places_of_publication.append(row['Place of publication'])
#        publishers.append(row['Publisher'])
#
#cursor.execute('DROP TABLE IF EXISTS data')
#cursor.execute('CREATE TABLE bl_data(id INTEGER PRIMARY KEY, composer TEXT, composer_life_dates TEXT, title TEXT, publication_date_standardised INTEGER, publication_date_not_standardised INTEGER, place_of_publication TEXT, publisher TEXT)')
#
#print(len(bl_record_ids), len(composers), len(titles))
#
#print('INSERT DATA FROM LISTS')
#
#for i in range(len(bl_record_ids)):
#
#
#all_rows = cursor.fetchall()
#for row in all_rows:
#    print(row)


#Task 4.2

#import psycopg2
#
#conn = psycopg2.connect("dbname=Task3 user=postgres password=****")
#cursor = conn.cursor()
#
#cursor.execute('''SELECT COUNT(DISTINCT composer) FROM composers''')
#all_rows = cursor.fetchall()
#
#for row in all_rows:
#    print('{0}'.format(row[0]))
#
#conn.commit()
#conn.close()


#Task 4.3
#
#import psycopg2
#
#conn = psycopg2.connect("dbname=Task3 user=postgres password=****")
#cursor = conn.cursor()
#
#cursor.execute("""SELECT COUNT(composer) FROM composers WHERE composer='Aarons, Sam'""")
#all_rows = cursor.fetchall()
#
#for row in all_rows:
#    print('{0}'.format(row[0]))
#
#conn.commit()
#conn.close()


#Task 4.4

#import psycopg2
#
#conn = psycopg2.connect("dbname=Task3 user=postgres password=****)
#cursor = conn.cursor()
#user_selection = input("Search for a place: ")
#
#cursor.execute('''SELECT COUNT(place_of_publication) FROM composers WHERE place_of_publication = %s''', (user_selection,))
#all_rows = cursor.fetchall()
#
#for row in all_rows:
#    print('{0}'.format(row[0]))
#
#conn.commit()
#conn.close()

#Task 4.5

#import psycopg2
#
#conn = psycopg2.connect("dbname=Task3 user=postgres password=****")
#cursor = conn.cursor()
#user_selection = input("Search for the end of a publisher's name: ")
#search = ('%{}'.format(user_selection), )
#
#for row in all_rows:
#    print('{0}'.format(row[0]))
#
#conn.commit()
#conn.close()
#


