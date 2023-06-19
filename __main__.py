#!/usr/bin/env python
# coding: utf-8

# In[1]:
#%%
import timeit
import mange_func as mf 
import Clean_df as CF 
import Nodes_maker 
import edges_maker 
import mN as mN # megration Nodes func 
import migration_edges as mE 
import BI_Migration_func 
import py2neo  
from urls_passwords import *  
import requests  
import tqdm  
import pandas as pd 

f = open('key.txt') #import key from file   
key1 = f.readline() 

graph=py2neo.Graph(httpneo, auth=(user, password), name="neo4j")

class BearerAuth(requests.auth.AuthBase): # key communication 
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r 
    
    



# In[2]:

#%%
def migrate_NU() :
    df=mf.import_data(urlUsers, BearerAuth(key1)) #importing
    df=CF.clen_user_nodes(df)   # trasform and clean 
    mN.migration_user(df, graph=graph) # migrate

    


# In[3]:


def migrate_court (): 
    for i in tqdm.tqdm(range(0,mf.Number_of_page(urlCourt1,BearerAuth(key1))+1)):
        urlx=urlCourt1+str(i)
        dx=mf.import_data(urlx ,BearerAuth(key1)) 
        mN.migration_court(dx,graph=graph)


# In[ ]:
def mig_creation_():
    for i in tqdm.tqdm(range(0,mf.Number_of_page("Data_API",BearerAuth(key))+1)):
        url="Data_API"+str(i)
        df=mf.import_data(url ,key=BearerAuth(key))
        BI_Migration_func.BI_USERS_creation(df,graph=graph)




# In[4]:


def migrate_facil(): 
    for i in tqdm.tqdm(range(0,mf.Number_of_page(urlstade ,BearerAuth(key1))+1)) : 
        df=mf.import_data(urlstade+str(i) ,BearerAuth(key1))   
        mN.migration_staduim(df=df,graph=graph) 


# In[5]:


def migrate_City_district(): 
    mN.migration_City(df=mf.import_data(urlcity ,BearerAuth(key1) ),graph=graph) 
    mN.migration_dist(df=mf.import_data(urlDist ,BearerAuth(key1) ), graph=graph) 


# In[6]:


def migrate_edges (): 
    for i in tqdm.tqdm(range(0,mf.Number_of_page(urlstade ,BearerAuth(key1))+1)):
        urls=urlCourt1+str(i)
        df=mf.import_data(urls,BearerAuth(key1))  
        mE.belon_to_staduim(df,graph=graph)  
    mE.belon_to_staduim(df ,graph=graph) 
    print('Court ==Belongs==> Facility  Done!!')
    df=mf.import_data(urlDist,BearerAuth(key1)) 
    mE.belon_to_City(df , graph=graph)  
    print('District ==IN==> City  Done!!')   
    for i in tqdm.tqdm(range(0,mf.Number_of_page(urlstade ,BearerAuth(key1))+1)) : 
        df=mf.import_data(urlstade+str(i),BearerAuth(key1))   
        mE.belon_to_dist(df , graph=graph) 
    print('Facility ==located==> District  Done!!')  
    court_ids=graph.query("MATCH (n:Court) return n.id_").to_data_frame() 
    list_id=court_ids["n.id_"] 
    for idc in tqdm.tqdm(list_id) : 
        df=mf.import_data(CF.req(idc,i=2),BearerAuth(key1)) 
        if df.empty == False : 
            df=edges_maker.user__court(df) 
            #df=CF.clen_df_Bookings(df) 
            df['first booking date']=CF.ch_time(df['first booking date']) 
            df['last booking date']=CF.ch_time(df['last booking date']) 
            mE.user_to_c(df , graph=graph) 
    print('User ==BOOKS==> Court  Done!!')  
    
    
    
    
    
    


# In[9]:



def migra_BI ():  
    court_ids=graph.query("MATCH (n:Court) return n.id_").to_data_frame() 
    list_id=court_ids["n.id_"]
    for ido in tqdm.tqdm(list_id) : 
        df=mf.import_data(CF.req2(ido),BearerAuth(key1))  
        if df.empty== False:
            df1=CF.resume_com(df)  # summrize BI information 
            df1['index1'] = df1.index 
        else: 
            pass
        BI_Migration_func.Com_add(df1=df1,graph=graph) #add to nodes 
    
        pass 
    print("COMM hours Done!")


def migra_userBI():
    court_ids=graph.query("MATCH (n:Court) return n.id_").to_data_frame()
    list_id=court_ids["n.id_"]
    for ido in tqdm.tqdm(list_id):
        df=mf.import_data(CF.req(ido) , BearerAuth(key))
        if df.empty == True:  # In[10]:
            pass
        else:
            df=CF.BI_info(df)
            df=Nodes_maker.Node_user2(df) #summrize BI information
            print(df)
            BI_Migration_func.BI_USERS(df ,graph=graph)

        #%%



#%%



if __name__ == "__main__":
    mf.drop_database(graph) # clean data base 
    start = timeit.default_timer()
    migrate_NU() # migrate Nodes
    migrate_court() 
    migrate_facil() 
    migrate_City_district()
    mig_creation_()
    print("All nodes entities are done !") 
    #migra_BI () #migrate BI
    #migra_userBI()###
    migrate_edges ()  # Migrate edges 
    stop = timeit.default_timer()
    print('Time of Migration ', round((stop - start)/60), "Minute")

#%%


#%%
    


    
    
    
    






