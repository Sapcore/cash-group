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
1. Run the 'main.py' script with all the necessary data files located in the same directory as the script files
_________________________________________________________
ToDo:
1. Edit 'source_combiner.py' so the keywords list would be read from separate file
2. Maybe it is not necessary to extract interim .csv's but extract the 'grouped_cabbage' only
3. Otherwise, Tin_Fiz.csv should also be extracted.
4. Maybe it is a good idea to combine 'to_csv_sber_yur.py' and 'to_csv_mdl_yur.py' into one script, but I like the idea of separate scripts for separate files (for now)
