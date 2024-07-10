import numpy as np
def replace_negatives_with_zeros(df, column_name):
    df[column_name] = np.where(df[column_name] < 0, 0, df[column_name])
    return df
