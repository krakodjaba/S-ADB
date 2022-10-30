import sqlite3
import os


class init:
    global cursor
    global connection
    connection = None
    try:
        connection = sqlite3.connect('S-ADB.db', check_same_thread=False)
    except Error as e:
        print(e)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS devices(base_id INTEGER,ip TEXT NOT NULL UNIQUE,port INTEGER,info TEXT,last_conn TEXT,PRIMARY KEY(base_id AUTOINCREMENT));")
    
    def insert(ip: str, port: int, info:str, status:str):
        values = [("ip", ip),
                  ("port", port),
                  ("info", info),
                  ("last_conn", status)]
        cursor.execute("INSERT OR IGNORE INTO devices(ip, port, info, last_conn) VALUES (?,?,?,?)",(ip, port, info, status))
        cursor.execute("UPDATE devices SET last_conn = (?) WHERE ip = (?)", (status, ip))
        cursor.execute("UPDATE devices SET port = (?) WHERE ip = (?)", (port, ip))
        cursor.execute("UPDATE devices SET info = (?) WHERE ip = (?)", (info, ip))
        connection.commit()
    def make_offline():
        offline = 'offline'
        re = cursor.execute('SELECT ip from devices WHERE last_conn = "online";')
        res = re.fetchall()
        for ip in res:
            ip = str(ip).replace("('", "").replace("',)","")
            #print(ip)
            cursor.execute("UPDATE devices SET last_conn = (?) WHERE ip = (?)", (offline, ip))
    def view_devices():
        re = cursor.execute('SELECT * from devices ORDER BY last_conn;')
        res = re.fetchall()
        import time
        return res
    def all_ip():
        re = cursor.execute('SELECT ip, port from devices;')
        res = re.fetchall()
        import time
        return res
    def view_count():
        re = cursor.execute('SELECT DISTINCT(ip) from devices;')
        res = re.fetchall()
        res = len(res)
        import time
        return res
    def view_online():
        re = cursor.execute('SELECT DISTINCT(ip) from devices WHERE last_conn = "online";')
        res = re.fetchall()
        res = len(res)
        import time
        return res