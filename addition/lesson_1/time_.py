import time
import datetime

'''
%a -> Mahalliy aholining ish kunining qisqartirilgan nomi.

%A -> Mahalliy hududning ish kunining toʻliq nomi.

%b -> Mahalliy oyning qisqartirilgan nomi.

%B -> Mahalliy hududning toʻliq oy nomi.

%c -> Mahalliy tilning tegishli sana va vaqt ko'rinishi.

%d -> O'nlik raqam sifatida oyning kuni [01,31].

%H -> Soat (24 soatlik soat) kasr soni sifatida [00,23].

%I -> Soat (12 soatlik soat) o'nlik raqam sifatida [01,12].

%j -> O'nlik raqam sifatida yil kuni [001,366].

%m -> Oy kasrli raqam sifatida [01,12].

%M -> O'nlik raqam sifatida daqiqa [00,59].

%p -> Mahalliy tilning AM yoki PM ekvivalenti.

%S -> Ikkinchi o'nlik raqam sifatida [00,61].

%w -> Hafta kuni kasr soni sifatida [0(yakshanba),6].

%x -> Mahalliy tilning tegishli sanasi.

%X -> Mahalliyning tegishli vaqtni ko'rsatishi.

%y -> O'nlik son sifatida asrsiz yil [00,99].

%Y -> O'nlik son sifatida asr bilan yil.
'''

print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2023-04-26 17:54:30
print(datetime.datetime.now())  # 2023-04-26 17:54:30.939615
# time.sleep(3)
print(time.gmtime(1682513325.0427969))  #
print(time.time()) # second 1682513589.2121658
print(datetime.time(12 , 56 , 12 , 23))   # 12:56:12.000023
print(datetime.timedelta(12 , 1000))    # 12 days, 0:16:40

