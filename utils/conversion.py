import pandas as pd
from io import StringIO

def convert_byte_to_df(byte_obj):
  s = str(byte_obj,'utf-8')
  
  data = StringIO(s)
  df = pd.read_csv(data)

  return df