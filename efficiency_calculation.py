def calculate_efficiency(df):
    # 假设水系统流量(kg/s)与比热容
    water_flow = 10.0  # kg/s
    Cp = 4.2           # kJ/kg.K
    # 计算冷量和COP
    df['cooling_capacity_kW'] = water_flow * Cp * (df['return_temp'] - df['supply_temp'])
    df['COP'] = df['cooling_capacity_kW'] / (df['chiller_power'] + 1e-9)  # 避免除零
    return df
