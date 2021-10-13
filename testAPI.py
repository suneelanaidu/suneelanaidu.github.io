import requests

url = "https://weatherapi-com.p.rapidapi.com/ip.json"

querystring = {"q":"209.66.205.197"}

headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "e2d0d1a7efmsh5668be741c711ffp1a3e44jsnfc9e0a91c2b2"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)