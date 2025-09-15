# import time
# sonlar = [1,32,4, 546, 7, 76]
# def sonlarnisaralash(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j]> arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# bosh = time.perf_counter()
# sonlar = sonlarnisaralash(sonlar)
# tugash = time.perf_counter()
# print(sonlar, tugash-bosh)

sonlar = [1,32,4, 546, 7, 76]
a = int(input("Qidirilayotgan sonni kiriting - "))
sanoq = 0
for i in range(len(sonlar)):
    if sonlar[i] == a:
        sanoq = sanoq + 1
if sanoq > 0:
    print(sanoq)
else:
    print("Bunday element mavjud emas")