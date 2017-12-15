# W205 Final Project
###### James Black, Ramsey Magana, Aniruddh Nautiyal, Rich Ung

## Set-Up Instructions
See Google Doc: https://docs.google.com/document/d/1JIP-m5Fz2fZq96D78muixMvgrbWwGmyBHJIHJreo8dY/edit?usp=sharing

## Powerpoint Presentation
See Google Slides: https://docs.google.com/presentation/d/1G7sQwsrevRdYoSHLpIscKi3sLB-p9J63iWhVfoOSuo4/edit?usp=sharing

## Colaboratory Doc
https://colab.research.google.com/notebook#fileId=1QWwCsd6YLo3iBQVce0Hs_I-ldoACU1AY

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
