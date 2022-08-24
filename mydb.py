import psycopg2
from psycopg2.extras import RealDictCursor
import time





class DB:
    TABLE_NAME_FLIGHT = "flights"

    def __init__(self):
        pass


    def connect(self):
        while True:
            try:
                self.conn = psycopg2.connect(host='localhost', 
                                            database= 'my fastapi', 
                                            user='postgres', 
                                            password='optimus1985', 
                                            cursor_factory=RealDictCursor)

                self.cur = self.conn.cursor()
                print("database connected!")
                break
            except Exception as e:
                print("cant connect: {e}")
                time.sleep(2)

    def create(self, item):
        pass

    def getall(self):
        self.cur.execute(f'SELECT * FROM {self.TABLE_NAME_FLIGHT}')
        flights = self.cur.fetchall()
        return flights

        
    def update(self, item):
        pass

    def delete(self, item):
        pass



# cur.execute("INSERT INTO {TABLE_NAME_FLIGHT} (flightno, registration, bodytype) VALUES('ENT4019', 'SPESC','B738')")






 








