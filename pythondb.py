import mysql.connector

# conn = mysql.connector.connect(host="localhost", user="root", password="", database="company")


# if mydb.is_connected():
#     print("Successfully connected")  

# else:
#     print("NOt connected")

class DBHelper:

    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="test")
        
        # self.cursorObject = self.conn.cursor()
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12)) '
        cur = self.conn.cursor()
        cur.execute(query)
        print("Table has been created...!!!")

    def insert_user(self, userid, username, phone):
        query = f"insert into user(userId, userName, phone) values({userid}, '{username}', '{phone}')"
        # print(query)

        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Data Insert Successfully")

    def fetch_all(self):
        query = "select * from user"
        # print(query)

        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            # print(row)
            print("User Id - ", row[0])
            print("User Name - ", row[1])
            print("Phone - ", row[2])
            print()
            print()

    def delete_user(self, userId):
        query = f"delete from user where userId = {userId}" 
        # print(query)

        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print(f"User with userID  = {userId} has been Deleted")

    def update_user(self, userId, newName, newPhone):
        query = f" update user set userName='{newName}', phone='{newPhone}' where userId ={userId}"
        # print(query)

        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Record has been updated")

# db = DBHelper()
# # db.insert_user(6, "Saurabh1","123456789")
# # db.insert_user(2, "Saurabh2","123456789")
# # db.insert_user(3, "Saurabh3","123456789")
# # db.insert_user(4, "Saurabh4","123456789")
# # db.insert_user(5, "Saurabh5","123456789")

# # db.fetch_all()

# # db.delete_user(6)
# # db.fetch_all()

# db.update_user(3,"Sam","987654321")
# db.fetch_all()