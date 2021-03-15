import pandas as pd
def format_date (X):
    X1 = X.loc[:,'identifiant accident':'date']
    X2 = X.loc[:,'departement':'nombre autres vehicules']
    formated_df = pd.concat([X1,X2], axis=1)
    formated_df['date'] = formated_df['date']+'T'+X['heure']+':00:00+1:00'
    return formated_df
