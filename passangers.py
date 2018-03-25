# -*- encoding: utf-8 -*-


def process(data, events, car):
    carname = car
    for event in events:
        value = event.get('passenger')
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
                        continue
                    if walk and name == train['name'] and distance >= 0:
                        car['people'].append(value)
                        walk = False
                        break
                    for man in car['people']:
                        if value == man:
                            car['people'].remove(value)
                            walk = True
                            name = train['name']
                            n = num
                            break
            if distance < 0:
                m = 0
                n = n + distance + 1
                if n > 0:
                    for train in data:
                        for car in train['cars']:
                            m += 1
                            if n == m and walk and name == train['name']:
                                car['people'].append(value)
                                walk = False
                                break
                else:
                    return -1
            print('DATA', data)
        else:
            value = event.get('cars')
            if value > 0:
                train_from = event['train_from']
                train_to = event['train_to']
                tail = []
                for train in data:
                    if train['name'] == train_from:
                        for car in train['cars'][::-1]:
                            if value > 0:
                                train['cars'].remove(car)
                                value -= 1
                                tail.append(car)
                for train in data:
                    if train['name'] == train_to:
                        train['cars'].extend(reversed(tail))

                print('DATA ', data)
            else:
                return -1
    for train in data:
        for car in train['cars']:
            if car['name'] == carname:
                return len(car['people'])
