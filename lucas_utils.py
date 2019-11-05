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

def show_fields_completeness(df:pd.DataFrame, fields:list, verbose=False):
    '''
    Create a bar plot of the levels of non nan values per field. 
    :param df: dataframe to extract info from
    :param fields: fields of the database to evaluate
    '''
    fields_fill_percentage = {}
    for i,field in enumerate(fields):
        fields_fill_percentage[field] = len(get_field_without_nan(df,field))/len(df) 
        if verbose:
            print('Done [%d/%d]' % (i+1,len(fields)), end='\r')
    plt.bar(fields_fill_percentage.keys(),fields_fill_percentage.values())
    plt.xticks(list(range(0,len(fields_fill_percentage))), fields_fill_percentage.keys(), rotation=90)
    plt.title('Fields\' level of completeness')
    plt.ylabel('Level of completeness')
    plt.grid()

def get_unique_values_of_field(df:pd.DataFrame, field='countries_tags', sep=','): 
    '''
    Returns a pd.Series with unique values for the given "field", where the field
    contains multiple values separated by "sep". 

    Procedure (line by line)
    1. Drop nan values from dataset and convert array to a Series.
    2. Split the field's values into list of strings. 
    3. Explode the lists into new rows. 
    4. Reset the index and return the final Series with unique values. 
    '''
    return pd.Series(pd.Series(df[field].dropna().unique())
        .apply(lambda x : str(x).split(sep)) 
        .explode().unique()).sort_values(ascending=True)\
        .reset_index()[0]

