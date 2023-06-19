import requests  # API Ballsquad  
import pandas as pd   
import json  
import datetime as dt  




    
def import_data(url ,key)  :  #Import Data from The Api 
    response = requests.get(url ,auth=key)    
    if response.status_code==200:  
        json=response.json()
        df=pd.DataFrame(json)  
        
        return df  
    else: 
        print("erreur") 


   


def Number_of_page(url ,key) : #Number of page in the Api 
    pages=1
    response = requests.get(url+str(pages), auth=key) #we take first page    
    json=response.json()
    df=pd.DataFrame(json) 
    while df.empty == False : 
        pages=pages+1 
        response = requests.get(url+str(pages), auth=key)   
        json=response.json()
        df=pd.DataFrame(json) 
         
    return  pages-1   
    
    

 

def drop_database (conn,yes='yes'): # Drop database 
    conn.query("match (n) detach delete n ")
    const = conn.query("CALL db.constraints")
      
    print("Database are Droped")