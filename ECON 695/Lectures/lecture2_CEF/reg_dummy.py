# Replicate reg_dummy.do 

import pandas as pd 
import os 
os.getcwd() # get current working directory
os.chdir("./Dropbox/UW695/lectures/2_CEF_BLP") # change working directory

temp = pd.read_stata("citytemp.dta")
print(temp.head())

# with constant
import statsmodels.formula.api as smf
model1  = smf.ols("tempjuly ~ C(region, Treatment(reference='West'))", data=temp).fit(cov_type='HC1')
print(model1.summary())

# no constant: all categories included 
model2  = smf.ols("tempjuly ~ 0 + C(region)", data=temp).fit(cov_type='HC1')
print(model2.summary())
