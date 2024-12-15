def create_equipment_library():
    equipment_library = pd.DataFrame({
        'equipment_name': ['Chiller_A', 'Chiller_B', 'Chiller_C'],
        'equipment_type': ['Chiller', 'Chiller', 'Chiller'],
        'rated_power': [500, 600, 450],  # kW
        'rated_cop': [5.0, 5.5, 4.8],   # COP
        'maintenance_cost_per_year': [10000, 12000, 9000],  # $
        'lifetime_years': [15, 20, 10],
        'purchase_cost': [100000, 150000, 80000]  # $
    })
    return equipment_library
