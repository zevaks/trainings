'''
Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
Примечание: данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)
'''
import datetime

while True:
    inp = input('Enter Q(uit)/q(uit) to quit, otherwise Enter to continue: ')
    if inp == 'Q' or inp == 'quit' or inp == 'Quit' or inp == 'q':
        print('Exit train calculator...')
        exit(0)
    count_of_trains = int(input('How many trains you have in the list: '))
    trains = {}
    for train in range(1, count_of_trains + 1):
        number_of_train = input('Enter train number: ')
        departure_train_time = datetime.datetime.strptime(input('Enter departure time in format HH:MM :  '), '%H:%M')
        from_location = input('Enter departure from:  ')
        destination_train_time = datetime.datetime.strptime(input('Enter arrival time in format HH:MM :  '), '%H:%M')
        to_location = input('Enter train destination to: ')
        total_time_way = destination_train_time - departure_train_time
        trains[number_of_train] = {'dep_from': from_location,
                                'time_from': departure_train_time,
                                'dest_to': to_location,
                                'time_to': destination_train_time,
                                'time_in_way': total_time_way}
    print()
    print('*** Current time schedule for trains running more then 7h 20 mins')
    print('***')
    for number_of_train in trains.keys():
        if trains[number_of_train]['time_in_way'] > datetime.timedelta(seconds=26400):
            dep_from = trains[number_of_train]['dep_from']
            dest_to = trains[number_of_train]['dest_to']
            time_from = trains[number_of_train]['time_from']
            time_to = trains[number_of_train]['time_to']
            print(f"*** Train number: {number_of_train}, destination {dep_from} -> {dest_to}, "
                  f"dep: {datetime.datetime.strftime(time_from,'%H:%M')}, arr: {datetime.datetime.strftime(time_to,'%H:%M')}")
    print('***')
    print('*** END Train Shedule')
    print()









