import statsmodels.api as sm

def train_regression_model(x_train, y_train):
  X = sm.add_constant(x_train)
  model = sm.OLS(y_train, X).fit()

  return model

def test_regression_model(x_test, model):
  X = sm.add_constant(x_test)
  pred = model.predict(X)

  return pred