import requests 
import pandas as pd 
import time

def dataFetch () :
 all_anime = []
 pages = 1

 while True:
   
   url1 = "" 
   url = f"https://api.jikan.moe/v4/anime?page={pages}"
   response1 = requests.get(url1)
   response = requests.get(url)

   if (response.status_code == 200):
      
      data = response.json()
      anime_list = data["data"]
      
      if not anime_list :
        break
      print("Data fetched!") 

      
      for anime in anime_list :
          all_anime.append({
          "title" : anime["title"],
          "episodes" : anime["episodes"],
          "status" : anime ["status"],
            "rating": anime["rating"],
            "genres": [genre["name"] for genre in anime["genres"]],})
          
      print(f'page fetched {pages}') 
      pages += 1
      time.sleep(3)
    

   else:
      print(f"Data fetching failed {response.status_code}")
      print(response.text)
  
 df = pd.DataFrame(all_anime)
 return df
   




print(dataFetch())  
 
 
   



