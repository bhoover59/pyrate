def plotRates(df_RAIN, df_DRY, title, save_filename = None):
    dfs = [df_RAIN, df_DRY]
    fig, axs = plt.subplots(nrows=2, figsize = (12, 14))
    
    for i, df in enumerate(dfs):
        # Calculate difference in rates (missing loss to reach photosationary state)
        df['diff'] = -(df['rateProduction'] + df['rateLoss']) # plus loss because it is already negative
        df['otherProduction'] = df['rateNO2_aerosol'] + df['rateSoilEmis'] + df['rateNO2_aerosol_hv'] + df['rateNO2_ground_hv'] + df['rateHNO3p_hv']
        df['otherLoss'] = df['rateDilution'] + df['rateHONO_OH_MCM']
    
        # Plots bottom to top
        hours = df['Time']
        loss_rates = [df['ratePhotolysis_MCM'], df['rateHONO_ground'], df['otherLoss'], df['diff']] # Negative values for loss rates
        production_rates = [df['rateOH_NO_MCM'], df['rateNO2_ground'], df['otherProduction']]
    
        # Plot loss rates
        loss_lines = axs[i].stackplot(hours, loss_rates, labels=['Photolysis', 'HONO+ground', 'Other', 'Unknown'], colors=['#FA888A', '#E63639', '#B50404', '#810202'])
    
        # Plot production rates
        prod_lines = axs[i].stackplot(hours, production_rates, labels=['OH+NO', 'NO$_2$+ground', 'Other'], colors=['#759DDB', '#3675D7', '#0545A8'])
    
        # Set axis labels and limits
#         axs[i].set_xlabel('Hour', fontsize=16)
        axs[i].set_ylabel('Reaction Rate (ppb/h)', fontsize=16)
#         axs[i].set_title(title[i], fontsize=16)
        
        # Set y limits to the maximum of production and the minimum of loss with buffer
#         buffer = 1.1
#         y_max = np.nanmax(np.concatenate(production_rates + loss_rates)) * buffer
#         y_min = -y_max
#         axs[i].set_ylim(y_min, y_max)
        
        axs[i].set_ylim(-0.1, 0.1)
    
        # Create separate legends for loss rates and production rates
        loss_legend = axs[i].legend(handles=loss_lines, loc='lower right', bbox_to_anchor = (0.9, -0.015), title='Loss Rates', frameon=False, fontsize=14)
        prod_legend = axs[i].legend(handles=prod_lines, loc='upper right', bbox_to_anchor = (0.9, 1.0), title='Production Rates', frameon=False, fontsize=14)
    
        loss_legend.get_title().set_fontsize(14)
        loss_legend.get_title().set_ha('left') # title of legend left justified
        prod_legend.get_title().set_fontsize(14)
        prod_legend.get_title().set_ha('left')
    
        # Add the legends to the plot
        axs[i].add_artist(loss_legend)
        axs[i].add_artist(prod_legend)
        
        # Set font size for tick labels on both axes
        axs[i].tick_params(axis='both', which='major', labelsize=12)
    
        # Add text (a) to plot
        plot_labels = ['(a) Rain days', '(b) Dry days']
        for i, label in enumerate(plot_labels):
            axs[i].text(0.045, 0.965, label, transform=axs[i].transAxes, fontsize=16, verticalalignment='top')


        # Remove extra space next to axes
#         axs[i].margins(x=0)
    axs[0].margins(x=0)
    axs[1].margins(x=0)

    # Save the figure if save_filename is provided
    if save_filename:
        save_filename = "C:\\Users\\bodehoov\\OneDrive - Indiana University\\Final MI 2022 Data\\FINAL\\Plots\\" + save_filename
        plt.savefig(save_filename, dpi=600, bbox_inches='tight')
        
    # Show the plot
    plt.show()
    
#plotRates(df_RAIN, df_DRY, ['Rain days', 'Dry days'], save_filename = 'ReactionRates_pH6_adjustedRates')
