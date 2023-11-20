def calculate_pivot_points(data):
    # Pivot Point hesapla
    data['Pivot_Point'] = (data['high'] + data['low'] + data['close']) / 3

    # Destek ve Direnç seviyelerini hesapla
    data['Support_1'] = data['Pivot_Point'] - 0.382 * (data['high'] - data['low'])
    data['Support_2'] = data['Pivot_Point'] - 0.618 * (data['high'] - data['low'])
    data['Support_3'] = data['Pivot_Point'] - 1 * (data['high'] - data['low'])

    data['Resistance_1'] = data['Pivot_Point'] + 0.382 * (data['high'] - data['low'])
    data['Resistance_2'] = data['Pivot_Point'] + 0.618 * (data['high'] - data['low'])
    data['Resistance_3'] = data['Pivot_Point'] + 1 * (data['high'] - data['low'])

    return data