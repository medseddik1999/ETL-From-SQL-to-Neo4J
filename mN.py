import requests  # API Ballsquad  
import pandas as pd   
import json  
import py2neo  ## concet to Neo4j 
import datetime as dt  
import tqdm  
import itertools



def migration_user(df,graph):    
   
    try:
        graph.run("MATCH (n:User) DETACH DELETE  n ") # delete all nodes if they exists  
    except:
         print("Is Clean") 
    
    try:
        graph.run("CREATE CONSTRAINT ON (n:User) ASSERT n.id_ IS UNIQUE") # red is Cypher 
    except:
         print("Constraint already exists")  
    iteration = 0  ## for spliting the megration 
    transaction_list = []
    for i in range(len(df)):
      # Append a dict, 1 dict per person 
        transaction_list.append({ 'id_':int(df['userId'][i]),'firstName':str(df['firstName'][i]),                 'lastName':str(df['lastName'][i]), 
                                 'email':str(df['email'][i]),'birthDate':str(df['birthDate'][i]),
                                 'langKey':str(df['langKey'][i]),'gender':str(df['gender'][i]) , 
                                  'attack':int(df['attack'][i]), 'defense':int(df['defense'][i]), 'speed':int(df['speed'][i]), 
                                'jump':int(df['jump'][i]),'physicalQualities':int(df['physicalQualities'][i]) })
                                                                                   ##for take information user by user 
        iteration += 1
        if i % 1000 == 0: # condition of split 
        # To commit a list of transaction with cypher you can use the UNWIND parameter
        # $json => json will be the argument of run with the data
            transaction = "UNWIND $json as data CREATE (n:User) SET n = data"
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list) 
    
    
    
    

    
def migration_court(df,graph): 
    try:
        graph.run("CREATE CONSTRAINT ON (n:Court) ASSERT n.id_ IS UNIQUE") # red is Cypher 
    except:
         print("Constraint already exists")
    
    iteration = 0  ## for spliting the megration 
    transaction_list = []
    for i in range(len(df)):
      # Append a dict, 1 dict per person 
        transaction_list.append({ 'id_':int(df['id'][i]),'name':str(df['name'][i]), 'status':str(df['status'][i]), 
                                 'defaultHourlyRate':str(df['defaultHourlyRate'][i]),
                                 'openTime':str(df['openTime'][i]),'closeTime':str(df['closeTime'][i]),
                                 'courtGrossHourlyRate':str(df['courtGrossHourlyRate'][i]),
                                 'maxBookingLimit':str(df['maxBookingLimit'][i]) 
                                }) ##for take information user by user 
        iteration += 1
        if i % 1000 == 0: # condition of split 
        # To commit a list of transaction with cypher you can use the UNWIND parameter
        # $json => json will be the argument of run with the data
            transaction = "UNWIND $json as data CREATE (n:Court) SET n = data"
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list)  
    
    


def migration_court_2(df,graph): 
     
    try:
        graph.run("CREATE CONSTRAINT ON (n:Court) ASSERT n.id_ IS UNIQUE") # red is Cypher 
    except:
         print("Constraint already exists")
    
    iteration = 0  ## for spliting the megration 
    transaction_list = []
    for i in range(len(df)):
      # Append a dict, 1 dict per person 
        transaction_list.append({ 'id_':int(df['id'][i]),'name':str(df['name'][i]), 'status':str(df['status'][i]), 
                                 'defaultHourlyRate':str(df['defaultHourlyRate'][i]),
                                 'openTime':str(df['openTime'][i]),'closeTime':str(df['closeTime'][i]),
                                 'courtGrossHourlyRate':str(df['courtGrossHourlyRate'][i]),
                                 'maxBookingLimit':str(df['maxBookingLimit'][i]) 
                                }) ##for take information user by user 
        iteration += 1
        if i % 1000 == 0: # condition of split 
        # To commit a list of transaction with cypher you can use the UNWIND parameter
        # $json => json will be the argument of run with the data
            transaction = "UNWIND $json as data CREATE (n:Court) SET n = data"
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list)  
    
       
def migration_staduim(df,graph): 
    
    try:
        graph.run("CREATE CONSTRAINT ON (n:Facility) ASSERT n.id_ IS UNIQUE") # red is Cypher 
    except:
         print("Constraint already exists")  
    iteration = 0  ## for spliting the megration 
    transaction_list = []
    for i in range(len(df)):
      # Append a dict, 1 dict per person 
        transaction_list.append({ 'id_':int(df['id'][i]),'name':str(df['name'][i]),'status':str(df['status'][i]),
                                 'longitude':float(df['longitude'][i]),'latitude':float(df['latitude'][i]),
                                'postalCode':str(df['postalCode'][i]) ,'streetAddress':str(df['streetAddress'][i]) ,
                                                 }) ##for take information item by item 
        iteration += 1
        if i % 1000 == 0: # condition of split 
        # To commit a list of transaction with cypher you can use the UNWIND parameter
        # $json => json will be the argument of run with the data
            transaction = "UNWIND $json as data CREATE (n:Facility) SET n = data"
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list)   
    


def migration_City(df,graph): 
    
    try:
        graph.run("CREATE CONSTRAINT ON (n:City) ASSERT n.id_ IS UNIQUE") # red is Cypher 
    except:
         print("Constraint already exists")  
    iteration = 0  ## for spliting the megration 
    transaction_list = []
    for i in range(len(df)):    
      # Append a dict, 1 dict per person 
        transaction_list.append({ 'id_':int(df['id'][i]),'name':str(df['name'][i]),
                                 'longitude':float(df['longitude'][i]),'latitude':float(df['latitude'][i])
                                 }) ##for take information user by user 
        iteration += 1
        if i % 1000 == 0: # condition of split 
        # To commit a list of transaction with cypher you can use the UNWIND parameter
        # $json => json will be the argument of run with the data
            transaction = "UNWIND $json as data CREATE (n:City) SET n = data"
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list) 
    

    

def migration_dist(df,graph): 
    
    try:
        graph.run("CREATE CONSTRAINT ON (n:District) ASSERT n.id_ IS UNIQUE") # red is Cypher 
    except:
         print("Constraint already exists")  
    iteration = 0  ## for spliting the megration 
    transaction_list = []
    for i in range(len(df)):
      # Append a dict, 1 dict per person 
        transaction_list.append({'id_':int(df['id'][i]),'name':str(df['name'][i])}) ##for take information user by user 
        iteration += 1
        if i % 1000 == 0: # condition of split 
        # To commit a list of transaction with cypher you can use the UNWIND parameter
        # $json => json will be the argument of run with the data
            transaction = "UNWIND $json as data CREATE (n:District) SET n = data" 
            graph.run(transaction, json=transaction_list)
            transaction_list = []

    graph.run(transaction, json=transaction_list)