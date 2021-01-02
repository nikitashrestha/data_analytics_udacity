import sys
import pandas as pd

from regression import model as m
from regression import preprocessing as prp
from utils.files import read_file_S3
from utils.conversion import convert_byte_to_df

def recommend_bid(pred_price):
  bid_amount = sum(pred_price)*0.7

  print("The recomended bidding for the diamond set will be: {0}".format(bid_amount))

def main():
  training_data = read_file_S3('diamond-price-prediction','training_dataset/diamonds.csv')
  testing_data = read_file_S3('diamond-price-prediction', 'testing_dataset/new-diamonds.csv')

  train_df = convert_byte_to_df(training_data)
  test_df = convert_byte_to_df(testing_data)

  x_train,x_test = train_df[['carat','cut_ord','clarity_ord']], test_df[['carat','cut_ord','clarity_ord']]
  y_train = train_df['price']  
  
  trained_model = m.train_regression_model(x_train, y_train)
  y_pred = m.test_regression_model(x_test, trained_model)

  print(trained_model.summary())
  print("\n\n")
  recommend_bid(y_pred)
  

if __name__=='__main__':
  main()