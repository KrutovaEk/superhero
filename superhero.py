import requests
# from operator import itemgetter


ids={332:"Hulk", 149:"Captain America", 665:"Thanos"}
superhero=[]
for key, value in ids.items():
    url_1 =f"https://akabab.github.io/superhero-api/api/powerstats/{key}.json"
    resp_1 = requests.get(url_1)
    resps_1=resp_1.json()
    resps_1['name']=value 
    superhero.append(resps_1)

# superhero.sort(key=itemgetter('intelligence'))
# print(superhero)

intelligences_max=0
name_superhero=()
for super in superhero:
    intelligences=super.get('intelligence')
    name=super.get('name')
    print(f'Интелект {name} равен {intelligences}')

    if intelligences>intelligences_max:
        intelligences_max = intelligences
        name_superhero= name
print(f'Самый умный супергерой {name_superhero}')

