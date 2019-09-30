import json
import falcon
import jwt
import datetime

from getData import get_IFSC,get_Branches

def authentcate(token = None):
	decode = jwt.decode(token, 'secret', algorithms=['HS256'])

class bank_using_ifsc(object):

    def on_get(self, req, resp,ifsc):
    	try:
    		token=req.get_header('Authorization').split()
    		authentcate(token[1])
    		doc = {}
    		bank_details = get_IFSC(ifsc)
    		doc = bank_details
    		resp.body = json.dumps(doc, ensure_ascii = False)
    		resp.status = falcon.HTTP_200
    	except jwt.ExpiredSignatureError:
    		error_msg="Token expired"
    		resp.body=json.dumps(error_msg,ensure_ascii=False)
    		resp.status = falcon.HTTP_408


class branches_using_bank(object):

	def on_get(self, req, resp,city,bank):

		try:
			token=req.get_header('Authorization').split()
			authentcate(token[1])
			limit=req.get_param('limit')
			offset=req.get_param('offset')
			if limit is None:
				limit = 0
			if offset is None:
				offset = 0
			doc = {}
			bank_details = get_Branches(city,bank,limit,offset)
			doc['branches']= bank_details
			resp.body = json.dumps(doc, ensure_ascii = False)
			resp.status = falcon.HTTP_200

		except jwt.ExpiredSignatureError:
			error_msg="Token expired"
			resp.body=json.dumps(error_msg,ensure_ascii=False)
			resp.status = falcon.HTTP_408


class token_generate(object):

	def on_post(self,req,resp):
		data = json.loads(req.stream.read().decode('utf-8'))
		encoded = jwt.encode({'iss':data,
					'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)}, 
					'secret',algorithm='HS256').decode('utf-8')
		data = {'token':encoded}
		resp.body=json.dumps(data,ensure_ascii=False)
		resp.status=falcon.HTTP_200