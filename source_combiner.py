import pandas as pd
import csv

# ________________________work with the 1st source (sber_yur)________________________
# add 1 additional 'source' column
df1 = pd.read_csv('SberYur.csv', encoding='windows-1251')
df1['source'] = 'Сбер юр'

# ________________________work with the 2nd source (mdl_yur)________________________
# add 1 additional 'source' column
df2 = pd.read_csv('MdlYur.csv', encoding='windows-1251')
df2['source'] = 'Мдл юр'

# ________________________work with the 3rd source (sber_fiz)________________________
# create 'whopays' and 'whogets' columns based on 'money' sign
# delete sign from 'money' column
# create 'source' column
# delete 'contractor' column
df3 = pd.read_csv('SberFiz.csv', sep=',', encoding='windows-1251')
df3['whopays'] = df3.apply(lambda row: row.contractor if '+' in row.money else 'ООО "ЛАЙМСТОУН"', axis=1)
df3['whogets'] = df3.apply(lambda row: row.contractor if '+' not in row.money else 'ООО "ЛАЙМСТОУН"', axis=1)
df3['money'] = df3.apply(lambda row: row.money if '+' not in row.money else row.money[1:], axis=1)
df3['money'] = df3.apply(lambda row: float(row.money.replace(',', '.')), axis=1)
df3['source'] = 'Сбер физ'
df3 = df3.drop(columns=['contractor'])

# ________________________work with the 4th source (tin_fiz)________________________
# it is assumed that Tin_Fiz data is presented in .csv format and, therefore,
# no additional "to_csv" script is necessary
df4_raw = pd.read_csv('4.csv', sep=';', encoding='windows-1251')
# create new filtered df
df4 = df4_raw[['Дата платежа', 'Сумма платежа', 'Описание', 'Категория']].copy()
# rename columns
df4 = df4.rename(columns={'Дата платежа': 'date',
                          'Сумма платежа': 'money',
                          'Описание': 'descr',
                          'Категория': 'reference'})
# create 'whopays' and 'whogets' columns based on 'money' sign
# create 'source' column
# delete sign from 'money' column
# delete 'description' column
df4['whopays'] = df4.apply(lambda row: row.descr if '-' not in row.money else "ООО 'ЛАЙМСТОУН'", axis=1)
df4['whogets'] = df4.apply(lambda row: row.descr if '-' in row.money else "ООО 'ЛАЙМСТОУН'", axis=1)
df4['source'] = 'Тинь физ'
df4['money'] = df4.apply(lambda row: row.money if '-' not in row.money else row.money[1:], axis=1)
df4['money'] = df4.apply(lambda row: float(row.money.replace(',', '.')), axis=1)
df4 = df4.drop(columns=['descr'])

# ________________________ work with all source (combine) ________________________
# combine all DFs, change datetype in order to sort by date correctly
# shorten the "OOO" abbreviation
df = pd.concat([df1, df2, df3, df4])
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
df = df.sort_values('date')
df['whopays'] = df.apply(lambda row: row.whopays.replace('ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ', 'ООО'), axis=1)
df['whogets'] = df.apply(lambda row: row.whogets.replace('ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ', 'ООО'), axis=1)

# ________________________ start grouping ________________________
# enter the keywords
# create list with sub-dfs
# fill the list in case if keyword matches the payment reference (case insensitive)
# delete these rows from initial df
# as result, initial df should contain 'other' payments only
cabbage = df.copy()
key_words = ['зачисление', 'аренд', 'комунал', 'комисси', 'зар', 'хоз', 'рекла', 'страховые']
grouped_cabbage = []
for word in key_words:
    try:
        grouped_cabbage.append(cabbage[cabbage['reference'].str.contains(word, case=False)])
        cabbage = cabbage.drop(grouped_cabbage[-1].index)
    except:
        continue

# export df in .csv
# create empty file
# fill the file in cycle with sub-dfs and add the keyword (prior)
# add the 'other' group

with open('grouped_cabbage.csv', 'w', newline='', encoding='windows-1251') as file:
    writer = csv.writer(file)

for i in range(len(key_words)):
    with open('grouped_cabbage.csv', 'a', newline='', encoding='windows-1251') as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow([key_words[i].capitalize()])
    grouped_cabbage[i].to_csv('grouped_cabbage.csv', index=False, mode='a', encoding='windows-1251')

with open('grouped_cabbage.csv', 'a', newline='', encoding='windows-1251') as file:
    writer = csv.writer(file)
    writer.writerow([])
    writer.writerow(['Разное'])

cabbage.to_csv('grouped_cabbage.csv', index=False, mode='a', encoding='windows-1251')
