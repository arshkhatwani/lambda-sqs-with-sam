import boto3
import json

session = boto3.Session(aws_access_key_id='',
                        aws_secret_access_key='',)

sqs = session.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='sam-app-MySqsQueue-JuGlACDSNXMr')

message = {
    'length': 20,
    'width': 10,
}

response = queue.send_message(MessageBody=json.dumps(message))
print('Successfully sent message to SQS')