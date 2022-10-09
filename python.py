from sqlalchemy import create_engine
import pandas as pd

brain = pd.read_csv(
    'csv/brain_size.csv')
brain.to_sql('brain_size_updated',
              con=engine, if_exists='append')