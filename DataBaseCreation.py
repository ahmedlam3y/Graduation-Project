import sqlite3

def main():
    db = sqlite3.connect("SGDataBase.db")
    db.execute("create table if not exists Admin(Name str, Password str, CarNumber str, CarModel str, CarColor str)")


if __name__ == '__main__':
    main()
