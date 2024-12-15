import pandas as pd
from sqlalchemy import create_engine

# 数据库连接
engine = create_engine("postgresql+psycopg2://user:password@host:port/dbname")

def fetch_and_clean_data():
    query = """
    SELECT timestamp, outdoor_temp, indoor_temp, chiller_power, airflow_rate, humidity, 
           valve_position, supply_temp, return_temp 
    FROM hvac_raw_data
    WHERE timestamp >= NOW() - INTERVAL '24 hours';
    """
    # 提取数据
    df = pd.read_sql(query, engine)
    # 清洗数据
    df = df.dropna()
    df = df[df['chiller_power'] > 0]  # 只保留有效功率数据
    return df
