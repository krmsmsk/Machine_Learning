import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import missingno as msno
from datetime import date
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler


#Verisetimizi yüklüyoruz.
def load():
    data = pd.read_csv("../datasets/diabetes.csv")
    return data


#Verisetini çağırıp, ilk 5 değerini gözlemliyoruz.
df = load()
df.head()


#Kategorik ve Numerik değişkenlere göre sınıfladırıyoruz.
def grab_col_names(dataframe, cat_th=10, car_th=20): #10'dan az eşsiz değer varsa "benim için" kategoriktir. 20 'den fazla sınıf sayısı varsa cardinaldir diye hesaplama yaptık.

    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"] #Değişkenin tipi object ise kategoriktir.
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"] #İlgili değişkendeki eşsiz değer sayısına bak, eğer belirlediğimiz cat_th den küçük ise ve tipide object değilse numerik görünümlü kategorik değişkendir.
    #Uçak sınıfı 1,2,3 gibi
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"] #Tipi object ve car_th 'si eşsiz değerden büyük olanlar categorik görünümlü cardinal değişkenlerdir. Ör: İsim Soyisim gibi
    cat_cols = cat_cols + num_but_cat #cat_cols listemizi güncelledik. num_but_cat 'leri ekledik.
    cat_cols = [col for col in cat_cols if col not in cat_but_car] #kategorik ama kardinal olmayanları da cat_cols listesine ekledik.

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"] #Object olmayanları seçtik
    num_cols = [col for col in num_cols if col not in num_but_cat] #numerik görünümlü kategorikleri çıkardık.

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_by_car = grab_col_names(df)
## Böylece verisetimizde 768 Gözlem değeri, 9 değişken, 1 kategorik, 8 numeric ve 1 tane de numeric görünümlü kategorik değişken olduğunu öğrendik.


# AYKIRI GÖZLEM ANALİZİ #

def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75): #Vahit hoca "q1=5 / q2 =95" yada "q1=1 / q2 =99" olabilir dedi.
    quartile1 = dataframe[col_name].quantile(q1) #q1 'i tanımladık.
    quartile3 = dataframe[col_name].quantile(q3) #q3 'ü tanımladık.
    interquantile_range = quartile3 - quartile1 #iqr 'ı hesapladık.
    up_limit = quartile3 + 1.5 * interquantile_range #üst limit
    low_limit = quartile1 - 1.5 * interquantile_range #alt limit
    return low_limit, up_limit #ileride kullanmak için bu limitleri return ettik.

outlier_thresholds(df, "Age")


low, up = outlier_thresholds(df, "Age") #Yaş değişkeninin alt ve üst sınır değerlerini değişkenlere atadık.

df[(df["Age"] < low) | (df["Age"] > up)].head() #Aykırı değerlerin ilk beşini getirdik.

def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name) #Yukarıda ki fonksiyona low ve up limitleri hesaplatıp, değişkenlere atadık.
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None): #Aykırı değer var mı? Varsa;
        return True
    else: #Yoksa;
        return False


check_outlier(df, "Age") #Böylece Age değişkeninde aykırı değer var mı görebildik.


for col in num_cols:
    print(col, check_outlier(df, col)) #Az önce elle yazdığımız age sütünunda aykırı değer var mı? kodunu, formülize ettik ve nümerik kolonlarda aykırı değer var mı diye bakabildik.


# Aykırı Değerlerin Kendilerine Erişmek

def grab_outliers(dataframe, col_name, index=False): #index istemiyoruz başta. Daha sonra fonksiyonu çağırırken parantez içinde 3. değer yerine True yazabiliriz.
    low, up = outlier_thresholds(dataframe, col_name)
    if dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].shape[0] > 10:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].head()) #shape 'i 10 dan büyükse ilk 5 gözlem değerini getir.
    else:
        print(dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))]) #değilse hepsini getir.


    if index:
        outlier_index = dataframe[((dataframe[col_name] < low) | (dataframe[col_name] > up))].index
        return outlier_index


grab_outliers(df, "Age") #Age sütununda aykırı değerlerin hangileri olduğunu getirdik.

# EKSİK GÖZLEM ANALİZİ #

def missing_values_table(dataframe, na_name=False):
    na_columns = [col for col in dataframe.columns if dataframe[col].isnull().sum() > 0]
    n_miss = dataframe[na_columns].isnull().sum().sort_values(ascending=False)
    ratio = (dataframe[na_columns].isnull().sum() / dataframe.shape[0] * 100).sort_values(ascending=False)
    missing_df = pd.concat([n_miss, np.round(ratio, 2)], axis=1, keys=['n_miss', 'ratio'])
    print(missing_df, end="\n")

    if na_name:
        return na_columns

missing_values_table(df)

## Böylece verisetimizde eksik gözlem olmadığını gördük.



