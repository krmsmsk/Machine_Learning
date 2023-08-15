# Sales Prediction with Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv("Machine Learning/datasets/advertising.csv")
df.shape #200 gözlem değeri, 4 değişken olduğunu gördük.

X = df[["TV"]] #TV değişkenini X 'e atadık.
y = df[["sales"]] #sales değişkenini y 'ye atadık.

# Model Kurma

reg_model = LinearRegression().fit(X, y)

# Sabit (b = Bias = intercept)
reg_model.intercept_[0] #Sıfır demezsek bize array olarak çıktı verir.

# TV 'nin katsayısı (w1 = coef)
reg_model.coef_[0][0]


# Tahmin
# 150 birimlik TV harcaması olursa ne kadar satış olması beklenir?

reg_model.intercept_[0] + reg_model.coef_[0][0]*150 #14 birimlik satış olması beklenir.

# Modelin Görselleştirilmesi
g = sns.regplot(x=X, y=y, scatter_kws={'color': 'b', 's': 9}, ci=False, color="r") #Güven aralığını False yaptık. Güven aralığı vermeyecek.
g.set_title(f"Model Denklemi: Sales = {round(reg_model.intercept_[0], 2)} + TV*{round(reg_model.coef_[0][0], 2)}") #Buralardaki 2 'ler virgülden sonra iki basamak al demektir. Round foksiyonuyla kullanılır. Round fonksiyonu sayıyı yuvarla demektir.
g.set_ylabel("Satış Sayısı")
g.set_xlabel("TV Harcamaları")
plt.xlim(-10, 310) #x ekseni için -10 'dan başla 310 'a kadar git dedik. (grafikte bu kısmı gösterecek)
plt.ylim(bottom=0) #y ekseni sıfırdan başlamalı dedik.
plt.show()


# Tahmin Başarısı

y_pred = reg_model.predict(X) #X değerleri üzerinden y yi tahmin ettirdik.

mean_squared_error(y, y_pred) #Ortalama hata (MSE) - Hata skorumuz.

y.mean() #Ortalama 14 birim satış var.
y.std() #5 standart sapmamız.
#Ortalama hata 10 çıkmıştı, bunun çok büyük bir hata olduğunu yorumladık.


# RMSE
np.sqrt(mean_squared_error(y, y_pred)) #Hata skorumuz.

# MAE
mean_absolute_error(y, y_pred) #Hata skorumuz.

# R-Kare Değeri : Veri setindeki bağımsız değişkenlerin, bağımlı değişkeni açıklama yüzdesidir.
reg_model.score(X, y) # Çıkan sonuçta, bu modeldeki bağımsız değişkenler (TV) bağımlı değişkeni (satışlar) %61 oranında açıklayabilir deriz.