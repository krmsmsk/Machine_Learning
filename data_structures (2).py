# Liste
x = ["btc", "eth", "xrp"]

# Sözlük
x = {"name": "Peter", " Age": 36}

# Tuple
x = ("python", "ml", "ds")

# Set
x = {"python", "ml", "ds"}

# Not : Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python COllections (Arrays) olarakta ifade edilir.

a = 5
b = 10.5

# Sayının karesini almak
a ** 2

# TİP DEĞİŞTİRME

int(b)  # 10.5 'i 10 olarak değiştirdi.
float(a)  # 5 'i 5.0 yaptı.

# Çok satırlı birşeyler yazacak olduğumuzda üç tırnak açarız
long_str = """ Selam
Ben
Kerem"""

name = "John"
name[0]
name[0:2]  # 0 'dan başla, 2 'ye kadar git. 2 dahil değil.

"Kerem" in long_str  # long_str 'nin içinde Kerem var mı? Büyük küçük harf duyarlıdır.

dir(str)  # veri yapısı ile kullanılabilecek metotları getirir.

len(name)  # Kaç karakterden oluştuğunu döndürür.
len("miuul")

# Eğer bir fonksiyon class yapısı içinde tanımlandıysa metot olur. Dışındaysa fonksiyondur. Görevleri aynıdır.

"miuul".upper()  # Bütün karakterleri büyütür
"MIUUL".lower()  # Bütün karakterleri küçültür

hi = "Hello world"
hi.replace("l", "r")  # l 'leri r ile değiştirdi

"Hello world".split()  # Hiçbir değer vermezsek boşlupa göre böler.

" ofofo ".strip()  # Boşlupa göre kırpar
"ofofo".strip("o")  # Sağ ve soldan o harfine gröe kırptı.

notes = [0, 2, 3, 4]
notes.append(100)  # 100 değerini listeye ekledi
notes.pop(0)  # 0. indeksteki veriyi siler
notes.insert(2, 99)  # 2. indekse 99 değerini girer

dictionary = {"REG": "Regression", "LOG": "Logistic Regression", "CART": "Classification and Reg"}
dictionary["REG"]  # Regression sonucunu döndürür
dictionary2 = {"REG": ["RMSE", 10],
               "CART": ["SSE", 30]}
dictionary2["CART"][1]  # CART listesindeki 1. indeksi getirir.
dictionary["REG"] = ["YSA", 10]  # REG 'in içeriğini değiştirdik.

dictionary.update({"RF": 10})  # Eğer RF diye bir tanım varsa onu günceller, yoksa en sona yenisini ekler

t = ("john", "mark", 1, 2)  # tumple
t[0]
t[0] = 99  # Hata verir, tuple 'da veri değiştirilemez.

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1 'de olup set2 'de olmayanlar
set1.difference(set2)  # 5 'i döndürür.
# ya da
set1 - set2

# İki kümedede birbirine göre olmayanlar
set1.symmetric_difference(set2)

# İki kümenin kesişimi
set1.intersection(set2)
# ya da
set1 & set2

# İki kümenin birleşimi
set1.union(set2)

# İki kümenin kesişimi boş mu?
set1.isdisjoint(set2)

# Bir küme diğer kümenin alt kümesi mi?
set1.issubset(set2)

# Bir küme diğer kümeyi kapsıyor mu?
set1.issubset(set2)


# Fonksiyon tanımlama
def calculate(x):
    print(x * 2)


calculate(5)  # x yerine 5 yazdık. 5*2 yapacak


# İki argümanlı/parametreli bir fonksiyon tanımlama
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)


# Docstring
def summer(arg1, arg2):
    print(arg1 + arg2)


def summer(arg1, arg2):
    """

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    """
    print(arg1 + arg2)

    help(summer)
    summer(1, 3)


# Fonksiyon yazma
def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("miuul")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# Girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)

# Ön tanımlı fonksiyon
def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")

say_hi("mrb") # Eğer kullanıcı 'mrb' değerini girmemiş olsaydı, ön tanımlı olan 'Merhaba'yı yazacaktı.


def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)


calculate(98,12,78)


# return ile fonksiyon tanımlama, bu sayede çıktıyı başka bir sayı ile işleme sokabiliriz
def calculate(varm, moisture, charge):
    return (varm + moisture)/charge


calculate(98,12,78)*10



def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture)/charge

    return varm, moisture, charge, output


calculate(98,12,78)


# Fonskiyon içinde fonksiyon çağırma
def standardization(a, p):
    return int(a * 10 / 100 * p * p)


def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


def all_calculate(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculate(3, 5, 7, 10)


# if
if 1 == 1:
    print("something")


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

# elif
def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")


number_check(1)


# for döngüsü
students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student.upper()) # Tüm elemanları büyük harfle yazdık



salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(int(salary * 20/100 + salary)) # Maaşlara %20 zam ekleyerek tüm maaşları getirdik


def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

new_salary(1500, 10) # 1500TL lik maaşa %10 zam uyguladık


for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10)) # Elimizdeki maaş listesindeki 3000TL 'den büyük her bir maaşa %10 zam uyguladık
    else:
        print(new_salary(salary, 20)) # Elimizdeki maaş listesindeki 3000TL 'den küçük her bir maaşa %20 zam uyguladık





def alternating(string):
    new_string = ""
    # Girilen stringin indexlerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfle yaz.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfle yaz.
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("miuul")


# break & continue & while

salaries = [1000, 2000, 3000, 4000, 5000]

# 3000 'e eşit olduğunda dur.
for salary in salaries:
    if salary == 3000:
        break
    print(salary)


# 3000 'e eşit olunca geç, çalışma. Devam et dedik. 3000 hariç hepsini yazar.
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)


# 5 'e kadar yazdır.
number = 1
while number < 5:
    print(number)
    number += 1



students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

    print(A, B)



# divide_students fonsiyonu yazınız.
# Çift indexte yer alan öğrenciler bir listeye,
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olmalı.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

divide_students(students)



def alternating_with_enumarate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumarate("Selam ben Kerem")



# zip
students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["Mat", "Sta", "Phy", "Ast"]
ages = [23, 30, 26, 22]

list(zip(students, departments, ages))


# lambda bir fonksiyon tanımlama şeklidir. Kullan at fonksiyonlardır.
def summer(a, b):
    return a + b

summer(1, 3) * 9

# Burada yaptığımız işlemi lambda ile yapalım,

new_sum = lambda a, b: a + b

new_sum(4, 5)


# map

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

list(map(new_salary, salaries)) # Döngü yazmadan tüm listeyi gezip işlem yaptırdık.


# lambda & map
list(map(lambda x : x * 20 / 100 + x, salaries)) # Yukarıda ki işlemin aynısını yaptık.


# filter - Çok önemli değil
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x : x % 2 == 0, list_store)) # Listede ki çift sayıları seçtik.


# reduce - Çok önemli değil
from functools import reduce

list_store = [1, 2, 3, 4]
reduce(lambda a, b : a + b, list_store)


# list comprehension
[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries] # if else birlikte kullanıldığında for döngüsü sağda kalır.
[salary * 2 for salary in salaries  if salary < 3000] # Sadece if kullanılırsa for döngüsü solda kalır.
# Önce for döngüsü yazılır, ardından soluna ne yapacağı yazılır, sonra şartlar ve koşullar eklenir.


# Örnek
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]
# students listesindeki elemanlar students_no listesinde varsa küçük harfle, yoksa büyük harfle yazdıralım.

[student.lower() if student in students_no else student.upper() for student in students]


# dict comprehension
dictionary = {"a" : 1,
              "b" : 2,
              "c" : 3,
              "d" : 4}

dictionary.key()
dictionary.values()
dictionary.items()

{k : v ** 2 for (k, v) in dictionary.items()} # k = Key, v = Value (Key = a,b,c,d Value = 1,2,3,4)


# Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# key 'ler orjinal değerler, Value 'lar ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

# kısa yol

{n : n ** 2 for n in numbers if n % 2 == 0}