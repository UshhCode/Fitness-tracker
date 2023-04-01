
class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        n = 3
        return f'Тип тренировки: {training_type:.{n}f}; Длительность: {duration} ч.; \
        Дистанция: {distance} км; Ср. скорость: {speed} км/ч; \
        Потрачено ккал: {calories}. ' # training_type округление до тысячных {n}


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    distance = LEN_STEP / M_IN_KM  # Может нужно добавить *action?

    def __init__(self, action: int, duration: float, weight: float,) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return distance / duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return get_message(InfoMessage)        #Возвращает объект класса сообщений


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self):
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        result_calories_run = (CALORIES_MEAN_SPEED_MULTIPLIER * get_mean_speed() + CALORIES_MEAN_SPEED_SHIFT) \
                          * weight / M_IN_KM * duration
        return result_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    M_IN_SEC = get_mean_speed() / 3.6
    training_in_min = duration / 60

    def __init__(self, height):
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        result_calories_walk = ((0.035 * weight + (M_IN_SEC**2 / height)
                                 * 0.029 * weight) * training_in_min)
        return result_calories_walk


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    avg_speed_swmng = length_pool * count_pool / M_IN_KM / duration

    def __init__(self, length_pool, count_pool):
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        result_calories_swmng = (get_mean_speed(Swimming) + 1.1) * 2 * weight * duration
        return result_calories_swmng

    def get_mean_speed(self) -> float:
        avg_speed_swmng = length_pool * count_pool / M_IN_KM / duration
        return avg_speed_swmng


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

