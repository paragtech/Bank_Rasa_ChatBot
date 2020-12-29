import requests

def Product(gender,age,balance):
    #fastapi = "http://127.0.0.1:8000/Classify"
    #msg = '"{\\"Gender\\":\\"'+gender+'\\",\\"Age\\":'+age+',\\"Balance\\":'+balance+'}"'
    #msg = "{\"Gender\":\"Male\",\"Age\":20,\"Balance\":55}"
    fastapi = "http://127.0.0.1:8000/Classifiy?Gender_="+gender+"&Age_="+age+"&Balance_="+balance
    print(fastapi)
    json_data = requests.get(fastapi)
    #print(json_data.text)
    group = (json_data.text)[-65]
    print(group)
    if group == '2':
        return "You are eligible for up to 200000 of loan"
    elif group == '1':
        return "You are eligible for up to 100000 of loan"
    elif group == '0':
        return "You are eligible for up to 50000 of loan"
Product("Male",'56','65546')