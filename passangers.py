# -*- encoding: utf-8 -*-
from functions import *


def process(data, events, car):
    car_name = car
    for event in events:
        # Определить тип события

        if event.get('type') == 'walk':
            # Поиск пассажира

            value = search_man(data, event)
            if value == -1:
                return -1
            # Перемещение пассажира

            if replace_man(data, event, value) == -1:
                return -1
        elif event.get('type') == 'switch':
            # Перемещение вагонов

            switch(data, event)
        else:
            return -1
            # Проверка кол-ва пассажиров в вагоне

    for train in data:
        for car in train['cars']:
            if car_name == car['name']:
                return len(car['people'])
