import glob
import csv

csvfiles = glob.glob('C:\Users\student\PycharmProjects\project_music\crawling\*.csv')
wf = csv.writer(open('C:\Users\student\PycharmProjects\project_music\crawling\DB.csv','wb'),delimiter = ',')

for files in csvfiles:
    rd = csv.reader(open(files,'r'),delimiter=',')
    rd.next()
    for row in rd:
        wf.writerow(row)