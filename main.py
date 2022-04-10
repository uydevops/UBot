from typing import Union, Any

import feedparser
import pyfiglet
import mysql.connector
from mysql.connector.cursor import CursorBase, MySQLCursor, MySQLCursorBuffered, MySQLCursorRaw, MySQLCursorBufferedRaw, \
    MySQLCursorDict, MySQLCursorBufferedDict, MySQLCursorNamedTuple, MySQLCursorBufferedNamedTuple, MySQLCursorPrepared
from mysql.connector.cursor_cext import CMySQLCursor

ascii_banner = pyfiglet.figlet_format("UDevp Bot")
print(ascii_banner)

url = "http://www.cnnturk.com/feed/rss/news"
haberler=feedparser.parse(url)

i=0
for haber in haberler.entries:
    i+=1
    print(i)
    print(haber.title)
    print(haber.link)
    print(haber.summary)


turl="http://patorjk.com/software/taag/#p=display&f=Stop&t=UYDev"
print(turl)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test2"
)
mycursor = mydb.cursor()

sql = "INSERT INTO haberler (haber_title, haber_link) VALUES (%s, %s)"
val = [haber.title,haber.link]

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")