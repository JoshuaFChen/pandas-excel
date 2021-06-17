import openpyxl
import pandas as pd

df = pd.read_excel(r"c:\temp\book2.xlsx")

print(df.info())
outfile = r'c:\temp\output.csv'
with open(outfile, 'w', encoding="utf-8") as outfile:
    for index, row in df.iterrows():
        zi_column = str(row['zi'])
        yin = str(row['yin'])
        if zi_column != 'nan' and zi_column:
            zi_list = zi_column.split(',')
            for zi in zi_list:
                outfile.write(f"{zi.strip()} {yin}\n")


