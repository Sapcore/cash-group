# cash-group
 Group cash flow data provided by 4 different sources

Necessary data:
1. File named "1.txt" - Sber yur extract in .txt format
2. File named "2.txt" - Mdk yur extract in .txt format
3. File named "3.txt" - Sber fiz extract in .txt format (export .pdf as 'plain text')
4. File named "4.csv" - Tin fiz extract in .csv format

Stored files:
1. 'to_csv_sber_yur.py' - python script switching .txt to .csv and keeping columns of interest only (sber yur source)
2. 'to_csv_mdl_yur.py' - python script switching .txt to .csv and keeping columns of interest only (mdl yur source)
3. 'to_csv_sber_fiz.py' - python script switching .txt to .csv and keeping columns of interest only (sber fiz source)
4. 'source_combiner.py' - python script combining all four sources in one dataframe (assuming that the 4th source is already in .csv) and grouping them based on the                           keywords list
5. 'main.py' - python master-script running all the scripts above

How to run:
1. run the 'main.py' script with all the necessary data files located in the same directory as the scipt files
