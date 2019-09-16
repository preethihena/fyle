#!/bin/sh
url='https://aqueous-meadow-97023.herokuapp.com'
ifsc='ALLA0210636'
token=`curl -s --request POST  --data '{"username":"preethi"}' $url/generate_token`
token="${token%\"}"
token="${token#\"}"
echo "\nToken : $token\n"
echo "Query 1: GET API to fetch a bank details,given branch IFSC code: $ifsc \n"
output=`curl -s -H "Authorization: Bearer ${token}" --request GET $url/banks/$ifsc`

echo $output

echo "\nQuery 2: GET API to fetch all details of branches,given \
bank name = INDIAN OVERSEAS BANK and a city = MUMBAI \n"
output=`curl -s -H "Authorization: Bearer ${token}"  --request GET \
$url/branches/INDIAN%20OVERSEAS%20BANK/MUMBAI?limit=5"&"offset=0`

echo $output