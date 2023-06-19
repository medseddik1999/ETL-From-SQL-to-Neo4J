import pandas as pd   
import tqdm  
import numpy as np  


def paid (stsd):
    if stsd==2 or stsd==6 or stsd==4 : 
        return 0 
    else : 
         return 1 
        

        
def user__court(dita):   
    dita['cancelled.Book']=dita['statusId'].map(lambda t : paid(t)) 
    users=[] 
    court=[] 
    date=[] 
    cancel=[]
    for index , row in dita.iterrows():  
        users.append(dita['userId'][index])  
        court.append(dita['courtId'][index]) 
        date.append(dita['startDateTime'][index])  
        cancel.append(dita['cancelled.Book'][index])    
    dictpa={'User ID':users , 'Court ID': court ,'cancel':cancel , 'date': date}  
    daaata1=pd.DataFrame(dictpa)  
    userIds=[] 
    courtIds=[] 
    num_booking=[]  
    num_cancel=[]
    first_date=[] 
    last_date=[]
    for user in tqdm.tqdm(list(set(daaata1['User ID'])))  : 
        gg= daaata1[daaata1['User ID']== user]   
        for court in gg['Court ID'] : 
            dd= gg[gg['Court ID']== court]    
            userIds.append(user)  
            courtIds.append(court) 
            num_booking.append(len(dd))  
            num_cancel.append(sum(dd['cancel'])) 
            first_date.append(min(dd['date'])) 
            last_date.append(max(dd['date'])) 
    dict2={'users id':userIds , 'court id':courtIds , 'num_bookig': num_booking ,
           'num_cancel':num_cancel  , 'first booking date':first_date,
           'last booking date':last_date} 
    data1=pd.DataFrame(dict2)   
    data1.drop_duplicates(inplace=True)   
    return(data1) 






