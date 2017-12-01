import numpy as np
import sys

FConfig={
        'dbConnectionString_Source' : 'DWENP_EXA.WORLD',
        'dbConnectionString_Password' : 'dh_den_stage',
        'dbConnectionString_Username' : 'dh_den_stage',
    }

import MeteoDB as md
db = md.Oracle()
#db = md.OracleSP() #store procedure --> in case it's a sql function you want to call                                                                                                   
db.connect(FConfig)

farm_id = 3
forecastdate=datetime.now()

#A long and boring sql string
## Put no ; at the end (invalid character)                                                                                                                                              
## Use double quotation to hold the query (single ones are used for strings in the query)  

sql_str=("merge into F_PRODUCTION_FARM_H T using ("+
         "select forecastdate, valuedate, farm_id, value_10, value_25, value_75, value_90"+
         " from f_production_farm_h_sens"+
         " where farm_id=" + str(farm_id) +" and model_type = 'PERC' and provider = 510 and technology = 1 and forecastdate >= "+ str(forecastdate) +
         ") S on (T.valuedate=S.valuedate and T.forecastdate = S.forecastdate and T.farm_id = S.farm_id and T.provider=51 and T.technology = 1 and T.model_type='DET')"+
         " when matched then"+
         " update set T.value_10=S.value_10, T.value_25=S.value_25, T.value_75=S.value_75, T.value_90=S.value_90")

##A simple query to test the code                                                                                                                   
#sql_str= ("select * from dh_den_stage.f_production_farm_h_new where farm_id=247 and model_type='PERC'")                                                                                
print(sql_str)

db.execute_str(sql_str)
##If it's a query, fetch the result
#print(np.array(db.cursor.fetchall ())) #In case you want to fetch the query results                                                                                                    
db.disconnect()

