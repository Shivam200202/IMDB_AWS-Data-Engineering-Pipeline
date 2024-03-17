# AWS Data Engineering Pipeline: Extracting, Transforming, and Analyzing IMDB Data
The "AWS Data Engineering Pipeline: Extracting, Transforming, and Analyzing IMDB Data" project is aimed at demonstrating the implementation of a comprehensive data engineering pipeline using various AWS services. 

# Project Goals
The primary goals of the "AWS Data Engineering Pipeline: Extracting, Transforming, and Analyzing IMDB Data" project are as follows:

1.**Demonstrate AWS Data Engineering Pipeline:** Showcase the implementation of a comprehensive data engineering pipeline using AWS services such as AWS Glue, Athena, and S3. The project aims to provide a practical example for building scalable and efficient data pipelines in the AWS cloud environment.

2.**Extract and Transform IMDB Data:** Extract movie data from the Internet Movie Database (IMDB) website and transform it into a structured format suitable for analysis. This involves cleaning, formatting, and enriching the raw data to prepare it for querying and visualization.

3.**Enable Data Analysis and Insights:** Enable data analysis and derive actionable insights from the IMDB dataset using AWS Athena for querying and Power BI for visualization. The project aims to showcase the capabilities of AWS services for performing data analysis and visualization tasks.

4.**Address Challenges in Data Processing:** Address challenges encountered in data processing, such as schema inference issues, mixed data formats, data cleaning, and performance optimization.

# Data Pipeline
![Data Pipeline](https://github.com/Shivam200202/IMDB_AWS-Data-Engineering-Pipeline/assets/159875270/30fabc8d-6403-4c2c-a809-b49701f72ca9)

# Prerequisites
Before using this project, ensure you have the following prerequisites installed and set up:

1.**AWS Account:** You will need an active AWS account to access and utilize AWS services such as AWS Cloud9, S3, Glue, and Athena.

2.**IAM Role:** Create an IAM role with appropriate permissions to access AWS services. Ensure that the IAM role has permissions for S3, Glue, Athena, and any other services used in the project.

3.**AWS Glue Crawler Setup:** Configure an AWS Glue Crawler to crawl the data stored in your S3 bucket and create a corresponding database and table schema in the AWS Glue Data Catalog.

4.**AWS Athena Configuration:** Set up AWS Athena to enable querying of the data stored in your S3 bucket. Ensure that the necessary permissions are granted to execute queries.

5.**Power BI (Optional):** If you plan to create visualizations with Power BI, ensure that you have Power BI Desktop installed on your local machine.

6.**Access to IMDB Data Source:** Ensure access to the IMDb data source (https://www.imdb.com/list/ls560109468/?sort=list_order,asc&st_dt=&mode=detail&page=1) or have a similar dataset available for extraction.

7.**Basic Understanding of AWS Services:** Familiarize yourself with AWS services such as S3, Glue, Athena, and IAM, as well as basic concepts of data engineering and data analysis.

8.**Basic Understanding of Python:** Knowledge of Python programming language is essential for interacting with AWS services programmatically, performing data transformations, and scripting tasks related to data processing.


# Installation
**Python Libraries in AWS Cloud9**

**Install required Python libraries:**

pip install bs4 requests pandas fastparquet s3fs pyarrow

**Power BI for Data Visualization**

**Download Power BI Desktop:**

Visit the Power BI website and download the latest version of Power BI Desktop suitable for your operating system.
Install Power BI Desktop:

Follow the installation instructions provided by Microsoft to install Power BI Desktop on your local machine.

# Usage
1.**Setup AWS Environment:**

Make sure you have an active AWS account and necessary permissions to access AWS services.
Set up IAM roles with appropriate permissions for accessing S3, Glue, Athena, etc.

2.**Data Extraction:**

Use Python scripts or AWS Cloud9 to extract data from the IMDb website (https://www.imdb.com/list/ls560109468/?sort=list_order,asc&st_dt=&mode=detail&page=1).
Store the extracted data in an S3 bucket.

3.**Data Transformation:**

Python scripts to transform the raw data into a structured format suitable for analysis.
Convert CSV files to Parquet format using Python libraries such as pandas and fastparquet.

4.**AWS Glue Setup:**

Configure an AWS Glue Crawler to crawl the data stored in the S3 bucket and create a database and table schema in the Glue Data Catalog.

5.**AWS Athena Querying:**

Use AWS Athena to run SQL queries on the data stored in the S3 bucket.
Analyze the data and derive insights using SQL queries.

6.**Power BI Visualization (Optional):**

If desired, use Power BI Desktop to create visualizations and dashboards based on the data.

# Issues Encountered
During the development of this project, the following issues were encountered:

1.**AWS Glue Catalog Schema Inference:**

AWS Glue Catalog Schema Inference (Due to CSV Format):
The AWS Glue Crawler had difficulty inferring the schema for certain data columns, resulting in blank or incorrectly mapped columns in the Glue Data Catalog. This issue was addressed by manually defining the schema during table creation in the Glue Data Catalog. Additionally, it was resolved by changing the data format from CSV to Parquet, which improved schema inference and compatibility with AWS Glue and Athena.
![issue1](https://github.com/Shivam200202/IMDB_AWS-Data-Engineering-Pipeline/assets/159875270/47b2ad4d-1f2e-40ba-8e2d-87264562f0a8)

![issue2](https://github.com/Shivam200202/IMDB_AWS-Data-Engineering-Pipeline/assets/159875270/9fa62270-f3a9-477e-8d31-90d0195103a2)


3.**Data Cleaning and Transformation Challenges:**

Data extracted from the IMDb website required cleaning and transformation to ensure consistency and accuracy. Handling missing values, inconsistencies in data formats, and data quality issues required additional preprocessing steps using Python scripts and AWS Glue jobs.

# Power BI Showcase
In this section, we present visualizations and insights derived from the IMDb dataset using Power BI. The Power BI report includes the following key visualizations and interactive features:

1.**Total Gross Earning:** A card visual displaying the total gross earnings of movies.

2.**Count of Drama Movies:** A card visual showing the count of drama movies.

3.**Count of Action Movies:** A card visual illustrating the count of action movies.

4.**Count of Comedy Movies:** A card visual indicating the count of comedy movies.

5.**Count of Adventure Movies:** A card visual representing the count of adventure movies.

6.**Count of Thriller Movies:** A card visual depicting the count of thriller movies.

7.**Movie with Highest Vote:** A group of card visuals showcasing details of the movie with the highest vote. The visuals include:

a.**Votes:** Total number of votes received by the movie.
b.**Year of Release:** The year in which the movie was released.
c.**Runtime:** The duration of the movie in minutes.
d.**IMDb Rating:** The IMDb rating of the movie.
e.**Metascore Rating:** The Metascore rating of the movie.
f.**Gross Earning:** The gross earning of the movie.

8.**Slicers for Filtering:** Slicers are provided to filter the data based on the PG rating and release year. Users can interactively select specific PG ratings or years to view relevant data.

9.**Horizontal Bar Chart:** A horizontal bar chart displaying the gross earnings of movies over five years.

10.**Vertical Bar Chart:** A vertical bar chart showing the count of movies released over five years. Users can analyze trends in movie production over time.
![IMBD_Dashboard](https://github.com/Shivam200202/IMDB_AWS-Data-Engineering-Pipeline/assets/159875270/4f01fb9b-7925-465f-a55d-836818d7fa04)
