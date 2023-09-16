import sqlite3

class Database:
    
    def connect(self, filename):
        conn = sqlite3.connect(filename)
        return conn

    def __init__(self, file, desired_table):
        self.link = self.connect(file)
        self.cursor = self.link.cursor()
        self.current_table = desired_table
    
    def printAllRecords(self):
        self.cursor.execute(f"SELECT * FROM {self.current_table}")
        result = self.cursor.fetchall()
        return result
    
    def selectRecords(self, command):
        self.cursor.execute(f"SELECT * FROM {self.current_table} {command}")
        result = self.cursor.fetchall()
        return result

    def changeTable(self, new_table):
        self.current_table = new_table
    
    def updateRecords(self, command):
        self.cursor.execute(f"UPDATE {self.current_table} SET {command}")

    def deleteRecords(self, command):
        self.cursor.execute(f"DELETE FROM {self.current_table} {command}")
    
    def addRecord(self, command):
        self.cursor.execute(f"INSERT INTO {self.current_table} VALUES {command}")
    
    def alterTable(self, command):
        self.cursor.execute(f"ALTER TABLE {self.current_table} {command}")
    
    def getTableFields(self):
        data = self.cursor.execute(f"SELECT * FROM {self.current_table}")
        columns = []
        for column in data.description:
            columns.append(column[0])
        return columns


if __name__ == '__main__':
    test = Database("filmflix.db", "tblFilms")
    print(test.printAllRecords())
    print(test.getTableFields())