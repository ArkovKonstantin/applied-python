def search_man(data, event):
    num = 0
    place = {}
    for train in data:
        for car in train['cars']:
            num += 1
            for man in car['people']:
                if event.get('passenger') == man:
                    car['people'].remove(man)
                    place['num'] = num
                    place['name'] = train['name']
                    return place
    if not place:
        return -1


def replace_man(data, event, value):
    destination = value['num'] + event.get('distance')
    for train in data:
        for car in train['cars']:
            destination -= 1
            if destination == 0 and value['name'] == train['name']:
                car['people'].append(event.get('passenger'))
                return 1
    return -1


def switch(data, event):
    value = event.get('cars')
    train_from = event.get('train_from')
    train_to = event.get('train_to')
    if value > 0:
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
    else:
        return -1
