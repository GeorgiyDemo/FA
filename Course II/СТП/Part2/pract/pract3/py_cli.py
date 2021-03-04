import requests

server_ip = "http://127.0.0.1:8080"

new_user = {
    "firstName" : "Деменчук",
    "lastName" : "Георгий",
    "street" : "Ул Ленина",
    "postalCode" : "233255",
    "date" : "06.05.1990"
}

#Нужно, чтоб посмотреть, что происходит
for person in requests.get(f"{server_ip}/persons").json():
    print(person)