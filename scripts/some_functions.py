import matplotlib.pyplot as plt
import seaborn as sns



#def grid_plot(grid_x, grid_y):



basic_colour = sns.xkcd_rgb['deep red']

# takes a series
def basic_histo(data, colour=basic_colour, **kwargs):
    plt.figure(figsize=(6, 4))
    sns.histplot(data, color=colour, **kwargs)
    
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plot_title=data.name
    plt.title(f'Distribution of {plot_title}')

    plt.show()


# takes a series
def basic_boxplot(data, colour=basic_colour, **kwargs):
    plt.figure(figsize=(8, 6))  
    sns.boxplot(data=data, color=colour, **kwargs)

    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plot_title = data.name
    plt.title(f'Boxplot of {plot_title}')

    plt.show()