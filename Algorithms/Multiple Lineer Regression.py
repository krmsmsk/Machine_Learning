import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.2f' % x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

df = pd.read_csv("Machine Learning/datasets/advertising.csv")

X = df.drop('sales', axis=1) #Bağımlı değişkeni çıkarıyoruz ki X değişkeninde sadece bağımsız değişkenler olsun.
y = df[["sales"]] #y değişkenine de bağımlı değişkenimizi atıyoruz.

# Model Kurma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1) #X ve y değişkenlerimizi alıp, test setinin boyutunu %20, train setinin boyutunu da %80 yaparak rastgele bir örneklem oluştur dedik.
## random_state 'i 1 aldık ki hocanın verileriyle aynı rassallığa sahip veriler ile çalışalım. 17 de verebilirdik.

reg_model = LinearRegression().fit(X_train, y_train) # Modeli train setinin bağımlı ve bağımsız değişkenleri üzerinden kur dedik.

# Tahmin
# Aşağıdaki gözlem değerlerine göre satışın beklenen değeri nedir?

# TV: 30
# radio: 10
# newspaper: 40

# 2.90 = b
# 0.04 , 0.17 , 0.002 = w

# Model Denklemi : Sales = 2.90 + (TV*0.04) + (radio*0.17) + (newspaper*0.002)

2.90 + (30*0.04) + (10*0.17) + (40*0.002) #5.88 çıktı.

# Fonksiyonlaştırma ########
yeni_veri = [[30], [10], [40]]
yeni_veri = pd.DataFrame(yeni_veri).T

reg_model.predict(yeni_veri)
############################

# Tahmin Başarısının Değerlendirilmesi
y_pred = reg_model.predict(X_train)
np.sqrt(mean_absolute_error(y_train, y_pred))
# Train hatamız 1.15 çıktı

# Train R-Kare
reg_model.score(X_train, y_train) # %90 çıktı. Bu şu demek, modele yeni değişkenler eklediğimizde (bir öncekini doğrusal reg. yapmıştık) açıklama oranımız arttı.

# Test RMSE (Önemli olan budur)
y_pred = reg_model.predict(X_test) # X yani bağımsız değişkenlerin test setini verip bağımlı değişkeni yani y 'yi tahmin ettiriyoruz.
np.sqrt(mean_absolute_error(y_test, y_pred)) # Bağımlı değişkenin yani y 'nin test değişkeni zaten elimizde vardı, bununla yeni tahmin ettirdiğimiz y_pred 'i karşılaştırıyoruz. Hata ortalamasını alıyoruz.
## Test hatamız 1.09 çıktı. Train hatasından daha düşük çıktı. İyi bir şeydir. Normalde train hatasının daha düşük çıkar.

# Test R-Kare
reg_model.score(X_test, y_test) # %90 çıktı.

### Biz burada train setinde modelimizi kurduk. Test setinde hatamızı değerlendirdik. Bu yüzden Test setinde başarı değerlendirmesi yapılır.


# 10 Katlı CV (Cross Validation) RMSE
np.mean(np.sqrt(-cross_val_score(reg_model, X, y, cv=10, scoring="neg_mean_squared_error"))) #scoring bize negatif ortalama hatayı verir. Bu yüzden başa - yazdık. Negatifle çarpmış olduk. 1.69 hata skoru aldık.