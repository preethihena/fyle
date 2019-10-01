import psycopg2
import os
db_url=os.environ['DATABASE_URL']
conn = psycopg2.connect(db_url, sslmode='require')
cur = conn.cursor()



def get_IFSC(ifsc):
	cur.execute("select * from bank_branches where ifsc=%s",[ifsc])
	ans=cur.fetchone()
	data = {}
	data['ifsc'] = ans[0]
	data['bank_id'] = ans[1]
	data['branch'] = ans[2]
	data['address'] = ans[3]
	data['city'] = ans[4]
	data['district'] = ans[5]
	data['state'] = ans[6]
	data['bank_name'] = ans[7]
	return data



def get_Branches(bank,city,limit,offset):
	cur.execute("select * from bank_branches where bank_name=%s and city=%s\
	 			limit %s offset %s",[bank,city,limit,offset])
	ans2=cur.fetchall()
	branches = []
	for ans in ans2:
		data = {}
		data['ifsc'] = ans[0]
		data['bank_id'] = ans[1]
		data['branch'] = ans[2]
		data['address'] = ans[3]
		data['city'] = ans[4]
		data['district'] = ans[5]
		data['state'] = ans[6]
		data['bank_name'] = ans[7]
		branches.append(data)
	return branches