import pandas as pd   
import datetime as dt   
from urls_passwords import * 



####################### For cleaning ###################
def ch_time(col)   : 
    col= pd.to_datetime(col)  
    col= col.dt.tz_localize(None) 
    return col 




def clen_user_nodes(df):
    df=df[['firstName', 'lastName', 'email', 'langKey', 'gender', 'birthDate',
       'phoneNumber', 'zipCode', 'attack', 'defense', 'speed', 'jump',
       'physicalQualities', 'userId']]    
    return df  
    



def clen_df_Bookings(df):
    df['first booking date']=ch_time(df['first booking date'])  
    df['last booking date']=ch_time(df['last booking date'])   
    return df  
######################## For  transforming##########

def BI_info (df): 
      
    df['Duration']= (ch_time(df['endDateTime']) - ch_time(df['startDateTime'])).dt.total_seconds() / 60 / 60  
    return df 

def resume_com(df):
    df1=df.groupby('courtId').agg(
         soldHours=('soldHours',sum) ,  
         totalCost=('totalCost',sum) , 
         courtGrossAmount=('courtGrossAmount',sum), 
         Meanoftotalhours=('totalHours',sum), 
         First_mounth=('month' , min), 
         First_year=('year' , min)) 
    df2=pd.DataFrame(df.groupby('courtId').size() , columns=['MounthServedNum'])  
    dfo=df2.join(df1) 
    return dfo  


###################### for API request##################
def req (id_,i=2): 
    if i==2 :
        url="Data_API"+str(id_)+"&from=2018-07-30T20%3A00%3A00&to=2022-08-30T20%3A00%3A00&size=500"
    return url  


def req2 (id_,page=0 ,i=2): 
    if i ==1:
        url=url1+str(id_)+url12+str(page)+"&size=500" 
    if i==2 :
        url="Data_API"+str(id_)+"&from=2018-01-01T20%3A00%3A00&to=2022-08-30T20%3A00%3A00&size=100000"
    return url
###############################################################


def clen_df_user_node(df):
    df['lastModifiedDate']=ch_time('lastModifiedDate')
    df['createdDate']=ch_time('createdDate')


#3460












