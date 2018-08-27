        def _met_agent_dummy(*args, **kwargs):
            return met_agent(*args[1:], **kwargs)

        # Passing this function with these arguments to load_save_merge_to_local
        #df_meteo = met_agent(train_st, train_en, available_dates, model_params, indexers,
        #                     point_values, mdl_type, freq, nation, FConfig,
        #                     farms_matrix, fc_mode='train')

        df_meteo = load_save_merge_to_local(load_func=_met_agent_dummy,
                                      func_args=(None, train_st, train_en, available_dates, model_params, indexers,
                                                 point_values, mdl_type, freq, nation, FConfig, farms_matrix),
                                      func_kwarqs={'fc_mode': 'train'},
                                      filepath=meteo_path,
                                      data_type='pd',
                                      mode=FConfig['meteo_mode'])
