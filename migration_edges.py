import requests  # API Ballsquad  
import pandas as pd   
import json  
import py2neo  ## concet to Neo4j 
import datetime as dt  
import tqdm 
import math



def user_to_c (df , graph) : 
    
    transaction = """UNWIND $json as data
        MATCH (a:User),(b:Court)
        WHERE a.id_ = data.id_1 AND b.id_ = data.id_2
        MERGE (a)-[r:BOOKS_FOR{NumBookings : data.NumBookings, NumCancel: data.NumCancel,First_booking:data.First_booking,
                     Last_booking:data.Last_booking }]->(b) 
        
         """ 
    

    transaction_list=[]
    it = 0   
    for index, row in tqdm.tqdm(df.iterrows()):
        sh1 = row['users id']
        sh2 = row['court id']
        sh3= row['num_bookig']
        sh4= row['num_cancel'] 
        sh5=row['first booking date'] 
        sh6=row['last booking date']
        transaction_list.append({"id_1":int(sh1),"id_2":int(sh2) ,"NumBookings":int(sh3) ,"NumCancel":int(sh4),
                                 "First_booking":str(sh5) , "Last_booking":str(sh6)}) 
        it +=1 
        #print(transaction_list)
        if it % 1000 == 0:
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list)  
    

    

def belon_to_dist(df , graph) : 
    
    transaction = """UNWIND $json as data
        MATCH (a:Facility),(b:District)
        WHERE a.id_ = data.id_1 AND b.id_ = data.id_2
        MERGE (a)-[r:LOCATED_AT]->(b)
         """
   
    transaction_list=[]
    it = 0   
    for  i in tqdm.tqdm(range(len(df))):
        sh1 = df['id'][i]
        sh2 = df['districtId'][i] 
        if math.isnan(sh2) == False : 
            transaction_list.append({"id_1":int(sh1),"id_2":int(sh2)})
            it +=1 
            #print(transaction_list)
            if it % 1000 == 0:
                graph.run(transaction, json=transaction_list)
                transaction_list = []

    graph.run(transaction, json=transaction_list) 




def belon_to_City(df , graph) : 
    
    transaction = """UNWIND $json as data
        MATCH (a:District),(b:City)
        WHERE a.id_ = data.id_1 AND b.id_ = data.id_2
        MERGE (a)-[r:I_N]->(b)
         """
   
    transaction_list=[]
    it = 0   
    for  i in tqdm.tqdm(range(len(df))):
        sh1 = df['id'][i]
        sh2 = df['cityId'][i] 
        if math.isnan(sh2) == False : 
            transaction_list.append({"id_1":int(sh1),"id_2":int(sh2)})
            it +=1 
            #print(transaction_list)
            if it % 1000 == 0:
                graph.run(transaction, json=transaction_list)
                transaction_list = []

    graph.run(transaction, json=transaction_list) 
    
    
    
    

    
def belon_to_staduim (df , graph) : 
    
    transaction = """UNWIND $json as data
        MATCH (a:Court),(b:Facility) 
        WHERE a.id_ = data.id_1 AND b.id_ = data.id_2
        MERGE (a)-[r:BELONGS_TO]->(b)
         """
   
    transaction_list=[]
    it = 0   
    for  i in tqdm.tqdm(range(len(df))):
        sh1 = df['id'][i]
        sh2 = df['stadiumId'][i] 
        transaction_list.append({"id_1":int(sh1),"id_2":int(sh2)})
        it +=1 
        #print(transaction_list)
        if it % 1000 == 0:
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list)