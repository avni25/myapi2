import psycopg2
from psycopg2.extras import RealDictCursor


class DB:
    TABLE_NAME_FLIGHT = "flights"

    def __init__(self):
        pass


    def connect(self):
        try:
            self.conn = psycopg2.connect(host='localhost', database= 'my fastapi', user='postgres', password='optimus1985', cursor_factory=RealDictCursor)
            self.cur = self.conn.cursor()
            print("database connected!")
        except Exception as e:
            print("cant connect: {e}")
    

    def create(self, item):
        pass

    def get(self):
        pass

    def update(self, item):
        pass

    def delete(self, item):
        pass



# cur.execute("INSERT INTO {TABLE_NAME_FLIGHT} (flightno, registration, bodytype) VALUES('ENT4019', 'SPESC','B738')")






 








