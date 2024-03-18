import pandas as pd

location = "AWS S3 Folder URI"
output_location = "AWS S3 Folder URI" # Where You Want Your Parquet File
df = pd.read_csv(rf"{location}\IMDB_Movies_1990-2022.csv.csv")
df.to_parquet(rf"{output_location}\IMDB.parquet")
