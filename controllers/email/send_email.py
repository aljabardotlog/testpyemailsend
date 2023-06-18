import pymysql
from connect import mysql
from flask import jsonify, request

def getSendEmail():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		cursor.execute("""
            SELECT 
                uuid, 
                (select email from email_master where uuid=uuid_user) as useremail,
                (select name from event_master where uuid=uuid_event) as event, 
                timesend, 
                CASE status
                    WHEN 0 THEN 'False'
                    WHEN 1 THEN 'True'
                    ELSE 'Unknown'
                END status
            FROM jublia.send_email;
         """)
		
		rows = cursor.fetchall()
		return rows
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()