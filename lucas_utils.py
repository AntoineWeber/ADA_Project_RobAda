'''
Utility functions for analyzing the Opend Food Facts database.
Conda: 'ada' environment  
'''

import re
import pickle 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

##################################
# Plots
##################################
def plot_bar(x, y, title:str, ylabel:str, size=(5,5)):
    plt.figure(figsize=size)
    plt.barh(list(x),list(y))
    plt.xticks(list(range(0,len(x))), x, rotation=90)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid()

def plot_barh(x, y, title:str, xlabel:str, size=(5,5)):
    plt.figure(figsize=size)
    plt.barh(list(x),list(y))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.margins(y=0)
    plt.grid()

##################################
# Pandas 
##################################

def get_field_without_nan(df:pd.DataFrame, field='origins', head=0):
    '''
    Returns a Series of none nan values for the specified "field".
    Specifiy the length of the Series to return with "head". 
    :param df: dataframe to extract info from
    :param field: field of the database to evaluate
    :param head: how many values to return
    :return: Series, percentage of none nan values for the given "field"
    '''
    if head == 0:
        return df[df.notna()[field]][field]
    elif head > 0:
        return df[df.notna()[field]][field].head(head)

def get_unique_values_of_field(df:pd.DataFrame, field='countries_tags', sep=','): 
    '''
    Returns a pd.Series with unique values for the given "field", where the field
    contains multiple values separated by "sep". 

    Procedure (line by line)
    1. Drop nan values from dataset and convert array to a Series.
    2. Split the field's values into list of strings. 
    3. Explode the lists into new rows. 
    4. Reset the index and return the final Series with unique values. 

    :param df: dataframe to extract info from
    :param field: field of the database to evaluate
    :param sep: sperator to split the values 
    '''
    return pd.Series(pd.Series(df[field].dropna().unique())
        .apply(lambda x : str(x).split(sep)) 
        .explode().unique()).sort_values(ascending=True)\
        .reset_index()[0]

def get_field_value_counts(df:pd.DataFrame, field='countries_tags', sep=','):
    '''
    Count the occurences of the different values of the given "field". 
    The fields containing the specified speratator "sep" are exploded (boom). 

    :param df: dataframe to extract info from
    :param field: field of the database to evaluate
    :param sep: sperator to split the values 
    '''
    return df[field].dropna().apply(lambda x : str(x).split(sep)).explode().value_counts()

##################################
# Visualization 
##################################

def show_fields_completeness(df:pd.DataFrame, fields:list, verbose=False):
    '''
    Create a barh plot of the levels of non nan values per field. 
    :param df: dataframe to extract info from
    :param fields: fields of the database to evaluate
    :param verbose: show progress
    '''
    fields_fill_percentage = {}
    for i,field in enumerate(fields):
        fields_fill_percentage[field] = len(get_field_without_nan(df,field))/len(df) 
        if verbose:
            print('Done [%d/%d]' % (i+1,len(fields)), end='\r')
    plot_barh(fields_fill_percentage.keys(),
                fields_fill_percentage.values(),
                'Fields\' level of completeness',
                'Level of completeness')

def show_field_value_counts(df:pd.DataFrame, field='countries_tags', sep=',', size=(5,5)):
    v_counts = get_field_value_counts(df,field,sep)
    plot_barh(v_counts.index, 
                v_counts.values,
                'Value counts for field "%s"'%(field),
                "Value counts",
                size=size)
    plt.xscale('log')

