def get_percents(df):
    df_day = df[(df['Time'] >= 8) & (df['Time'] < 20)]
    df_night = df[(df['Time'] < 8) | (df['Time'] >= 20)]
    
    # Define the rate names for production and loss rates
    production_rates = ['rateOH_NO_MCM', 'rateNO2_aerosol', 'rateNO2_ground']
    loss_rates = ['ratePhotolysis_MCM', 'rateHONO_OH_MCM', 'rateDilution', 'rateHONO_ground', 'diff']
    
    # Calculate total production for day and night
    total_day_production = np.abs(df_day[production_rates]).sum()
    total_night_production = np.abs(df_night[production_rates]).sum()
    
    # Calculate total loss for day and night
    total_day_loss = -np.abs(df_day[loss_rates]).sum()
    total_night_loss = -np.abs(df_night[loss_rates]).sum()
    
    # Calculate the percentage contribution of each production rate DAYTIME
    total_production = total_day_production.sum()
    perc_day_production = total_day_production / total_production
    
    # Calculate the percentage contribution of each production rate NIGHTTIME
    total_production_night = total_night_production.sum()
    perc_night_production = total_night_production / total_production_night
    
    # Calculate the percentage loss of each rate DAYTIME
    total_loss = total_day_loss.sum()
    perc_day_loss = total_day_loss / total_loss
    
    # Calculate the percentage loss of each rate NIGHTTIME
    total_loss_night = total_night_loss.sum()
    perc_night_loss = total_night_loss / total_loss_night
    
    return perc_day_production, perc_night_production, perc_day_loss, perc_night_loss

percents = get_percents(df_ALL)
print(percents[1])
