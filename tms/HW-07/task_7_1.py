'''
1. Написать 12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты

Примечание: функция принимает на вход число и возвращает конвертированное число

2. Написать программу, со следующим интерфейсом:
пользователю предоставляется на выбор 12 вариантов перевода(описанных в первой задаче).
Пользователь вводит цифру от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого задания.
Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.
'''
def du_cm(du):
  cm = float(du) * float(2.54)
  return str(cm) + ' cm'
def cm_du(cm):
  du = float(cm) * float(0.394)
  return str(du) + ' du'
def mil_km(mil):
  km = float(mil) * float(1.609)
  return km
def km_mil(km):
  mil = float(km) * float(0.62137)
  return mil
def fu_kg(fu):
  kg = float(fu) * float(0.454)
  return kg
def kg_fu(kg):
  fu = float(kg) * float(2.2046)
  return fu
def un_g(un):
  g = float(un) / float(0.035274)
  return g
def g_un(g):
  un = float(g) * float(0.035274)
  return un
def gal_l(gal):
  l = float(gal) * float(3.785)
  return l
def l_gal(l):
  gal = float(l) * float(0.2641)
  return gal
def pt_l(pt):
  l = float(pt) / float(1.7598)
  return l
def l_pt(l):
  pt = float(l) * float(2.1133)
  return pt

while True:
    print('1. Дюймы в сантиметры;  2. Сантиметры в дюймы; 3. Мили в километры; 4. Километры в мили;\n' 
          '5. Фунты в килограммы;  6. Килограммы в фунты; 7. Унции в граммы;   8. Граммы в унции\n' 
          '9. Галлон в литры;      10. Литры в галлоны;   11. Пинты в литры;   12. Литры в пинты')
    choice = int(input('Selcet from converter from 1 to 12 or 0 to exit: '))
    if choice == 0 :
        print('Exit')
        exit()
    elif choice <= 12:
        number_to_convert = input('Enter number to be converted: ')
        calculation = {1: du_cm, 2: cm_du, 3: mil_km, 4: km_mil, 5: fu_kg, 6: kg_fu,
                       7: un_g, 8: g_un, 9: gal_l, 10: l_gal, 11: pt_l, 12: l_pt}
        print()
        print(calculation[choice](number_to_convert))
        print()
    else:
        print()
        print('Greater then 12 ')
        print()
        continue


