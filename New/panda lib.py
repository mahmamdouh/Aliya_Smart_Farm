import pandas as pd
import openpyxl
import xlsxwriter

# define data as a dictionary
data = ({"language": [ "Python", "C-Sharp", "Javascript","PHP"] ,
         "avg_salary": [120, 100, 120, 80],
          "applications": [10,15,14,20]})

# Create a Pandas DataFrame out of a Python dictionary
df = pd.DataFrame.from_dict(data)
# look at the Data
df.head()
df.to_excel("languages.xlsx") 