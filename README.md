# 1. 数据收集与清洗
工作内容：
从客户已有的暖通系统实时数据平台获取数据（通过API或数据库连接）。
数据包括：

时间序列：室内外温度、湿度、机组耗电量、流量、阀门开度、风机启停状态、机组运行功率、负荷数据等
维护记录及设备基本信息
处理手段：

编写Airflow任务定期拉取数据（例如每小时）
使用Pandas进行数据清洗与特征提取（如计算每天平均COP，统计机组启停次数等）

# 2. 设备库构建
工作内容：
建立一个数据表（设备库），存储各类暖通设备的参数：

设备类型（风机盘管、冷水机组、锅炉、热交换器等）
额定功率、额定工况下的COP或EER
可运行负荷范围、维护周期与成本、寿命年限、价格信息等
该设备库可用来在投资模型中选用可替代设备，从而进行改造方案评估。

# 3. 效率计算模型
基于实时运行数据计算系统效率指标，例如：
COP（Coefficient of Performance）计算：
COP=制冷量或制热量/机组功耗
制冷量可通过测量供回水温差与水流量估算：
Q=mCp(Treturn-Tsupply)

# 4. 投资与改造决策模型
思路：
对于每种改造方案（例如更换现有冷水机组为更高COP机组），可设定：

新设备采购成本
改造实施费用
预期的能耗降低比例
由此估算未来5-10年的节能收益（电费节省）
计算净现值（NPV）与内部收益率（IRR）
选择ROI最高的方案作为推荐

# 5. 模拟与验证
引入EnergyPlus等仿真工具或采用简化模型，将历史气候条件、室内需求负荷与设备特性输入模型中，仿真不同改造方案下的年度能耗情况。

工具：

使用Python的eppy包操控EnergyPlus输入文件（IDF文件），动态修改设备参数与运行策略，然后运行EnergyPlus仿真，获得输出能耗数据。

# 6. 自动化数据集成与展示
使用Airflow调度以下任务：

定期拉取实时数据更新数据库
运行模型计算当前COP与历史趋势
运行改造方案评估，更新ROI与NPV分析结果
将结果输出至前端API接口
前端使用Flask/Dash构建Web界面，图表用Plotly显示能效指标趋势、投资回报分析折线图和条形图。

# 评分要点保证措施
模型的准确度：
通过历史数据与基准案例验证模型结果，并进行参数校准，使模拟结果与实际能耗数据的偏差降至可接受范围内（如<5%）。
优化COP计算方法，确保输入数据可靠性。

软件的使用体验：
提供简洁明了的前端界面，清晰显示能耗趋势、COP变化、改造方案的NPV和ROI对比，提供可交互的情景切换与导出报告功能。

数据的自动倒入集成：
采用Airflow自动化工作流，在后台定期执行数据同步与模型计算。
确保数据管道可靠性并自动更新前端可视化结果。

