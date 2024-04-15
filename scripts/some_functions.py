import matplotlib.pyplot as plt
import seaborn as sns



#def grid_plot(grid_x, grid_y):




# takes a series
def basic_histo(data, , **kwargs):
    plt.figure(figsize=(5, 5))
    sns.histplot(data, **kwargs)
    

    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plot_title=data.name
    plt.title(f'Histogram of {plot_title}')


    plt.show()