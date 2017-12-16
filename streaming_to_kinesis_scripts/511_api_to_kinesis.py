import boto3
import time
import urllib.request
from google.transit import gtfs_realtime_pb2

def lambda_handler(event, context):
    # All agencies
	# agencies = ['3D','AC','AM','AT','AY','BA','BG','CC','CE','CM','CT','DE','EM','FS','GF','GG','HF','MA','MS','PE','RV','SA','SB','SC','SF','SM','SO','SR','ST','UC','VC','VN','WC','WH']

	# All succcessful API call agencies
	# agencies = ['3D','AC','BA','CC','CT','DE','GG','MA','SC','SF','SM','SR','VN','WC']

	# All succcessful API call agencies that return vehicle positions
	agencies = ['3D','AC','CC','SF','SR','VN']

	kinesis_client = boto3.client('kinesis', region_name='us-east-1', 
		aws_access_key_id='AKIAJP4ASR6L7P6X2YIQ',
		aws_secret_access_key='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')

	# Pick a specific agency depending on the minute
	minute = int(time.strftime("%M"))
	agency = agencies[minute % len(agencies)]
	print("Loading Agency:",agency)

	# Load latest vehicle positions for agency and send data to Kinesis
	try:
	  feed = gtfs_realtime_pb2.FeedMessage()
	  response = urllib.request.urlopen('http://api.511.org/Transit/VehiclePositions?api_key=c446f9f0-5979-4667-a37b-d31b41480fa9&agency='+agency)
	  feed.ParseFromString(response.read())

	  print("Sending", len(feed.entity), agency, "rows to Kinesis")
	  
	  for x in range(0, len(feed.entity)):
	  	put_response = kinesis_client.put_record(
	  		StreamName = 'W205',
	  		Data = "{}, {}, {}, {}, {}, {} \n".format(
	  			feed.entity[x].vehicle.vehicle.id, 
				feed.entity[x].vehicle.timestamp,
				feed.entity[x].vehicle.position.latitude,
				feed.entity[x].vehicle.position.longitude,
				feed.entity[x].vehicle.trip.trip_id,
				agency),
			PartitionKey = "abc123")
	  print(agency,"Successful")
	except:
	  print(agency,"Failed")
	
	return