import psycopg2
import os
db_url=os.environ['DATABASE_URL']

conn = psycopg2.connect(db_url, sslmode='require')
cur = conn.cursor()



def get_IFSC(ifsc):
	cur.execute("select * from bank_branches where ifsc=%s",[ifsc])
	ans=cur.fetchone()
	return ans



def get_Branches(city,bank,limit,offset):
	cur.execute("select * from bank_branches where bank_name=%s and city=%s\
	 			limit %s offset %s",[bank,city,limit,offset])
	ans2=cur.fetchall()
	return ans2