def data_overview(df) -> pd.DataFrame :
    """
    Overview DataFrame
    usage: data_overview(df)
           (available type: np.number, np.object, 'category', 'all')
    :param df: dataframe to describe 
    :return: overview (type: dataframe)
    """ 

    return_dict = dict() # return dict 선언
    missing_cells = df.isna().sum().sum()
    duplicate_celks = df.duplicated(df.columns).sum()
    
    return_dict['Number of variables'] = pd.Series(df.shape[1])     # column
    return_dict['Number of observations'] = pd.Series(df.shape[0])  # row
    return_dict['Missing cells'] = pd.Series(str(missing_cells) + ' (' + str(missing_cells/df.shape[0]) + '%)') # Missing Cells
    return_dict['Duplicate cells'] = pd.Series(str(duplicate_celks) + ' (' + str( duplicate_celks/df.shape[0]) + '%)')
    
    return pd.DataFrame(return_dict).rename(index={0:"data info"}).T