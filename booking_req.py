import requests as req
import json
url = "https://actgt74bvg.execute-api.ap-south-1.amazonaws.com/dev"
def sign_up():
    header = {'Content-Type': 'application/json','Accept': 'application/json'}
    data = {'user_name':'mrkrao','password':'test123','email':'mrkrao.com'}
    r = req.post('https://actgt74bvg.execute-api.ap-south-1.amazonaws.com/dev/signup',data = json.dumps(data),headers = header)
    print(r.text)
sign_up()
def log_in(url):
    header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    data = {'user_name': 'abcdefghi', 'password': 'abcdefgh'}
    r = req.post(url + '/login', data=json.dumps(data), headers=header)
    return r.text
# print(log_in(url))

def book_ticket(url):
    token = "1656068690:abcdefghi"
    header = {'Content-Type': 'application/json', 'Accept': 'application/json','Auth':token}
    data = {'bus_id': '1002', 'date': '29-06-2022','time':'07:00'}
    r = req.post(url + '/book_ticket', data=json.dumps(data), headers=header)
    return r.text
# print(book_ticket(url))

def booking_history(url):
    token = "1656068690:abcdefghi"
    header = {'Content-Type': 'application/json', 'Accept': 'application/json','Auth':token}
    r = req.get(url + '/booking_history', headers=header)
    return r.text
# print(booking_history(url))
# 1657096190:mrkrao