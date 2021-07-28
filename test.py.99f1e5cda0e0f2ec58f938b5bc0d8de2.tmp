import requests

response = requests.get("http://127.0.0.1:8000")
header = {'accept: application/json','Content-Type: application/json'}
print(response.text)
params = [{"content":"Pakistan have won the world cup in 1992","comments":["waooo","not bad"]}]
article = requests.post(f"http://127.0.0.1:8000/article/",json=params)


data_dick = article.json()
data_dick.keys()
print(article.text)
print(data_dick.keys())
print(list(data_dick["ents"][1].values())[0])

