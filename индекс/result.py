txt_index = "Ваш индекс Руфье"
txt_workheart = "Ваша работоспособность сердца"
txt_nodata = "Нет данных для вашего возраста"
txt_res = []
txt_res.append('''Низкая''')
txt_res.append('''Удовлетворительная''')
txt_res.append('''Средняя''')
txt_res.append('''Выше среднего''')
txt_res.append('''Высокая''')

def index (p1,p2,p3):
    return (4*(p1+p2+p3)-200)/10

def neud_level(age):
    good = (min(15,age) - 7) // 2
    result_age = 21-good*1.5
    return result_age

def rufier_result(r_index, level):
    if r_index >= level:
        return 0
    level -= 4
    if r_index >= level:
        return 1
    level -= 5
    if r_index >= level:
        return 2
    level -= 5.5
    if r_index >= level:
        return 3
    return 4

def res(p1,p2,p3,age):
    if age < 7:
        return(txt_index + "0", txt_nodata)
    else:
        ruff_index = index(p1,p2,p3)
        result1 = txt_res[rufier_result(ruff_index, neud_level(age))]
        res1 = txt_index + str(ruff_index) + '\n' + txt_workheart + ':' + result1
        return res1