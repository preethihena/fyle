import json
import falcon
import jwt
import datetime

from getData import get_IFSC,get_Branches

class bank_using_ifsc(object):

    def on_get(self, req, resp,ifsc):
    	try:
    		token=req.get_header('Authorization')
    		token=token.split()
    		decoded=jwt.decode(token[1], 'secret', algorithms=['HS256'])
    		bank_details = get_IFSC(ifsc)
    		resp.body = json.dumps(bank_details, ensure_ascii=False)
    		resp.status = falcon.HTTP_200
    	except jwt.ExpiredSignatureError:
    		error_msg="Token expired"
    		resp.body=json.dumps(error_msg,ensure_ascii=False)
    		resp.status = falcon.HTTP_408


class branches_using_bank(object):

	def on_get(self, req, resp,city,bank):

		try:
			token=req.get_header('Authorization')
			token=token.split()
			decoded=jwt.decode(token[1], 'secret', algorithms=['HS256'])
			limit=req.get_param('limit')
			offset=req.get_param('offset')
			if limit is None:
				limit = 0
			if offset is None:
				offset = 0
			bank_details = get_Branches(city,bank,limit,offset)
			resp.body = json.dumps(bank_details, ensure_ascii=False)
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
		resp.body=json.dumps(encoded,ensure_ascii=False)
		resp.status=falcon.HTTP_200