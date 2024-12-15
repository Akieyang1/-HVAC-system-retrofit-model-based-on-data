import pandas as pd


def investment_analysis(equipment_library, base_energy_cost=100000):
    """
    计算设备改造的投资回报（NPV）
    参数:
        - equipment_library: 包含设备信息的 DataFrame
        - base_energy_cost: 初始能耗成本 (默认 100000 美元/年)
    返回:
        - 分析结果 DataFrame
    """
    discount_rate = 0.08  # 折现率
    years = 10

    def cash_flow(efficiency_gain_ratio, equipment_cost):
        annual_saving = base_energy_cost * efficiency_gain_ratio
        flows = [-equipment_cost] + [annual_saving] * years
        npv = sum([flows[i] / ((1 + discount_rate) ** i) for i in range(len(flows))])
        return npv

    results = []
    for _, row in equipment_library.iterrows():
        npv = cash_flow(0.15, row['purchase_cost'])  # 假设节能 15%
        results.append({'equipment_name': row['equipment_name'], 'NPV': npv})

    return pd.DataFrame(results)


if __name__ == "__main__":
    # 测试代码
    equipment_library = pd.DataFrame({
        'equipment_name': ['Chiller_A', 'Chiller_B'],
        'purchase_cost': [100000, 150000]
    })
    analysis_result = investment_analysis(equipment_library)
    print("投资决策分析结果：")
    print(analysis_result)
