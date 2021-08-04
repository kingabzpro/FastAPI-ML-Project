import requests

response = requests.get("http://127.0.0.1:8000")
header = {'accept': 'application/json','Content-Type': 'application/json'}
print(response.text)

params = [
            {
                "content": "The 1992 Cricket World Cup was won by Pakistan",
                "comments": ["waooo", "not bad"],
            }
         ]

article = requests.post(f"http://127.0.0.1:8000/article/",headers = header,json=params)

data_dict = article.json()

print("Label: ",list(data_dict["ents"][1].values())[1])
print("Text: ",list(data_dict["ents"][1].values())[0])