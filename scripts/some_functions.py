## contains some basic functions ##

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


basic_colour = sns.xkcd_rgb['deep red']
basic_colour_2 = sns.xkcd_rgb['royal']

basic_pallette = [basic_colour_2, basic_colour]


# takes a series
def basic_histo(data, values="Values", colour=basic_colour, **kwargs):
    plt.figure(figsize=(6, 4))
    sns.histplot(data, color=colour, **kwargs)

    plt.xlabel(values)
    
    plot_title=data.name
    plt.title(f'Distribution of {plot_title}')

    plt.show();


# takes a series
def basic_boxplot(data, values=None, colour=basic_colour, **kwargs):
    plt.figure(figsize=(6, 4))  
    sns.boxplot(data=data, color=colour, **kwargs)

    plt.xlabel(values)

    plot_title = data.name
    plt.title(f'Boxplot of {plot_title}')
    plt.show();


def basic_bootstrap(data, sample_n=100, x_value="retention_1", labels="version" ):
    boot_list = []
    for i in range(sample_n):
        boot_mean = data.sample(frac=1, replace=True).groupby(labels)[x_value].mean()
        boot_list.append(boot_mean)
    
    boot_df = pd.DataFrame(boot_list)
    
    sns.kdeplot(data=boot_df, fill=True, palette=basic_pallette)
    plt.ylabel(None)

    plt.title(f"Bootstrap of {x_value} with {sample_n} samples")
    plt.show();