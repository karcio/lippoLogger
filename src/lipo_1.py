'''
Created on 26 Nov 2014

@author: crystal
'''
import csv
from datetime import datetime
import os


os.system('clear')

def insertData():
    name = input('Insert lipo name - ')
    number = int(input('Insert lipo number - '))
    start_Volt = float(input('Insert start voltage - '))
    end_Volt = float(input('Insert end voltage - '))
    comma = ","
    print('Inserted success ...')
    print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()), name, comma, number, comma, start_Volt, comma, end_Volt)

    with open('lipologger.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()), name, number, start_Volt, end_Volt])

def openCsv ():
        with open('lipologger.csv') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                print(', '.join(row))
                
def errhandler():
    print ('your input has not been recognised')
    
print ('===> Lipo battery logger <===')
x = input('For insert data select [1], for view data select [2] ')

if x == '1':
    insertData()
elif x == '2':
    openCsv()
else:
    errhandler()