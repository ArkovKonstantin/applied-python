# -*- encoding: utf-8 -*-


def process(data, events, car):
    '''
        ТУТ ДОЛЖЕН БЫТЬ ВАШ КОД
    '''
    carname = car
    print(car)
    for train in data:
        print(train['name'])
        for car in train['cars']:
            print('\t{}'.format(car['name']))
            for man in car['people']:
                print('\t\t{}'.format(man))

    # print('ITEM ', data[0]['cars'])

    print('events ', events)
    # print('data ', data)

    for event in events:

        print('EVENT ', event)

        # keys = event.keys()
        value = event.get('passenger')
        # print('VALUE ', value)
        if value is not None:

            distance = event['distance'] - 1
            walk = False
            name = ''
            num, n = 0, 0

            for train in data:
                for car in train['cars']:
                    num += 1
                    if walk and distance > 0:
                        distance -= 1
                        # print('distance', distance)
                        continue
                    if walk and name == train['name'] and distance >= 0:
                        car['people'].append(value)
                        # print("СРАБОТАЛ АППЕНД")
                        walk = False
                        break
                        # print('DATA', data)
                    for man in car['people']:
                        if value == man:
                            car['people'].remove(value)
                            # print('LIST= ', (car['people']))
                            # print('DATA ', data)

                            walk = True
                            name = train['name']
                            n = num

                            # print(num)
                            break

            if distance < 0:
                m = 0
                n = n + distance + 1
                # print('N', n)
                # print('DATA',  data)
                # print(num)
                if n > 0:
                    for train in data:
                        for car in train['cars']:
                            m += 1
                            print('CHEK', n, m, walk, name)
                            if n == m and walk and name == train['name']:
                                car['people'].append(value)
                                print('WALK', walk)
                                walk = False
                                # print('DATA', data)
                                break
                else:
                    return -1
                    # print('VALUE ', value, distance, name, n, walk)
                    # print('DATA', data)





        else:
            value = event.get('cars')
            train_from = event['train_from']
            train_to = event['train_to']
            tail = []
            flagfrom = False
            # print('V', type(value))
            newdata = []
            for train in data:
                if train['name'] == train_from:
                    flagfrom = True
                    for car in train['cars'][::-1]:
                        # print('CARS', car)
                        if value > 0:
                            train['cars'].remove(car)
                            value -= 1
                            tail.append(car)
            if not flagfrom:
                return -1
            # print('TAIL ', tail)
            flagto = False
            for train in data:
                if train['name'] == train_to:
                    dlagto = True
                    # print('TRAINNAME ', train['name'])
                    train['cars'].extend(reversed(tail))

                    # print('DATA ', data)
            # if not flag

    for train in data:
        for car in train['cars']:
            if car['name'] == carname:
                return len(car['people'])
