def plotPie(df, save_filename = None):
    ############ Calculate percents ####################
    df_day = df[(df['Time'] >= 8) & (df['Time'] < 20)]    
    df_night = df[(df['Time'] < 8) | (df['Time'] >= 20)]
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
    perc_OH_NO_production = total_day_production[0] / total_production
    perc_NO2_aerosol_production = total_day_production[1] / total_production
    perc_NO2_ground_production = total_day_production[2] / total_production
    
    # Calculate the percentage contribution of each production rate NIGHTTIME
    total_production_night = total_night_production.sum()
    perc_OH_NO_production_night = total_night_production[0] / total_production_night
    perc_NO2_aerosol_production_night = total_night_production[1] / total_production_night
    perc_NO2_ground_production_night = total_night_production[2] / total_production_night
    
    # Calculate the percentage loss of each rate DAYTIME
    total_loss = total_day_loss.sum()
    perc_photolysis_loss = total_day_loss[0] / total_loss
    perc_HONO_OH_loss = total_day_loss[1] / total_loss
    perc_dilution_loss = total_day_loss[2] / total_loss
    perc_HONO_ground_loss = total_day_loss[3] / total_loss
    perc_unknown_loss = total_day_loss[4] / total_loss
    
    # Calculate the percentage loss of each rate NIGHTTIME
    total_loss_night = total_night_loss.sum()
    perc_photolysis_loss_night = total_night_loss[0] / total_loss_night
    perc_HONO_OH_loss_night = total_night_loss[1] / total_loss_night
    perc_dilution_loss_night = total_night_loss[2] / total_loss_night
    perc_HONO_ground_loss_night = total_night_loss[3] / total_loss_night
    perc_unknown_loss_night = total_night_loss[4] / total_loss_night
    
    ############# Start plotting ###########################
    # Create a list of labels for the production pie chart with the percentage values
    labels_production = [f'OH+NO ({perc_OH_NO_production:.1%})', 
                          f'NO$_2$+aerosol ({perc_NO2_aerosol_production:.1%})', 
                          f'NO$_2$+ground ({perc_NO2_ground_production:.1%})']

    # Create a list of labels for the production pie chart with the percentage values NIGHT
    labels_production_night = [f'OH+NO ({perc_OH_NO_production_night:.1%})', 
                          f'NO$_2$+aerosol ({perc_NO2_aerosol_production_night:.1%})', 
                          f'NO$_2$+ground ({perc_NO2_ground_production_night:.1%})']
    
    # Create a list of values for the production pie chart
    values_production = [perc_OH_NO_production, perc_NO2_aerosol_production, perc_NO2_ground_production]

    # Create a list of values for the production pie chart
    values_production_night = [perc_OH_NO_production_night, perc_NO2_aerosol_production_night, perc_NO2_ground_production_night]
    # Define the colors for the production pie chart as shades of red
    colors_production = ['#328BB8','#006298', 'navy', '#63B1D3']

    
    # Create a list of labels for the loss pie chart with the percentage values
    labels_loss = [f'Photolysis ({perc_photolysis_loss:.1%})', 
                    f'HONO+OH ({perc_HONO_OH_loss:.1%})', 
                    f'Dilution ({perc_dilution_loss:.1%})',
                    f'HONO ground ({perc_HONO_ground_loss:.1%})',
                    f'Unknown ({perc_unknown_loss:.1%})']

    # Create a list of labels for the loss pie chart with the percentage values
    labels_loss_night = [f'Photolysis ({perc_photolysis_loss_night:.1%})', 
                    f'HONO+OH ({perc_HONO_OH_loss_night:.1%})', 
                    f'Dilution ({perc_dilution_loss_night:.1%})',
                    f'HONO ground ({perc_HONO_ground_loss_night:.1%})',
                    f'Unknown ({perc_unknown_loss_night:.1%})']
    
    # Create a list of values for the loss pie chart
    values_loss = [perc_photolysis_loss, perc_HONO_OH_loss, perc_dilution_loss, perc_HONO_ground_loss, perc_unknown_loss]

    # Create a list of values for the loss pie chart
    values_loss_night = [perc_photolysis_loss_night, perc_HONO_OH_loss_night, perc_dilution_loss_night, perc_HONO_ground_loss_night, perc_unknown_loss_night]
    
    # Define the colors for the loss pie chart as shades of blue
    colors_loss = ['#800020', '#E3735E', '#AA4A44', '#D2042D', '#630330']
#         colors_loss = ['#5A0C0C', '#990000', '#F23A3F', 'purple', 'black']

#     wedgeprops = {'width': 1, 'linewidth': 3.0, 'edgecolor': 'white'}
    
    # Create the subplots for the two pie charts side by side
    fig, ax = plt.subplots(2, 2, figsize=(12,8))

    # Create the production pie chart with the custom colors and labels
    # If you want labels 
    ax[0,0].pie(values_production, colors=colors_production)

    # Add a title to the production chart
    ax[0,0].set_title('Average Daytime Production')
    ax[0,0].legend(labels=labels_production, loc="center left", bbox_to_anchor=(1, 0.5), frameon = False)
    ax[0,0].text(0.025, 0.95, "(a)", transform=ax[0,0].transAxes, fontsize=16, verticalalignment='top')


    # Create the loss pie chart with the custom colors and labels
    ax[0,1].pie(values_loss, colors=colors_loss)
    # Add a title to the production chart
    ax[0,1].set_title('Average Daytime Loss')
    # For legend next to pie chart
    ax[0,1].legend(labels=labels_loss, loc="center left", bbox_to_anchor=(1, 0.5), frameon = False)
    ax[0,1].text(0.085, 0.95, "(b)", transform=ax[0,1].transAxes, fontsize=16, verticalalignment='top')

    
    # NIGHTTIME
    # Create the production pie chart with the custom colors and labels
    ax[1,0].pie(values_production_night, colors=colors_production)

    # Add a title to the production chart
    ax[1,0].set_title('Average Nightime Production', loc = 'center')
    ax[1,0].legend(labels=labels_production_night, loc="center left", bbox_to_anchor=(1, 0.5), frameon = False)
    ax[1,0].text(0.025, 0.95, "(c)", transform=ax[1,0].transAxes, fontsize=16, verticalalignment='top')

    # Create the loss pie chart with the custom colors and labels
    # labels=labels_loss_night,
    ax[1,1].pie(values_loss_night, colors=colors_loss)
    # Add a title to the production chart
    ax[1,1].set_title('Average Nightime Loss')
    ax[1,1].legend(labels=labels_loss_night, loc="center left", bbox_to_anchor=(1, 0.5), frameon = False)
    ax[1,1].text(0.05, 0.95, "(d)", transform=ax[1,1].transAxes, fontsize=16, verticalalignment='top')

       # Save the figure if save_filename is provided
    if save_filename:
        save_filename = "C:\\Users\\bodehoov\\OneDrive - Indiana University\\Final MI 2022 Data\\FINAL\\Plots\\" + save_filename
        plt.savefig(save_filename, dpi=600, bbox_inches='tight')
        
        
    plt.show()
    
#plotPie(df_ALL, 'ALL Pie chart daytime and nighttime production loss ')
plotPie(df_RAIN, 'Rain Pie chart daytime and nighttime production loss ')
