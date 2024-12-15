from flask import Flask, jsonify
from data_cleaning import fetch_and_clean_data
from efficiency_calculation import calculate_efficiency

app = Flask(__name__)

# 定义一个 API 接口，返回处理后的性能数据
@app.route('/api/performance', methods=['GET'])
def get_performance():
    # 数据清洗
    df = fetch_and_clean_data()
    # 计算 COP 效率
    df = calculate_efficiency(df)
    # 返回 JSON 数据
    return jsonify(df.to_dict(orient='records'))

# 定义一个默认页面
@app.route('/')
def index():
    return "HVAC 系统性能分析 API 已启动！"

if __name__ == "__main__":
    app.run(debug=True)
