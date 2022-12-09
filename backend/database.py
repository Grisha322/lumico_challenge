import mysql.connector
from mysql.connector import cursor
from vessel import Vessel
import dbConstants as constants

class Database:
    def __init__(self) -> None:
        # timestamp is used to select only unseen data from the database
        self.__timestamp = None
        self.__mydb = None

    def __openConnection(self) -> cursor.MySQLCursor:
        if not self.__isConnected():
            self.__mydb = mysql.connector.connect(
                host=constants.host, 
                user=constants.user, 
                password=constants.password, 
                database=constants.database
            )
        
        return self.__mydb.cursor()

    def __closeConnection(self) -> None:
        if not self.__isConnected():
            return

        self.__mydb.commit()
        self.__mydb.close()
        self.__mydb = None

    def __isConnected(self) -> bool:
        return self.__mydb != None and self.__mydb.is_connected()

    # Returns a list of vessels created/modified since the last update
    def getVessels(self) -> list:
        query = f"select * from {constants.vesselsTable}"
        if(self.__timestamp != None):
            query += f" where {constants.vesselsTimestampColumn} > '{self.__timestamp}'"
            
        query += " order by last_changed desc;"

        result = self.__performQuery(query=query)
        vessels = []
        newTimestamp = None
        for x in result:
            vessel, t = self.__parseResult(x)
            vessels.append(vessel)
            if newTimestamp == None:
                newTimestamp = t
        if newTimestamp != None:
            self.__timestamp = newTimestamp
        return vessels

    # Adds a new vessel into the database.
    def addVessel(self, name: str, lat: float, long: float):
        name = name.strip().replace("\n", "")
        query = f"""insert into {constants.vesselsTable}
            (
                {constants.vesselsNameColumn}, 
                {constants.vesselsLatColumn}, 
                {constants.vesselsLongColumn}
            ) values
            (
                '{name}', 
                {float(lat):8.6f}, 
                {float(long):9.6f}
            );"""
        
        self.__performQuery(query=query, keepConnection=True)        

    # deletes the vesse with the given id from the database      
    def removeVessel(self, id: int):
        query = f"delete from {constants.vesselsTable} where {constants.vesselsIdColumn} = {id};"
        self.__performQuery(query=query, keepConnection=True)  

    # edits vessel details in the database
    def editVessel(self, id: int, name: str, lat: float, long: float):
        name = name.strip().replace("\n", "")
        query = f"""update {constants.vesselsTable} 
            set 
                {constants.vesselsNameColumn} = '{name}',
                {constants.vesselsLatColumn} = {lat}, 
                {constants.vesselsLongColumn} = {long} 
            where {constants.vesselsIdColumn} = {id};"""
        
        self.__performQuery(query=query, keepConnection=True) 

    def __performQuery(self, query: str, keepConnection = False):
        cursor = self.__openConnection()
        print(query)
        cursor.execute(query)
        result = cursor.fetchall()
        if(keepConnection):
            cursor.close()
        else:
            self.__closeConnection()
            
        return result

    def __parseResult(self, result: tuple) -> tuple:
        id, name, lat, long, timestamp = result
        return (Vessel(id, name, lat, long), timestamp)

# Singleton object
db = Database()