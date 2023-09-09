def get_error(df, col_name):
    '''Get standard error of the mean (SEM) for input column (string)'''
    sigma = df[col_name].std()
    N = len(df[col_name])
    SEM = sigma / np.sqrt(N)
    error_low = df[col_name] - SEM
    error_high = df[col_name] + SEM
    return error_low, error_high, SEM, sigma
