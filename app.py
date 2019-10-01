import falcon
from bankDetails import bank_using_ifsc,branches_using_bank,token_generate


api = application = falcon.API()
bank_ifsc=bank_using_ifsc()
branches=branches_using_bank()
token= token_generate()
api.add_route('/banks/', bank_ifsc)
api.add_route('/branches/', branches)
api.add_route('/generate_token/', token)



