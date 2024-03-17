import pandas as pd

location = "Your S3 Bucket Location"
output_location = "Where You Want to Save Parquet File"
df = pd.read_csv(rf"{location}\IMDB_Movies_1990-2022.csv.csv")
df.to_parquet(rf"{output_location}\IMDB.parquet")
