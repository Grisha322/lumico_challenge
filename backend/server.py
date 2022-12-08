from database import db
from vessel import Vessel

class Server:
    def __init__(self) -> None:
        self.__database = db
        self.__vessels = set(self.__database.getVessels())

    @property
    def vessels(self):
        return self.__vessels

    def reload(self):
        vessels = self.__database.getVessels()
        print(vessels)
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

    # Delete is an expensive operation, due to the brute force search of the value to delete
    def removeVessel(self, id: int):
        self.__database.removeVessel(id)
        for vessel in self.__vessels:
            if vessel.id != id:
                continue
            self.__vessels.remove(vessel)
            print("removed vessel")
            break
        
        self.reload()