import psycopg2

conn = psycopg2.connect(database = "task", user = "postgres", 
			password = "hena@22", host = "127.0.0.1", port = "5432")
cur = conn.cursor()



def get_IFSC(ifsc):
	cur.execute("select * from branches where ifsc= %s",[ifsc])
	ans=cur.fetchone()
	cur.execute("select name from banks where id= %s",[ans[1]])
	ans2=cur.fetchone()
	return ans+ans2


def get_Branches(city,bank,limit,offset):
	cur.execute("select * from banks where name=%s",[bank])
	ans=cur.fetchone()
	cur.execute("select * from branches where bank_id=%s \
				and city=%s limit %s offset %s",[ans[1],city,limit,offset])
	ans2=cur.fetchall()
	return ans2