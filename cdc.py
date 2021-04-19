import boto3
import requests
from requests_aws4auth import AWS4Auth
import os

def lambda_handler(event, context):
    region = os.environ['region'] 
    service = os.environ['service_name']
    hostname=os.environ['host']
    index_name='data'
    index_type=os.environ['index_type']
    url=hostname + '/' + index_name + '/' + index_type +'/'
    headers = { "Content-Type": "application/json" }
    credentials = boto3.Session().get_credentials()
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token) 
    for record in event['Records']:
        # To Get the primary key for using as Elasticsearch ID
        id = record['dynamodb']['Keys']['id']['S']
        #Checking the condition of eventname while databse update this trigger will be called
        if record['eventName'] == 'REMOVE':
            document = record['dynamodb']['OldImage']
            r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
        elif record['eventName'] == 'MODIFY' or record['eventName'] == 'INSERT':
            document = record['dynamodb']['NewImage']
            print(document)
            r = requests.put(url + id, auth=awsauth, json=document, headers=headers)
