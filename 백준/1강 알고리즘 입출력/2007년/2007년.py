# x,y = map(int, input().split())
# arr1 = [1,3,5,7,8,10,12]
# arr2 = [4,6,9,11]
# arr3 = [2]
#
# month_days = 0
# for i in range(1,x):
#     if i in arr1:
#         month_days += 31
#     elif i in arr2:
#         month_days += 30
#     elif i in arr3:
#         month_days += 28
#
# final_days = month_days + y
#
# if final_days % 7 == 1:
#     print("MON")
# elif final_days % 7 == 2:
#     print("TUE")
# elif final_days % 7 == 3:
#     print("WED")
# elif final_days % 7 == 4:
#     print("THU")
# elif final_days % 7 == 5:
#     print("FRI")
# elif final_days % 7 == 6:
#     print("SAT")
# else:
#     print("SUN")

x,y = map(int, input().split())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
days = 0

for i in range(x-1):
    days = days + month[i]
print(days)
print(week[((days + y) % 7) - 1])
