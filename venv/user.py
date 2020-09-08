import sqlite3

class User:
    def __init__(self, user_id):
        self.print5()
        self.add_id_to_DB(user_id)

    def connect_to_DB(self):
        self.connect = sqlite3.connect("hello.db")
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()

    def get_all_id(self):
        self.connect_to_DB()
        request = "SELECT id FROM user"
        result = self.cursor.execute(request).fetchall()
        self.close()
        return [i[0] for i in result]

    def add_id_to_DB(self, user_id):
        self.connect_to_DB()
        if self.get_all_id().count(user_id) == 0:
            request = "INSERT INTO user(id, stat) VALUES(?, ?)"
            self.cursor.execute(request, (user_id, "start"))
            self.connect.commit()
            self.close()

    def get_field(self, user_id, field):
        self.connect_to_DB()
        request = f"SELECT {field} FROM user WHERE id=?"
        result = self.cursor.execute(request, (user_id, )).fetchall()
        self.close()
        return result[0]

    def set_field(self, user_id, field, value):
        self.connect_to_DB()
        request = f"UPDATE user SET {field}=? WHERE id=?"
        self.cursor.execute(request, (value, user_id))
        self.connect.commit()
        self.close()

    def print5(self):
        print("five")