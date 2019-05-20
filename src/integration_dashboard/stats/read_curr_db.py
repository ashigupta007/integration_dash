import sqlite3

def get_db_status():
	conn=sqlite3.connect('../ControlTable.db')
	c = conn.cursor()
	return 1