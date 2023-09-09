def plot_stacked_bars_with_labels(percents, production_rates, loss_rates, x_labels, y_label, production_labels, loss_labels, prod_colors, loss_colors):
    # Define the data for the four plots
    day_production_data = percents[0][production_rates].values
    day_loss_data = percents[2][loss_rates].values
    night_production_data = percents[1][production_rates].values
    night_loss_data = percents[3][loss_rates].values
   # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the stacked bars for daytime production
    day_prod_bars = []
    for i in range(len(production_rates)):
        if i == 0:
            day_prod_bars.append(ax.bar(x_labels[0], day_production_data[i], color=prod_colors[i], label=production_labels[i]))
        else:
            day_prod_bars.append(ax.bar(x_labels[0], day_production_data[i], bottom=sum(day_production_data[:i]), color=prod_colors[i], label=production_labels[i]))

    # Create the stacked bars for daytime loss
    day_loss_bars = []
    for i in range(len(loss_rates)):
        if i == 0:
            day_loss_bars.append(ax.bar(x_labels[1], day_loss_data[i], color=loss_colors[i], label=loss_labels[i]))
        else:
            day_loss_bars.append(ax.bar(x_labels[1], day_loss_data[i], bottom=sum(day_loss_data[:i]), color=loss_colors[i], label=loss_labels[i]))

    # Create the stacked bars for nighttime production
    night_prod_bars = []
    for i in range(len(production_rates)):
        if i == 0:
            night_prod_bars.append(ax.bar(x_labels[2], night_production_data[i], color=prod_colors[i], label=production_labels[i]))
        else:
            night_prod_bars.append(ax.bar(x_labels[2], night_production_data[i], bottom=sum(night_production_data[:i]), color=prod_colors[i], label=production_labels[i]))

    # Create the stacked bars for nighttime loss
    night_loss_bars = []
    for i in range(len(loss_rates)):
        if i == 0:
            night_loss_bars.append(ax.bar(x_labels[3], night_loss_data[i], color=loss_colors[i], label=loss_labels[i]))
        else:
            night_loss_bars.append(ax.bar(x_labels[3], night_loss_data[i], bottom=sum(night_loss_data[:i]), color=loss_colors[i], label=loss_labels[i]))

    # Add the first legend for the production rates
    day_prod_bars_labels = [bar[0] for bar in day_prod_bars]
    night_prod_bars_labels = [bar[0] for bar in night_prod_bars]
    ax.legend(day_prod_bars_labels + night_prod_bars_labels, production_labels, frameon = False, bbox_to_anchor=(1.3, 0.75), fontsize = 12)

    # Add the second legend for the loss rates
    day_loss_bars_labels = [bar[0] for bar in day_loss_bars]
    night_loss_bars_labels = [bar[0] for bar in night_loss_bars]
    ax2 = ax.twinx()  # Create a second y-axis that shares the same x-axis
    ax2.legend(day_loss_bars_labels + night_loss_bars_labels, loss_labels, frameon = False, bbox_to_anchor=(1.3, 0.45), fontsize = 12)
    
    # Add x-axis label and y-axis label to the main axis
    ax.set_xlabel('Rates', fontsize = 14)
    ax.set_ylabel(y_label, fontsize = 14)
    ax2.set_yticklabels([])
    ax2.set_yticks([])
    
    
    # Show the plot
    plt.show()

# Define the rate names for production and loss rates
production_rates = ['rateOH_NO_MCM', 'rateNO2_aerosol', 'rateNO2_ground']
loss_rates = ['ratePhotolysis_MCM', 'rateHONO_OH_MCM', 'rateDilution', 'rateHONO_ground', 'diff']

# Define the labels for the x-axis and y-axis
x_labels = ['Daytime Production', 'Daytime Loss', 'Nighttime Production', 'Nighttime Loss']
y_label = 'Contribution'

# Define the labels for the stacked bars
production_labels = ['OH + NO', 'NO$_2$ + Aerosol', 'NO$_2$ + Ground']
loss_labels = ['Photolysis', 'HONO + OH', 'Dilution', 'HONO + Ground', 'Unknown']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
prod_colors = ['#328BB8','#006298', 'navy', '#63B1D3']
loss_colors = ['#800020', '#E3735E', '#AA4A44', '#D2042D', '#630330']

# Define the colors for the stacked bars
#plot_stacked_bars_with_labels(percents, production_rates, loss_rates, x_labels, y_label, production_labels, loss_labels, prod_colors, loss_colors)
