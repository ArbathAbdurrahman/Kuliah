import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data_cars.csv")

reg = LinearRegression()
reg.fit(df[['x1','x2']].values,df.y)

LinearRegression()

a = reg.intercept_
b = reg.coef_
print('\nintercept = ', a)
print('Koefisien regresi = ', b[0], ' dan ', b[1])
X_baru =np.array([13, 107]).reshape(1,2)
prediksi_Y = reg.predict(X_baru)
print('Hasil prediksi untuk x1=8 dan x2=125 yaitu ',prediksi_Y)
print('\n\n\n\n')


mpl.rcParams['legend.fontsize'] = 12
fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
ax.scatter(df.x1, df.x2, df.y)
ax.legend()
ax.view_init(45, 0)
plt.show()
