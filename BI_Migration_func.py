import tqdm




def Com_add(df1,graph):
    
        transaction = """UNWIND $json as data
    OPTIONAL MATCH (a:Court {id_:data.id_})
    SET a += {MounthServedNum:data.MounthServedNum,soldHours:data.soldHours,
    totalCost:totalCost+data.totalCost,courtGrossAmount:courtGrossAmount+data.courtGrossAmount,
    Meanoftotalhours:data.Meanoftotalhours, First_mounth:data.First_mounth,First_year:data.First_year} 
          """
        transction_list={'id_':int(df1['index1']) ,'soldHours':int(df1['soldHours']) ,
                      'courtGrossAmount':int(df1['courtGrossAmount']),'totalCost':int(df1['totalCost']),
                      'TotalHours':int(df1['Meanoftotalhours']) , 
                      'MounthServedNum':int(df1['MounthServedNum']),'First_mounth':int(df1['First_mounth']),
                      'First_year':int(df1['First_year'])}  

        graph.run(transaction, json=transction_list) 
    
        pass  
    
    

def BI_USERS (df , graph) :
    df['index1'] = df.index
    transction_list=[]
    for index, row in tqdm.tqdm(df.iterrows()): 
            
            transaction = """UNWIND $json as data
       OPTIONAL MATCH (a:User {id_:data.id_})
    SET a += {gross_amout_payed:data.gross_amout_payed,soldHours:data.Duration,
    totalCost:data.totalCost , BS_Fee:data.BS_Fee}   
          """
            transction_list.append({'id_':int(row['index1']) ,'gross_amout_payed':row['gross_amout_payed'] ,
                      'Duration':(row['Duration']),'totalCost':(row['totalCost'])})

    graph.run(transaction, json=transction_list)


def BI_USERS_creation (df,graph) :


    transction_list=[]
    for index,row in tqdm.tqdm(df.iterrows()):

        transaction = """UNWIND $json as data
       OPTIONAL MATCH (a:User {id_:data.id_})
    SET a += {createdDate:data.createdDate}   
          """
        transction_list.append({'id_':int(df['id'][index]),'createdDate':df['createdDate'][index]})

    graph.run(transaction, json=transction_list)
#%%
