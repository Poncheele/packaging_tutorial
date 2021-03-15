import biketrauma
import pandas as pd


df = biketrauma.Load_db().save_as_df()
df2=biketrauma.format_date(df)
df2