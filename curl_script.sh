#!/bin/bash
url='https://aqueous-meadow-97023.herokuapp.com'
ifsc='ALLA0210636'
token=`curl -s --request POST  --data '{"username":"preethi"}' $url/generate_token`
token="${token%\"}"
token="${token#\"}"
echo "$token"
output=`curl -s -H "Authorization: Bearer ${token}" --request GET $url/banks/$ifsc`

echo $output

output=`curl -s -H "Authorization: Bearer ${token}"  --request GET $url/branches/INDIAN%20OVERSEAS%20BANK/MUMBAI?limit=5"&"offset=0`
echo $output