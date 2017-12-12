from google.transit import gtfs_realtime_pb2
import urllib

def lambda_handler(event, context):
	# feed = gtfs_realtime_pb2.FeedMessage()
	# response = urllib.urlopen('http://api.511.org/Transit/VehiclePositions?api_key=baa045f5-dff4-44f4-ad59-8d50f70b12ad&agency=AC')
	# feed.ParseFromString(response.read())
	# for entity in feed.entity:
	#   return entity
	return "hi"
