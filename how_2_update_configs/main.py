import defines as defines ## Default defines used for several projects


from optparse import OptionParser, make_option
option_list = [
    make_option("-c", "--config",default=None),
]
parser = OptionParser(option_list=option_list)
(options, args) = parser.parse_args()


####
#### Take the default config
config = defines.ETL_CONFIG.copy() 


if options.config is not None: ## update the default config in case it's needed
    import importlib
    defines_diff = importlib.import_module(options.config)
    config_diff = defines_diff.ETL_CONFIG.copy()
    config.update(config_diff)

print(config) ## new config with updated variables


   
