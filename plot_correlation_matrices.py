def plot_correlation_matrices(df1, df2, file_name=None):
    # select the columns to include
    keep_columns = ['HONO', 'OH', 'T', 'RH', 'NO', 'NO2', 'diff']
    ticks = ['[HONO]', '[OH]', 'Temp', 'RH', '[NO]', '[NO$_2$]', 'Unknown']

    # plot the correlation matrices for the three dataframes
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 10), gridspec_kw={'wspace': 0.1, 'width_ratios': [1, 1]})
    title = ['(a) Rain', '(b) Dry']
    for i, df in enumerate([df1, df2]):
        correlation = df[keep_columns].corr().round(2)
        mask = np.triu(np.ones_like(correlation))
        sn.heatmap(correlation, annot=True, cmap="coolwarm", mask=mask, xticklabels=ticks, yticklabels=ticks, ax=axes[i], cbar=i==2, annot_kws={"fontsize":16})
        axes[i].set_xticklabels(ticks, rotation=45, fontsize = 16)
        axes[i].set_yticklabels(ticks, rotation=45, fontsize = 16)
        if i != 0:
            axes[i].set_yticks([])
            axes[i].set_ylabel('')
        axes[i].set_title(title[i], fontsize = 18)

    # create a single legend for all the plots
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=1, fontsize = 16)

    # Save plot if name provided
    if file_name:
        file_name = "C:\\Users\\bodehoov\\OneDrive - Indiana University\\Final MI 2022 Data\\FINAL\\Plots\\" + file_name
        plt.savefig(file_name, dpi=600, bbox_inches='tight')
        
    plt.show()
