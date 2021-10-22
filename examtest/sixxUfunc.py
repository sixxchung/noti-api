def uFunc_create_week_date(dataframe, weekcolNm='week'):
  dataframe['Month']            = pd.to_datetime(dataframe[weekcolNm]).dt.month
  dataframe['Day']              = pd.to_datetime(dataframe[weekcolNm]).dt.day
  dataframe['DayOfweek']        = pd.to_datetime(dataframe[weekcolNm]).dt.dayofweek
  dataframe['DayOfyear']        = pd.to_datetime(dataframe[weekcolNm]).dt.dayofyear
  dataframe['Week']             = pd.to_datetime(dataframe[weekcolNm]).dt.isocalendar().week
  #dataframe['Week']             = pd.to_datetime(dataframe[weekcolNm]).dt.week
  dataframe['Quarter']          = pd.to_datetime(dataframe[weekcolNm]).dt.quarter 
  dataframe['Is_month_start']   = pd.to_datetime(dataframe[weekcolNm]).dt.is_month_start
  dataframe['Is_month_end']     = pd.to_datetime(dataframe[weekcolNm]).dt.is_month_end
  dataframe['Is_quarter_start'] = pd.to_datetime(dataframe[weekcolNm]).dt.is_quarter_start
  dataframe['Is_quarter_end']   = pd.to_datetime(dataframe[weekcolNm]).dt.is_quarter_end
  dataframe['Is_year_start']    = pd.to_datetime(dataframe[weekcolNm]).dt.is_year_start
  dataframe['Is_year_end']      = pd.to_datetime(dataframe[weekcolNm]).dt.is_year_end
  dataframe['Days_in_month']    = pd.to_datetime(dataframe[weekcolNm]).dt.days_in_month
  dataframe['Semester']   = np.where(dataframe[weekcolNm].isin([1,2]),1,2)
  dataframe['Is_weekend'] = np.where(dataframe[weekcolNm].isin([5,6]),1,0)
  dataframe['Is_weekday'] = np.where(dataframe[weekcolNm].isin([0,1,2,3,4]),1,0)
  return dataframe





