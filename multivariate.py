import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt  
from pandas.tools.plotting import scatter_matrix
import statsmodels.api as sm
import statsmodels.formula.api as smf
loansDatafull = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv')
loansDatafull = loansDatafull.rename(columns={'Monthly.Income': 'Annual.Income'})
loansDatafull['Annual.Income'] *= 
loansDatafull.dropna(inplace=True)
loansDatafull['Interest.Rate'] = loansDatafull['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
int_rate = loansDatafull['Interest.Rate']
annual_inc = loansDatafull['Annual.Income']
y = np.matrix(intrate).transpose()
x1 = np.matrix(annual_inc).transpose()
X = sm.add_constant(x1)
model = sm.OLS(y,X)
f = model.fit()
print f.summary()
loansDatafull['home_ownership'] = pd.Categorical(loansDatafull['Home.Ownership']).codes
x2 = np.matrix(loansDatafull['home_ownership']).transpose()
x = np.column_stack([x1, x2])
X = sm.add_constant(x)
model2 = sm.OLS(y, X)
f = model.fit()
f.summary()
print("The coefficient of annual income doubles")
model3 = smf.ols(formula='int_rate ~ annual_inc * home_ownership', data=loansDatafull).fit()
model3.summary()
print("The interaction effect of annual income and home ownership seems to have much more predictive value of interest rates than the two separated.")
