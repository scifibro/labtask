import pandas as pd
from database.db import conn
from pandas.io.sql import read_sql
from database.commands import get_view_processed


def get_df_from_query(query, db_connection):
    """gets pandas dataframe from database"""
    df = read_sql(query, db_connection)
    return df


def get_data_by_region(df, region):
    """creates subset of dataframe by region"""
    df_region = df[df['region'] == region]
    return df_region


view_processed = get_df_from_query(get_view_processed, conn)
view_processed['date'] = pd.to_datetime(view_processed['year'].astype(str) + '-' + view_processed['month'], format='%Y-%m').dt.strftime('%Y-%m')
regions = sorted(view_processed['region'].unique()) # all regions list


#addition visualizations from me


#view_processed_second = get_df_from_query(get_view_processed_second, conn)
#view_processed_second['date'] = pd.to_datetime(view_processed_second['year'].astype(str) + '-' + view_processed_second['month'], format='%Y-%m').dt.strftime('%Y-%m')
#view_processed_day = get_df_from_query(get_view_processed_with_day, conn)



