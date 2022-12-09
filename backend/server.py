from database import db
from vessel import Vessel

class Server:
    def __init__(self) -> None:
        self.__database = db
        # uses hash set for better perfomance
        self.__vessels = set(self.__database.getVessels())

    @property
    def vessels(self):
        return self.__vessels

    # following methods provide api of working with databse, plus updates the internal state of the server
    def reload(self):
        vessels = self.__database.getVessels()
        for vessel in vessels:
            # Remove an old version of the vessel, if such exists
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
        # Uses a dummy vessel with same id, to get rid of the real one.
        # This works due to the reimplementation of the hash and equality dunder methods.
        vessel = Vessel(int(id), "", 0.0, 0.0)
        print(self.__vessels)
        if(vessel in self.__vessels):
            self.__vessels.remove(vessel)
            print(self.__vessels)
        
        self.reload()