import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True, axis=0)


if __name__ == '__main__':
    data1 = {'student_id': [1, 2, 3, 4],
             'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
             'age': [8, 6, 15, 17]}
    df1 = pd.DataFrame(data1)

    data2 = {'student_id': [5, 6],
             'name': ['Leo', 'Alex'],
             'age': [7, 7]}
    df2 = pd.DataFrame(data2)
    result = concatenateTables(df1, df2)
    print(result)
