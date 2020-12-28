from utils.files import read_file_S3

def main():
  data = read_file_S3('diamond-price-prediction','training_dataset/diamonds.csv')
  print(data)


if __name__=='__main__':
  main()