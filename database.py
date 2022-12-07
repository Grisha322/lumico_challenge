import mysql.connector
from mysql.connector import cursor
from vessel import Vessel
import dbConstants
from datetime import datetime


class DBReading:
    def __init__(self, vessels: list, timestamp: datetime) -> None:
        self.vessels = vessels
        self.timestamp = timestamp

class Database:
    vesselTable = "vessels"
    def __init__(self) -> None:
        self.__mydb = None

    def __openConnection(self) -> cursor.MySQLCursor:
        if not self.__isConnected():
            self.__mydb = mysql.connector.connect(
                host=dbConstants.host, 
                user=dbConstants.user, 
                password=dbConstants.password, 
                database=dbConstants.database
            )
        
        return self.__mydb.cursor()

    def __closeConnection(self) -> None:
        if not self.__isConnected():
            return

        self.__mydb.close()
        self.__mydb = None

    def __isConnected(self) -> bool:
        return self.__mydb != None and self.__mydb.is_connected()

    def getVessels(self, timestamp = None) -> DBReading:
        cursor = self.__openConnection()

        query = None
        if(timestamp == None):
            query = dbConstants.vesselsSelectStatement + ";"
        else:
            query = f"{dbConstants.vesselsSelectStatement} where {dbConstants.vesselsTimestampColumn} > '{timestamp}'"

        cursor.execute(query)
        vessels = []
        for x in cursor:
            vessel, t = self.__parseResult(x)
            print(vessel)
            vessels.append(vessel)
            if maxT == None:
                maxT = t
        self.__closeConnection()
        return DBReading(vessels=vessels, timestamp=maxT)

    def __parseResult(self, result: tuple) -> tuple:
        id, name, lat, long, timestamp = result
        return (Vessel(id, name, lat, long), timestamp)

# Singleton object
db = Database()

