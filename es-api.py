import boto3
import requests
from requests_aws4auth import AWS4Auth
import json
import os

def lambda_handler(event, context):
    region_name = 'us-east-1'
    service = 'es'
    hostname='https://search-changedata-lq2yok2wmkhwzeu7awauv4a3km.us-east-1.es.amazonaws.com'
    indexname = 'data'
    type = 'lambda-type'
    credentials = boto3.Session().get_credentials()
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region_name, service, session_token=credentials.token)
    url = hostname + '/' + indexname + '/_search/?size=300'
    headers = {"Content-Type": "application/json"}
    #getting the data from elasticsearch using host and indexname
    response = requests.get(url, auth=awsauth, headers=headers)
    results = json.loads(response.text)
    records = [ {"data": x['_source']['cupcake']['S'],"time":x['_source']['Month']['S']} for x in results['hits']['hits']]
    print(records)
    return records
