import tabula 
import pandas as pd

pdf_file = "C:\Users\neelp\Downloads\breach_report.pdf"
excel_file= "C:\Users\neelp\Downloads\output_1.xlsx"

df = tabula.read_pdf(pdf_file, output_format="dataframe", pages='all') 

# Clean up column names

df.columns = [col.strip() for col in df.columns]


# Remove unnecessary spaces

df = df.applymap(lambda x: str(x).strip() if isinstance(x, str) else x)

df.to_excel(excel_file, index=False) 
