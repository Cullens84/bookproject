

import pymysql


class Database:
    def connect(self):
        # return pymysql.connect("book-mysql", "dev", "dev", "crud_flask")

        return pymysql.connect(host="book-mysql", user="dev", password="dev", database="crud_flask", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM book order by name asc")
            else:
                cursor.execute(
                    "SELECT * FROM book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO book(name,Book,Author) VALUES(%s, %s, %s)",
                           (data['name'], data['Book'], data['Author'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE book set name = %s, Book = %s, Author = %s where id = %s",
                           (data['name'], data['Book'], data['Author'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
