class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type: str, duration: float, distance: float,
                 speed: float, calories: float):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
        self.formatted_calories = "{:.3f}".format(calories)

    def get_message(self):
        return f'Тип тренировки: {self.training_type}; \
 Длительность: {self.duration} ч.;\
 Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч;\
 Потрачено ккал: {self.formatted_calories}. '


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.distance = self.action * self.LEN_STEP / self.M_IN_KM
        self.mean_speed = self.distance / self.duration

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        calories = self.get_spent_calories()
        speed = self.get_mean_speed()
        distance = self.get_distance()
        training_type = self.__class__.__name__
        return InfoMessage(training_type, self.duration, distance,
                           speed, calories)


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        result_calories_run = ((18 * self.get_mean_speed() + 1.79)
                               * self.weight / 1000 * self.duration)
        return result_calories_run


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, action: int, duration: int, weight: float,
                 height: int) -> None:
        super().__init__(action, duration, weight)
        self.weight = weight
        self.height = height
        self.M_IN_SEC = self.get_mean_speed() / 3.6
        self.training_in_min = duration / 60

    def get_spent_calories(self) -> float:
        result_calories_walk = ((0.035 * self.weight + (self.M_IN_SEC ** 2
                                                        / self.height)
                                 * 0.029 * self.weight) * self.training_in_min)
        return result_calories_walk


class Swimming(Training):
    """Тренировка: плавание."""
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: int, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.avg_speed_swmng = (self.length_pool * self.count_pool
                                / 1000 / self.duration)

    def get_spent_calories(self) -> float:
        result_calories_swmng = ((self.avg_speed_swmng + 1.1) * 2
                                 * self.weight * self.duration)
        return result_calories_swmng

    def get_mean_speed(self) -> float:
        return self.avg_speed_swmng


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    parametr = {
        'RUN': Running,
        'SWM': Swimming,
        'WLK': SportsWalking}
    if workout_type in parametr:
        return parametr[workout_type](*data)
    else:
        raise ValueError("Тренировка не найдена")


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    message = info.get_message()
    print(message)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

