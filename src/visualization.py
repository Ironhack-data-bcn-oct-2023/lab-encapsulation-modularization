import pandas as pd
import os
def visualizing (df, file_name):
    """
    Create a bar plot from grouped data and export it as an image.

    Parameters:
        grouped_data (pd.DataFrame): The grouped data to be used for the bar plot.
        output_filename (str): The name for the exported image file.

    Returns:
        None
    """
    # plot info will be ...
    grouped_data = df.groupby('type')['averageprice'].mean()

    # make plot
    ax = grouped_data.plot(kind='bar')
    
    # set labels and title
    ax.set_xlabel(grouped_data.index.name)    

    # set x-axis tick labels and rotation
    ax.set_xticklabels(grouped_data.index, rotation=0)  

    # save the figure as an image
    ax.get_figure().savefig(f'images/{file_name}.png')   

    # open the saved image
    os.system(f'start images/{file_name}.png') 