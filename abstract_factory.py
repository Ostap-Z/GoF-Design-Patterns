from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def release_engine(self):
        pass


class JapaneseEngine(Engine):

    def release_engine(self):
        print("Japanese engine", end="")


class GermanyEngine(Engine):

    def release_engine(self):
        print("Germany engine", end="")


class Car(ABC):

    @abstractmethod
    def release_car(self, engine: Engine):
        pass


class JapaneseCar(Car):

    def release_car(self, engine: Engine):
        print("Release Japanese car", end=", ")
        engine.release_engine()


class GermanyCar(Car):

    def release_car(self, engine: Engine):
        print("Release Germany car", end=", ")
        engine.release_engine()


class Factory(ABC):

    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_car(self) -> Car:
        pass


class JapaneseFactory(Factory):

    def create_engine(self) -> Engine:
        return JapaneseEngine()

    def create_car(self) -> Car:
        return JapaneseCar()


class GermanyFactory(Factory):

    def create_engine(self) -> Engine:
        return GermanyEngine()

    def create_car(self) -> Car:
        return GermanyCar()


if __name__ == "__main__":
    japanese_factory = JapaneseFactory()
    japanese_engine = japanese_factory.create_engine()
    japanese_car = japanese_factory.create_car()
    japanese_car.release_car(japanese_engine)

    print()

    germany_factory = GermanyFactory()
    germany_engine = germany_factory.create_engine()
    germany_car = germany_factory.create_car()
    germany_car.release_car(germany_engine)
