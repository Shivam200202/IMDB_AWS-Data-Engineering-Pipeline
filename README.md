# AWS Data Engineering Pipeline: Extracting, Transforming, and Analyzing IMDB Data

# Introduction
The "AWS Data Engineering Pipeline: Extracting, Transforming, and Analyzing IMDB Data" project is aimed at demonstrating the implementation of a comprehensive data engineering pipeline using various AWS services. The primary objective of this project is to extract movie data from the Internet Movie Database (IMDB), transform it into a structured format, and analyze it to derive valuable insights.

This project showcases the end-to-end process of collecting data from a web source, storing it in Amazon S3 buckets, transforming it using AWS Glue, and querying it with Amazon Athena. Additionally, it highlights the challenges encountered during the implementation and how they were addressed.

The project serves as a practical example for data engineers and enthusiasts looking to leverage AWS services for building scalable and efficient data pipelines. By following along with this project, users can gain valuable insights into best practices for working with AWS Cloud infrastructure and data engineering tools.

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

The AWS Glue Crawler had difficulty inferring the schema for certain data columns, resulting in blank or incorrectly mapped columns in the Glue Data Catalog. This issue was addressed by manually defining the schema during table creation in the Glue Data Catalog.
https://github.com/Shivam200202/IMDB_AWS-Data-Engineering-Pipeline/assets/159875270/4d985ce2-34f6-479d-aed4-9438c133c9ad

2.**Mixed Data Formats in S3 Bucket:**

Storing both CSV and Parquet files in the same S3 bucket caused compatibility issues with AWS Glue Catalog and Athena. As a solution, only Parquet files were retained in the S3 bucket, ensuring uniform data format for seamless processing.

3.**Data Cleaning and Transformation Challenges:**

Data extracted from the IMDb website required cleaning and transformation to ensure consistency and accuracy. Handling missing values, inconsistencies in data formats, and data quality issues required additional preprocessing steps using Python scripts and AWS Glue jobs.
