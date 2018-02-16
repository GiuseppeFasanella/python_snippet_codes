########config.py

def load():
    FConfig={
        'dbConnectionString_Main' : 'Use_args', #'PROD','TEST', 'Use_args'                                                                                                              
        'dbConnectionString_Prod' : 'DWHP',
        'dbConnectionString_Test' : 'DWHD',
        'dbConnectionString_Password' : 'dh_den_stage',
        'dbConnectionString_Username' : 'dh_den_stage',
        'LOG_PATH': '/home/gfasanella/devel/logs/Perc_aggregation/', #gfasanella/devel --> home/production                                                                              
        'send_mail_on_error' : 0,
        'save_plot' : 0,
        'coef_table_name' : 'F_METEO_PERCENTILE_COEF',
        'coef_table_name_aux' : 'T_METEO_PERCENTILE_COEF',
        'write_to_DB' : 1,
        'technology' : 1,
        'nation' : 'ITA',
        'Wind_DufEnergyFarms_Info' : '/srv/meteodata/Data_repository/WindFarm_DB/DufEnergyFarms/WindITA_DufEnergyFarmsInfo.csv'
    }

    return FConfig
###############

###nel main:
import config

FConfig = config.load()
