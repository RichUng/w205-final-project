# W205 Final Project
###### James Black, Ramsey Magana, Aniruddh Nautiyal, Rich Ung

## Overview

### Scope

The purpose of this project is to design an end-to-end data flow to visualize transportation data. We use a lambda function and python scripts to pull data from different APIs into S3 and Amazon Kinesis, and pipe the data into Amazon Redshift, our serving layer. This will allow users to see the latest position of a vehicle in real-time and allow the user to filter the vehicle by variables such as the operator name. Since we are streaming data with Kinesis, we are involving real-time analytics (velocity). We are using multiple data sources ("GTFS Operator List", trips.txt files from the "GTFS DataFeed", and the "GTFS-Realtime Vehicle Positions" API to simulate streaming data) that are merged to create the final view table, "latest_position". Since we are using S3 as our data lake and storage layer, and Amazon Kinesis can scale out to handle more data by adding more shards and streams, this solution has the potential to handle high volumes of data.

### Functional

This GitHub repository includes all code that's necessary to execute our end-to-end data flow. We combine 3 datasets together when creating our final view table for Tableau, and regularly update our data through streaming new data into Kinesis. We clean the data when ingesting the static tables by adding an "Agency" column to one of our datasets and remove whitespaces between trip_ids in order to perform a proper join between the datasets, and believe that this will help provide an easy experience for the end user to see the current location of a vehicle in real-time.

### Design/Architecture

We chose an AWS design (using Lambda functions, Kinesis, S3, and Redshift) because it allows us to concentrate on the implementation of the end-to-end data flow without needing to maintain servers. These services require minimum server maintenance, and can be considered to be a serverless architecture. While it does provide us with less control over our architecture versus implementing our own servers and services such as Apache Kafka, it allows us to concentrate more on the data flow aspect of the project. This solution is capable of scaling as we add more data into S3, Kinesis, and Redshift since Kinesis only requires more shards if we add more data and Redshift only requires more nodes of we add more data, and this implementation also has clear processing and service layers (we use S3, Python scripts, and Kinesis Firehose to process our data and use Amazon Redshift as our serving layer).

### Additional Information

We can scale this solution by simply adding more data into S3 through Python scripts if they are static datasets, or use Amazon Kinesis to pipe data into S3 and Redshift if they are streaming datasets. This allows to scale our solution in the future by either having more services connect to Amazon Kinesis to handle real-time processing, or use Amazon EMR (Elastic MapReduce) to run Spark or Hadoop based jobs on our S3 datasets (which we can use as our source of truth and large scale data processing). In the future, we envision additional datasets are incorporated by piping them into S3 and Kinesis, and future processing and technological needs are incorporated by having these additional technologies (such as Spark or Hive) to connect to S3 and Kinesis for additional processing.

## Set-Up Instructions
https://docs.google.com/document/d/1JIP-m5Fz2fZq96D78muixMvgrbWwGmyBHJIHJreo8dY/edit?usp=sharing

## Powerpoint Presentation
* Final Presentation Powerpoint
  * https://docs.google.com/presentation/d/1TKMiFkk51V3EwioeHWTxsdTUgc-i-tPFCuxD4uFuvHQ/edit?usp=sharing
* Proposal Powerpoint
  * In Powerpoints folder
* Progress Powerpoint
  * In Powerpoints folder

## Colaboratory Doc
https://colab.research.google.com/notebook#fileId=1QWwCsd6YLo3iBQVce0Hs_I-ldoACU1AY

## Diagrams
https://www.lucidchart.com/invitations/accept/d7295df6-b367-4beb-a5f4-777a172a6ce0

## Rich's AWS Management Console
https://133706797667.signin.aws.amazon.com/console

## Authentication Information
### Redshift
* JDBC URL:
  * jdbc:redshift://w205-final-project.cspk3mfgs5hv.us-east-1.redshift.amazonaws.com:5439/dev
* Server
  * w205-final-project.cspk3mfgs5hv.us-east-1.redshift.amazonaws.com
* Port
  * 5439
* Default Database
  * dev
* Master Username
  * w205
* Master Password
  * W205final

### S3
* Bucket Name
  * w205-rich
* Bucket ARN
  * arn:aws:s3:::w205-rich
* Access key ID
  * AKIAJWJYSHBBOJTWHHTQ
* Secret access key
  * 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

### Kinesis Data Stream
* Access key ID
  * AKIAJWJYSHBBOJTWHHTQ
* Secret access key
  * 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
* Stream Name
  * W205
* Region Name
  * us-east-1
* Stream ARN
  * arn:aws:kinesis:us-east-1:133706797667:stream/W205

### Data Source
* GTFS-Realtime Vehicle Positions
  * GTFS-realtime Vehicle Positions service produces realtime information about the vehicles including location and congestion level.
  * Example API Call:
    * http://api.511.org/Transit/VehiclePositions?api_key=c446f9f0-5979-4667-a37b-d31b41480fa9&
* GTFS Operator List
  * GTFS Operator List is the list of operators/agencies that have GTFS dataset available via Open511 APIs.
  * Example API Call:
    * http://api.511.org/transit/gtfsoperators?api_key=c446f9f0-5979-4667-a37b-d31b41480fa9
* GTFS DataFeed download
  * GTFS datafeed download allows the user to download a zip file containing GTFS dataset for the specified operator/agency
  * The zip file contains the text files corresponding to the GTFS file formats. It also contains additional files, called the GTFS+ files, that provide information that is not contained in the GTFS files such as the direction names, farezone names, etc. The list of GTFS+ files and their data structures are provided in Appendix D of this document
  * When the request is processed successfully, the user will receive a zip file attachment in response to this API.
  * Example API Call:
    * http://api.511.org/transit/datafeeds?api_key=c446f9f0-5979-4667-a37b-d31b41480fa9&operator_id=AC

## Redshift Access Instructions
* Follow steps located here:
  * http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-connect-to-cluster.html
* Download a SQL query tool such as SQL Workbench/J:
  * http://www.sql-workbench.net/downloads.html
* JDBC Driver is located within github repo
  * RedshiftJDBC42-1.2.10.1009.jar
