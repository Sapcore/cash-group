import csv
# open text file for reading using 'windows-1251' encoding
# name should be '3.txt.' (probably not the best approach)
inf = open('3.txt', 'r', encoding='windows-1251')

# write all the rows into list
mlist = []

for line in inf:
    mlist.append(line.replace('\n', '').replace('\xa0', ''))


# keywords:
ro = 'Расшифровка операций'
pnss = 'Продолжение на следующей странице'
dom = 'ДАТА ОПЕРАЦИИ (МСК)'
vvs = 'В валюте счёта'
npages = mlist.count(pnss)

# cut intro part, prepare for HEAD and BODY
csv_prep = mlist[mlist.index(ro) + 1:]

# create header
csv_header = csv_prep[:csv_prep.index(vvs) + 1]

# delete header and new pages headers
csv_prep = csv_prep[csv_prep.index(vvs) + 1:]
for _ in range(npages - 1):
    csv_prep = csv_prep[:csv_prep.index(pnss)] + csv_prep[csv_prep.index(vvs) + 1:]
csv_prep = csv_prep[:csv_prep.index(pnss)]

# create body
csv_body = []
for i in range(0, len(csv_prep) - 8, 9):
    csv_body.append(csv_prep[i:i + 9])

# ________________________________________________________________________________________________________________
# create header with 'date', 'money', 'contractor', 'reference'
# change body accordingly

csv_real_header = ['date', 'money', 'contractor', 'reference']
csv_real_body = []
for row in csv_body:
    csv_real_body.append([row[0], row[-3], row[-4], row[-5]])

# create csv
csv_name = 'SberFiz.csv'
with open(csv_name, 'w', newline='', encoding='windows-1251') as file:
    writer = csv.writer(file)
    writer.writerow(csv_real_header)
    writer.writerows(csv_real_body)
