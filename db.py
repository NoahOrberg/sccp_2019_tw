import sqlite3

dbname = 'data.db';

con = sqlite3.connecton();

c = conn.cursor();

c.execute('INSERT INTO users ');

c.commit();
