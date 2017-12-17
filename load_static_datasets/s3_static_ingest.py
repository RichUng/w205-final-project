import boto3

import urllib.request
import os, shutil, zipfile, io

import pandas as pd
import json
import csv


def main():
    ACCESS_KEY = 'AKIAJP4ASR6L7P6X2YIQ'
    SECRET_KEY = '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'

    APIKEY_511 = 'c446f9f0-5979-4667-a37b-d31b41480fa9'
    URL_PREFIX =  'http://api.511.org/transit/datafeeds?api_key='

    AGENCY_LIST = ['3D','AC','CC','SF','SR','VN']

    BUCKET_NAME = 'w205-redshift-intermediate'

    CWD = os.getcwd()

    DIR_1 = CWD+'/my_directory/'

    DIR_2 = CWD+'/tripsdir/'

    ##### connect to s3 ######

    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    ##### datafeed files #####

    for agency in AGENCY_LIST:
    
        try:
            r = requests.get(URL_PREFIX+APIKEY_511+'&operator_id='+agency)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(DIR_1)

            if not os.path.exists(DIR_2):
                os.makedirs(DIR_2)
        
        
            FILENAME = 'trips'+str(agency)+'.txt'

            os.rename(DIR_1+'trips.txt', DIR_2+FILENAME)

            #delete the directory and contents
            shutil.rmtree(DIR_1)
        
            # Read file as pandas frame and append column
            df = pd.read_csv(DIR_2+FILENAME)
            df['agency'] = agency
            data = df.to_csv(index=False)
            print('data')

            # Write file to S3
            s3.Bucket(BUCKET_NAME).put_object(Key='test/static_datafeed/'+FILENAME, Body=data)
            print('Agency successfully uploaded: '+agency)
        
        except:
            print('Agency failed upload: '+agency)
            print(URL_PREFIX+str(APIKEY_511)+'&operator_id='+str(agency))
            pass

    #shutil.rmtree(DIR_2)


    ##### crime data  #####

    response = urllib.request.urlopen('https://data.sfgov.org/api/views/9v2m-8wqu/rows.json?accessType=DOWNLOAD')
    body = response.read().decode('utf-8-sig')
    json_data = json.loads(body)

    try:
        os.mkdir(DIR_1)
    except:
        pass

    crime_headers = [i['fieldName'] for i in json_data['meta']['view']['columns']]

    with open(DIR_1+'sf_crime.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        spamwriter.writerow(crime_headers)
        for line in json_data['data']:
            spamwriter.writerow(line)

    s3.Object(BUCKET_NAME, 'static_crime/'+'sf_crime.csv').put(Body=open(DIR_1+'sf_crime.csv', 'rb'))                

    #shutil.rmtree(DIR_1)

    ##### gtfs_operator_list.csv #####

    response = urllib.request.urlopen('http://api.511.org/transit/gtfsoperators?api_key=baa045f5-dff4-44f4-ad59-8d50f70b12ad&format=json')

    body = response.read().decode('utf-8-sig')
    json_data = json.loads(body)
    df = pd.io.json.json_normalize(json_data)

    try:
        os.mkdir(DIR_1)
    except FileExistsError:
        pass

    df.to_csv(DIR_1+'gtfs_operator_list.csv', index=False)
    s3.Object(BUCKET_NAME, 'test/static_operators/'+'gtfs_operator_list.csv').put(Body=open(DIR_1+'gtfs_operator_list.csv', 'rb'))

    #shutil.rmtree(DIR_1)


    ##### income data #####

    response = urllib.request.urlopen('https://www.irs.gov/pub/irs-soi/15zpallagi.csv')
    string = response.read().decode('utf-8-sig')
    body = [i.split(',') for i in string.split('\n')]

    try:
        os.mkdir(DIR_1)
    except:
        pass

    with open(DIR_1+'irs_income.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        for line in body:
            spamwriter.writerow(line)

    s3.Object(BUCKET_NAME, 'static_income/'+'irs_income.csv').put(Body=open(DIR_1+'irs_income.csv', 'rb'))
        
    #shutil.rmtree(DIR_1)



if __name__ ==  "__main__":
	main()
    
    