import csv
# open text file for reading using 'windows-1251' encoding
# name should be '1.txt.' (probably not the best approach)
inf = open('1.txt', 'r', encoding='windows-1251')

# write all the rows into list
mlist = []

for line in inf:
    mlist.append(line.replace('\n', ''))

# create list for 'СекцияДокумент=Платежное поручение' only
# if other sections: 'СекцияРасчСчет' and 'СекцияДокумент=Платежное требование' are important,
# see previous code versions or write additional rows
index_pp = mlist.index('СекцияДокумент=Платежное поручение')
mlist_pp = mlist[index_pp:]

# work with Platezhnoe Poruchenie section
# first step: create template for .csv containing full data from the source
# second step: .csv columns are to be changed as per the customer's request

# _______________step 1________________
# create csv header
start_i = 1
stop_i = mlist_pp.index('КонецДокумента')
plat_poruch_head = []
for i in range(len(mlist_pp[start_i: stop_i])):
    # fill head values with left part of split rows for the defined string slice
    plat_poruch_head.append(mlist_pp[start_i: stop_i][i].split('=')[0])

# create csv body
plat_poruch = []
while stop_i <= len(mlist_pp):
    templist = []
    for i in range(len(mlist_pp[start_i: stop_i])):
        templist.append(mlist_pp[start_i: stop_i][i].split('=')[-1])
    plat_poruch.append(templist)
    # '+2' is necessary because of start-end cells of each block
    start_i, stop_i = stop_i + 2, 2 * stop_i - start_i + 2

# _______________step 2________________
# create header with 'date', 'money', 'whopays', 'whogets', 'reference'
# change body accordingly

csv_real_header = ['date', 'money', 'whopays', 'whogets', 'reference']
csv_real_body = []
for row in plat_poruch:
    csv_real_body.append([row[1], row[2], row[5], row[14], row[-1]])

# create csv
csv_name = 'SberYur.csv'
with open(csv_name, 'w', newline='', encoding='windows-1251') as file:
    writer = csv.writer(file)
    writer.writerow(csv_real_header)
    writer.writerows(csv_real_body)
