import pandas as pd   
import datetime as dt  



  
def paid (stsd):
    if stsd==2 or stsd==6 or stsd==4 : 
        return 0 
    else : 
         return 1 
        


def Node_user2(dita) :    
     data2=dita.groupby(['userId']).agg(
     gross_amout_payed=('courtGrossAmount',sum) ,  
     totalCost=('totalCost',sum) , 
      Duration=('Duration',sum)
     )
     return data2




def Node_courts(dita):   
    data_transction['cancelled.Book']=data_transction['statusId'].map(lambda t : paid(t))  
    data2=dita.groupby(['courtId']).agg(
     Num_cancel=('cancelled.Book',sum) ,  
     courtGrossAmount=('courtGrossAmount',sum) , 
     Frist_apparition=('datetime' , min) 
     )  
    data3=pd.DataFrame(dita.groupby('Court.ID').size() , columns=['Num.Booking']) 
    Court=data3.join(data2)  
    return Court    



