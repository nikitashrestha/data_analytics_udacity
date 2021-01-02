import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def show_null_rows(df, column_name):
  # Returns list of records having null value in a given column
  bool_series = pd.isnull(df[column_name])

  return df[bool_series]

def visualize_data(type, df, x_col=None, y_col=None):
  # Plots different types of graphs based on parameters passed
  if type=="scatter":
    ax = sns.scatterplot(data=df,x=x_col,y=y_col)
    plt.show()
  elif type=="box":
    sns.set_theme(style="whitegrid")

    if y_col is None:
      ax = sns.boxplot(x=df[x_col])
      plt.show()

      return
    ax = sns.boxplot(x=x_col, y=y_col,data=df)
    plt.show()
  elif type=='heatmap':
    sns.heatmap(df.corr(), cmap="YlGnBu", annot = True)
    plt.show()
  else:
    raise ValueError("Unsupported visualization format")

def print_summary(df):
  # Prints the overall summary of your dataset
  print ("\n------Basic summary of Dataframe------\n")
  print(df.info())
  print("\n")
  print("-------Summary Statistics on Numeric Values in Dataframes------\n")
  print(df.describe())