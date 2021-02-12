import requests
import json

# link do api https://cat-fact.herokuapp.com/facts/random
animal_type = 'cat'
url = "https://cat-fact.herokuapp.com/facts/random?animal_type={}".format(animal_type)
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
json = json.loads(response.text)
# Wyświetlenie items
print(json.items())

# -----------------------------------
# sprawdzanie kluczy
expected = ['status', 'type', 'deleted', 'updatedAt', 'createdAt', 'user', 'text', '__v']
current = []

for key, value in json.items():
    if key in expected:
        current.append(key)

expected.sort()
current.sort()
assert expected == current
# Wyświetlenie wartości oczekiwanej i aktualnej
print(expected)
print(current)
# -----------------------------------
# sprawdzanie odpowiedzi
assert response.status_code == 200
# Wyświetlenie odpowiedzi
print(response.status_code)
# -----------------------------------
# sprawdzanie niepoprawnego zapytania
url = "https://cat-fact.herokuapp.com/facts/a?animal_type={}".format(animal_type)  # zmiana endpointu z random na a
response = requests.request("GET", url)
assert response.status_code == 400
# Wyświetlenie odpowiedzi
print(response.status_code)
