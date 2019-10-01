#!/bin/sh
url='https://aqueous-meadow-97023.herokuapp.com'
ifsc='ALLA0210636'
token=`curl -s --request POST  --data '{"username":"preethi"}' $url/generate_token| \
python3 -c "import sys, json; print(json.load(sys.stdin)['token'])"`
token="${token%\"}"
token="${token#\"}"
echo "\nToken : $token\n"
echo "Query 1: GET API to fetch a bank details,given branch IFSC code: $ifsc \n"

output=`curl -s -H "Authorization: Bearer ${token}" --request GET $url/banks?ifsc={$ifsc}`


echo $output | python -m json.tool

echo "\nQuery 2: GET API to fetch all details of branches,given \
bank name = INDIAN OVERSEAS BANK and a city = MUMBAI \n"
bank="INDIAN%20OVERSEAS%20BANK"
city="MUMBAI"
limit=5
offset=0

output=`curl -s -H "Authorization: Bearer ${token}"  --request GET \
$url/branches?bank={$bank}"&"city={$city}"&"limit={$limit}"&"offset={$offset}`


echo $output | python -m json.tool


