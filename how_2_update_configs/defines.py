ETL_CONFIG = dict(
    MONGO_TARGET_GROUPS_PR=['Data_for_Prediction.xlsx'],
    TIME_SERIES_OPEN_COLUMNS=["open", "open_u"],
    TIME_SERIES_CLOSE_COLUMNS=["close", "volume", "high_u", "low_u", "last_u"],
    TIME_SERIES_COLUMNS_EXT=["open", "close", "name"],  
    TIME_SERIES_CLOSE_COLUMNS_FUT=['close', 'name'],
    TIME_SERIES_OPEN_COLUMNS_FUT=['open', 'name'],
)

