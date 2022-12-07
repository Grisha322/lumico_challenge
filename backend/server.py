from database import db

class Server:
    def __init__(self) -> None:
        self.__database = db
        self.__vessels = set(self.__database.getVessels())

    def reload(self):
        vessels = self.__database.getVessels()
        for vessel in vessels:
            if vessel in self.__vessels:
                self.__vessels.remove(vessel)
            self.__vessels.add(vessel)

    def addVessel(self, name: str, lat: float, long: float):
        self.__database.addVessel(name, lat, long)
        self.reload()

    def editVessel(self, id: int, name: str, lat: float, long: float):
        self.__database.editVessel(id, name, lat, long)
        self.reload()

    def removeVessel(self, id: int):
        self.__database.removeVessel(id)
        self.reload()