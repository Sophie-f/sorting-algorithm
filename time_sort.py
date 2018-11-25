# میخواهیم تعداد عملیات را بشماریم.ضرایب مهم نیستند. یک آرایه رندوم میسازیم. تعداد عملیات را میشماریم.ان بار تکرار میکنیم

from random import randrange 
max = 200 #بزرگترین عدد آرایه 
len_list = 100
sim_number = 100
def simulate(max,len_list):
    my_list = [randrange(max) for i in range(len_list)]
    ops = 0               #شمارنده تعداد عملیات
    for i in range(1,len_list):
        temp = my_list[i]
        j = i-1           #شمردن اینجا خیلی مهم نیست چون کار اصلی روی آرایه دو خط پایین‌تره 
        while j >= 0 and temp < my_list[j]:
            my_list[j+1], j = my_list[j], j-1
            ops += 1         #تعداد نابه‌جایی ها را می‌شماری
        my_list[j+1] = temp        
    return ops
sum_ops = 0   
for i in range(sim_number):
    sum_ops += simulate(max, len_list)
print(int(sum_ops/sim_number))
# نتیجه
#  تعداد نابه‌جایی یعنی تعدا حالتهایی که جای دوعنصر ارایه اشتباه باشد مثلا در
#   [2,0,3,4,6]
# تعداد نابه‌جایی یک است
# کمترین تعداد مربوط به حالت کاملا مرتب است وبرابر با صفر است. 
# بدترین حالت نابه جایی مربوط به آرایه معکوس مرتب شده و از مرتبه ۲ از طول آرایه است.
# میانگین حالت ها تعداد بدترین تقسیم بر دو است
# در هر دو حالت میانگین و بدترین تعداد عملیات از مرتیه طول آرایه به توان دو است.
#در مورد مرتبه ،جلسه جهار داده ساختار اخراش 