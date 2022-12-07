from decimal import Decimal

class Vessel:
    def __init__(self, id: int, name: str, lat: Decimal, long: Decimal):
        self.__id = id
        self.name = name
        self.lat = lat
        self.long = long

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lat(self) -> float:
        return self.__lat

    @lat.setter
    def lat(self, lat: float):
        self.__lat = lat

    @property
    def long(self) -> float:
        return self.__long

    @long.setter
    def long(self, long: float):
        self.__long = long

    def __repr__(self) -> str:
        return f"{self.id} {self.name} {self.lat:8.6f} {self.long:9.6f}"

    def __eq__(self, __o: object) -> bool:
        return (
            self.__class__ == __o.__class__ and
            self.name == __o.name and
            self.lat == __o.lat and
            self.long == __o.long
        )

    def __hash__(self) -> int:
        return hash(self.id)