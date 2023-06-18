import pymysql
from connect import mysql
from flask import jsonify, request

def getEmail():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM email_master")
		rows = cursor.fetchall()
		return rows
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()