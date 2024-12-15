from data_cleaning import fetch_and_clean_data
from equipment_library import create_equipment_library
from efficiency_calculation import calculate_efficiency
from investment_analysis import investment_analysis

def main():
    # 1. 数据收集与清洗
    data = fetch_and_clean_data()
    print("数据清洗完成：", data.head())

    # 2. 设备库构建
    equipment = create_equipment_library()
    print("设备库构建完成：", equipment)

    # 3. 效率计算
    efficiency_data = calculate_efficiency(data)
    print("效率计算结果：")
    print(efficiency_data[['timestamp', 'COP']])

    # 4. 投资决策分析
    investment_results = investment_analysis(equipment)
    print("投资决策分析结果：")
    print(investment_results)

if __name__ == "__main__":
    main()
