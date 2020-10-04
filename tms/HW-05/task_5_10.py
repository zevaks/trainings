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
    train_count = int(input('How many trains you have in the list: '))
    trains = {}
    for train in range(1, train_count + 1):
        train_number = input('Enter train number: ')
        train_departure_time_hour, train_departure_time_min = input('Enter departure time in format HH:MM :  ').split(':')
        train_departure = input('Enter departure from:  ')
        train_destination_time_hour, train_destination_time_min = input('Enter destination time in format HH:MM :  ').split(':')
        train_destination = input('Enter train destination to: ')
        train_time_in_way = datetime.timedelta(hours=int(train_destination_time_hour), minutes=int(train_destination_time_min)) - \
                            datetime.timedelta(hours=int(train_departure_time_hour), minutes=int(train_departure_time_min))
        trains[train_number] = {'dep_from': train_departure,
                                'time_from': datetime.time(int(train_departure_time_hour), int(train_departure_time_min)).strftime('%H:%M'),
                                'dest_to': train_destination,
                                'time_to': datetime.time(int(train_destination_time_hour), int(train_destination_time_min)).strftime('%H:%M'),
                                'time_in_way': train_time_in_way}
    print('*** Current time schedule for trains go more then 7h 20 mins')
    for train_number in trains.keys():
        if trains[train_number]['time_in_way'] > datetime.timedelta(seconds=26400):
            dep_from = trains[train_number]['dep_from']
            dest_to = trains[train_number]['dest_to']
            time_from = trains[train_number]['time_from']
            time_to = trains[train_number]['time_to']
            print(f'*** Train number: {train_number}, destination {dep_from} - {dest_to}, dep: {time_from}, arr: {time_to}')
    print('*** END Train Shedule')









