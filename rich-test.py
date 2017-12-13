import boto3

def lambda_handler(event, context):
    # TODO implement
    
    kinesis_client = boto3.client('kinesis', region_name='us-east-1', 
        aws_access_key_id='AKIAJP4ASR6L7P6X2YIQ',
        aws_secret_access_key='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')
    # kinesis.describe_stream("BotoDemo")
    # kinesis_client.list_streams()
    
    put_response = kinesis_client.put_record(
                        StreamName='Rich_Test',
                        Data='Testing123',
                        PartitionKey='abc123')
    
    return put_response