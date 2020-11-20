"""LINEAR REGRESSION IN PYTHON
Exxon-Mobile stock price vs. Oil barrel price: is there a relationship?



$ python3 -m venv env
$ source env/bin.activate
$ pip install [pandas, matplotlib, statsmodels, sklearn,


"""
#
#
#
### [1] IMPORT THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import math
import pickle

from IPython.display import display #?
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from scipy import stats
from scipy.stats import kurtosis, skew
# %matplotlib inline









#
#
#
### [2a] LOAD THE DATA
#--The path to our data source file (excel file):
path = r"oil_exxon.xlsx" #'r' for raw-string method (single \)
#--Create DataFrame object:
price_data = pd.read_excel(path)
#--Set index to date, not index nums (but check that it is true datetime format)
price_data.index = pd.to_datetime(price_data['date'])
#--Drop old date col
price_data = price_data.drop(['date'], axis=1)
#--Check data (print first 5 rows)
# print(price_data.head())


#
#
#
### [2b] CHECK DATA TYPES
# print(price_data.dtypes) #=> 'float64', 'float64'



#
#
#
### [3] CLEAN UP DATA
#--Define the new name:
new_col_names = {'exon_price':'exxon_price'} # 1 col was mispelled...
#--Rename the column (only renames ones included in dict{} passed in)
price_data = price_data.rename(columns = new_col_names)
# print(price_data.head()) # another check



#
#
#
### [4] HANDLE MISSING VALUES IN DATA
    # Two thoughts: fillna() to fill in missing values, or
    # dropna() to simply drop those places in the data.
#--Check for missing values:
# print(price_data.isna().any()) # gives a summary: does a col have NA values? (True if some NA)
#--Drop NA values
price_data = price_data.dropna() # can set a threshold (if x missing values, drop; else...)
# print(price_data.isna().any()) # now all 'False' (no NA values anywhere)


#
#
#
### [5] VISUALIZE THE DATA
#--Define the X/Y data (to graph the data to see overall picture):
x = price_data['exxon_price'] # col of dataframe obj
y = price_data['oil_price']
#--Create the scatterplot:
plt.plot(x,y, 'o', color = 'cadetblue', label='Daily Price') # ,plot(x,y, 'marker', color)
#--Scatterplot formatting...:
plt.title('Exxon Stock vs. Oil Price')
plt.xlabel('Exxon Mobile')
plt.ylabel('Oil Barrel')
plt.legend()
# plt.show() # creates a window w/ scatterplot


### [6] MEASURE THE CORRELATION:
#--Call .corr(), which gives back another DataFrame w/ the metrics
print(price_data.corr())
""" What is the correlation between these axes?:
             exxon_price  oil_price
exxon_price      1.00000    0.60132
oil_price        0.60132    1.00000
 => 0.60 is a definite relationship, almost a 'strong' one
"""

### [7] STATISTICAL SUMMARY
print(price_data.describe()) # populates a new data_frame, with each col being exxon_price and oil_price, and the rows being different metrics: count, mean, std, min, max...
    # Think (and analyze)– does anything seem an outlier?
    # Not really... everything within 3 STDs...
"""
       exxon_price    oil_price
count  1248.000000  1248.000000
mean     84.802796    61.935000
std       7.424687    19.288424
min      68.120003    26.010000
25%      80.190002    48.162500
50%      83.024998    57.120000
75%      88.529999    70.725000
max     104.379997   115.190000
"""

#
#
#
### [8] CHECK FOR OUTLIERS / SKEWNESS
price_data.hist(color = 'cadetblue')
plt.show()
    # Data: maybe a slight skew? Let's get a number on it.

#--Calculate excess kurtosis using Fisher-method:
exxon_kurtosis = kurtosis(price_data['exxon_price'], fisher=True) #fisher method: want kurtosis closer to 0 (more 'normal')
oil_kurtosis = kurtosis(price_data['oil_price'], fisher=True)
#--Calculate the skew:
exxon_skew = skew(price_data['exxon_price'])
oil_skew = skew(price_data['oil_price'])
#--Display the calculations:
display(f"Exxon kurtosis: {exxon_kurtosis:.2}")
display(f"Oil kurtosis: {oil_kurtosis:.2}")
display(f"Exxon skew: {exxon_skew:.2}")
display(f"Oil skew: {oil_skew:.2}")
"""
Exxon kurtosis: 0.088       => Good enough
Oil kurtosis: 0.53          => Good enough
Exxon skew: 0.66            => Fine (mod. skew)
Oil skew: 1.0               => Ehh.. (right at cut-off)
    We could perform a kurtosis/skew test...
"""
#--Kurtosis test: (measures 'pointiness')
display('Exxon')
display(stats.kurtosistest(price_data['exxon_price']))
display('Oil')
display(stats.kurtosistest(price_data['oil_price']))
""" => Reveals a degree of kurtosis.
BUT: is it significant? (the larger your dataset grows, the likelier kurtosis/skew are to happen)... but to what degree/magnitude?
"""
#--Skew test: (skewed toward + or - values)
display('Exxon')
display(stats.skewtest(price_data['exxon_price']))
display('Oil')
display(stats.skewtest(price_data['oil_price']))
"""
Again- reveals there IS skew... but to what degree?
    It might still be in normal range...
Oil skew alone was iffy...
"""


"""EXTENDED NOTES:
KURTOSIS:
    - any distribution w/ kurtosis=3 is mesokurtic (normal distribution)
    - any distribution w/ kurtosis<3 is platkurtic. Tails are shorter and thinner, and often its central peak is lower and broader.
    - any distribution w/ kurtosis>3 is leptokurtic. Tails are longer and fatter, and often its central peak is higher and sharper.
SKEWNESS:
    - if skewness is less than -1 or greater than +1, the distribution is highly skewed.
    - if skewness is between -1 and -1/2 OR +1/2 and +1, its distribution is moderately skewed.
    - if skewness is between -1/2 and +1/2, its distribution is approx. symmetric.

"""







### [9] BUILD THE MODEL
#--Define the input & output variable
Y = price_data.drop('oil_price', axis = 1) # only want 'Exxon mobile' col/series
X = price_data[['oil_price']] # different method to do same as line above (but opposite)

#--Split X and y into X_
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=1) #convention is to save 20-30% of the data for testing purposes.. the rest for training

#--Create a linear regression model object:
regression_model = LinearRegression()
#--Pass thru the X_ and Y_-train dataset
regression_model.fit(X_train, y_train)


### [10] EXPLORE THE OUTCOME
        # y = β₀ + β₁x
intercept = regression_model.intercept_[0] #returns array, get 1st instance
coefficient = regression_model.coef_[0][0] #returns nested list
print(f"Coefficient is {coefficient:.2}, intercept is {intercept:.4}.")
#
"""INTERPRETING THE COEFFICIENT:
coef=0.24 => We would say that a single unit increase in oil is associated with (not causal!) a 0.24 increase in Exxon-Mobile stock price.
intercept=70.01
    -> Now we can 'build the line'
"""


### [11] PREDICTIONS
#--A single prediction (pass in a random value in a double array [[]] ).
prediction = regression_model.predict([[67.33]])
predicted_value = prediction[0][0]
print(f"Predicted value for 67.33: {predicted_value:.4}")
""" INTERPRETING PREDICTION:
We would say 'given a barrel of oil at a price of 67.33, we would predict Exxon Mobile to be trading at a price of 85.95.'
    -> How can we evaluate this prediction?
"""

#--Multiple predictions:
    # Using the test dataset we put aside... get a list of predictions!:
y_predict = regression_model.predict(X_test)
#--Show first 5 predictions:
print(y_predict[:5])
""" =>
[[82.23530265]
 [82.87451035]
 [81.48245802]
 [78.9256272 ]
 [84.01324704]]
"""


### [12] EVALUATING THE MODEL:
#--Define our input:
X2 = sm.add_constant(X) # X=input
#--Create a OLS model
model = sm.OLS(Y, X2) #output, input
#--Fit the Data:
est = model.fit()

#--Make some confidence intervals, 95% by default
    # B/c we aren't taking entire pop. of data, we can't be absolutely certain. We are saying, 'with 95% confidence we are saying the true coefficient exists somewhere in this range.'
print(est.conf_int())
"""
                  0         1
const      69.358126  71.57579
oil_price   0.214372   0.24856
    ->'With 95% confidence, our coefficient is somewhere in the range of 0.21<>0.24 (this is only sample data, not the sum-total pop. Only so confident.)'
- Want a narrower range: decrease confidence
- Want a wider range: increase confidence
"""

### [13] HYPOTHESIS TESTING:
"""
- Null hypothesis: there is no relationship between the price of oil and price of exxon stock (coefficient equals 0)
- Alternative hypothesis: there is a relationship (coefficient does not equal 0)
    -> If we reject the null, we are saying there is a relationship and the coef != 0.
We want to disprove the null hypothesis, since the coefficient is not equal to 0.
"""
print(est.pvalues)
    # Disregard constant
    # oil_price = reallyyyy small number (almost 0)
"""
oil_price    1.423529e-123
- The p-value represents the probability that the coefficient equals 0. We want a p-value that is less than 0.05.
    - If it is, we can reject the NULL HYPOTHESIS.
    -> Our pvalue is far lower than 0.05.
=> There IS a relationship (association, not causal), we believe it to be between oil price and stock price.
"""



### [14] MODEL FIT
    # How well our data fits the model: a few metrics...
    # Compare predictions to actual (residuals):
# Mean Absolute Error (MAE): mean of the abs. value of the error (magnitude, but not direction (high or low)).
# Mean Squared Error (MSE): more popular b/c it punishes larger errors.
# Root Mean Squared Error (RMSE): square root of the mean of the squared errors. Even more favored bc it allows us to interpret the output in y-units.

#-- Calculate the MSE:
model_mse = mean_squared_error(y_test, y_predict)
#--Calc the MAE:
model_mae = mean_absolute_error(y_test, y_predict)
#--Calc the RMSE:
model_rmse = math.sqrt(model_mse)
#--Display the outputs
print(f"MSE:{model_mse:.3},\nMAE:{model_mae:.3},\nRMSE:{model_rmse:.3}.")

"""
MSE: 38.4
MAE: 5.03
RMSE: 6.2
"""


### [15] # R-SQUARED:
# A goodness of fit metric. The higher the r-squared, the better the data fits our model.
    # R-squared is simply the square of the correlation (from earlier).
model_r2 = r2_score(y_test, y_predict)
print(f"R-squared: {model_r2:.2}")
    # r-squared = 0.31. Meaning, our data explains 31% of the variance.
# is this good? bad? for complex matters (the domain you are working in), even .3-.4 is good (psychology, stocks...)
# How to improve r-squared?
    # Add more cols of data to the model (features)
# ADJUSTED R-SQUARED: penalized for more complex models (more features tends to drive up r2 in any case... but it doesn't always mean it is correct/helping the model)

### [16] SUMMARY OF MODEL OUTPUT
print(est.summary())
"""
OLS Regression Results
==============================================================================
Dep. Variable:            exxon_price   R-squared:                       0.362
Model:                            OLS   Adj. R-squared:                  0.361

Method:                 Least Squares   F-statistic:                     705.7
Date:                Thu, 19 Nov 2020   Prob (F-statistic):          1.42e-123
Time:                        22:40:01   Log-Likelihood:                -3992.3
No. Observations:                1248   AIC:                             7989.
Df Residuals:                    1246   BIC:                             7999.
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         70.4670      0.565    124.678      0.000      69.358      71.576
oil_price      0.2315      0.009     26.565      0.000       0.214       0.249
==============================================================================
Omnibus:                       61.541   Durbin-Watson:                   0.024
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               31.074
Skew:                          -0.198   Prob(JB):                     1.79e-07
Kurtosis:                       2.337   Cond. No.                         218.
==============================================================================
"""


### PLOTTING THE RESIDUALS
    # How many times were we off by this much, &c. &c.
(y_test - y_predict).hist(grid = False, color="royalblue")
plt.title("Model Residuals")
plt.show


### PLOTTING OUR LINE ON A GRAPH
#--Plot outputs:
plt.scatter(X_test, y_test, color="gainsboro", label="Price")
plt.plot(X_test, y_predict, color="royalblue", linewidth=3, linestyle='-', label='Regression Line')
plt.title("Linear Regression Model Exxon vs. Oil")
plt.xlabel('Oil')
plt.ylabel('Exxon Mobile')
plt.legend()
plt.show()
#--Coefficients



### SAVE THE MODEL FOR FUTURE USE
    # stores model in a pickle which is a python object (a bytestream)
#--Pickle the trained model (don't re-train it everytime you need to make predictions!!)
with open('my_linearRegression.sav', 'wb') as f:
    pickle.dump(regression_model, f)
#--Load it back in:
with open('my_linearRegression.sav', 'rb') as f:
    regression_model_2 = pickle.load(f)
#--Make a new prediction from newly loaded model:
print(regression_model_2.predict([[67.33]]))



#
