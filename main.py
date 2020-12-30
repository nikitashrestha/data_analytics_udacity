from utils.files import read_file_S3
from utils.conversion import convert_byte_to_df

def main():
  data = read_file_S3('diamond-price-prediction','training_dataset/diamonds.csv')

  df=convert_byte_to_df(data)
  print(df.isnull()==True)
  

if __name__=='__main__':
  main()