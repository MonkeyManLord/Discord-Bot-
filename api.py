import requests
import json

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"sname":"Alice","fname":"John"}

headers = {
	"X-RapidAPI-Key": "315bdcb2f9msh7337f81afeb7004p13b3f6jsnf7c48660ac73",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

fname = data['fname']
sname = data['sname']
percentage = data['percentage']
result = data['result']

print(f'{fname} and {sname}\'s percentage: {percentage}% - {result}.')
print(fname[1:])




