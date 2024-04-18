import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    low_fat_y = products[products['low_fats'] == 'Y']
    recycble_y = low_fat_y[low_fat_y['recyclable'] == 'Y']
    result = recycble_y[['product_id']]

    # equivalent to: products[(products['low_fats']  == 'Y') & (products['recyclable'] == 'Y')][['product_id']]
    return result


if __name__ == '__main__':
    data = {
        'product_id': [0, 1, 2, 3, 4],
        'low_fats': ['Y', 'Y', 'N', 'Y', 'N'],
        'recyclable': ['N', 'Y', 'Y', 'Y', 'N']
    }

    df = pd.DataFrame(data)
    result = find_products(df)
    print(result)
