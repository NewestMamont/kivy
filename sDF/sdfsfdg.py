import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as Model
from sklearn.metrics import mean_absolute_percentage_error,mean_squared_error
from joblib import dump,load
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler as SC
from sklearn.neighbors import KNeighborsRegressor as REG

df = pd.read_csv('hfhfhfhfhfhf.csv')
df.info()
x = df.drop('House price of unit area', axis = 1)
y = df['House price of unit area']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)
sc = SC()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
reg = REG(n_neighbors=5)
reg.fit(x_train,y_train)

dump(reg, 'Regression.joblib')

y_pred = reg.predict(x_test)
print(mean_absolute_percentage_error(y_test, y_pred))
print(mean_squared_error(y_test, y_pred))

plt.scatter(x_test[: ,-1], y_test)
plt.scatter(x_test[: ,-1],y_pred,color = 'red')
plt.show()