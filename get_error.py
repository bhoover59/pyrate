def get_error(df, col_name):
    '''Get standard error of the mean (SEM) for input column (string)'''
    sigma = df[col_name].std()
    SEM = sigma / np.sqrt(24)
    error_low = df[col_name] - SEM
    error_high = df[col_name] + SEM
    return error_low, error_high, SEM, sigma
