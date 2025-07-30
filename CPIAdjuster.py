def get_cpi_data():
    return {
        2010: 218.056,
        2011: 224.939,
        2012: 229.594,
        2013: 232.957,
        2014: 236.736,
        2015: 237.017,
        2016: 240.007,
        2017: 245.120,
        2018: 251.107,
        2019: 255.657,
        2020: 258.811,
        2021: 270.970,
        2022: 292.655,
        2023: 305.322,
        2024: 314.195,
        2025: 320.000
    }

def adjust_prices_for_inflation(df, price_col = 'Hourly Average Price', base_year = 2025):
    cpi_data = get_cpi_data()

    if 'Timestamp' not in df.columns:
        raise ValueError("DataFrame must contain a 'Timestamp' column.")
    
    df['Year'] = df['Timestamp'].dt.year
    df['CPI'] = df['Year'].map(cpi_data)

    base_cpi = cpi_data.get(base_year)
    if base_cpi is None:
        raise ValueError(f"Base year {base_year} CPI not found in data.")
    
    df['Real Price'] = df[price_col] * (base_cpi / df['CPI'])
    return df