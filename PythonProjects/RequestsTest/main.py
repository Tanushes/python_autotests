import requests

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= 'df1cdbb079cc5726e12bb7f23215ee8a'
HEADER= {'Content-Type':'application/json', 'trainer_token': TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "tanushes@mail.ru",
    "password": "Iloveqa1"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "176273",
    "name": "born",
    "photo_id": 2
}

body_pokeball ={
    "pokemon_id": "176273"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''
 
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)'''

'''massage = response_create.json()['massage'] 
print(massage)''' 


'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_create.status_code)'''

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_create.status_code)
