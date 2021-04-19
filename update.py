import json
import boto3
import random
import datetime
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cakedata')
    dyndb_client = boto3.client('dynamodb', 'us-east-1')
    #Generates Random values for id
    for i in range(100):
        x=random.randrange(1, 207)
        #Get values from dynamodb using above generated randomly generate id
        response = table.get_item(
                    Key={
                        'id': str(x),
                        
                    }
                )
        print(x)
        updated_cupcake_value=random.randrange(1,101)
        item = response['Item']
        #update new column in dynamodb using put_item method
        response=dyndb_client.put_item(
            TableName='cakedata',
            Item={
                    'id' : {'S':item['id']},
                    'Month': {'S':item['Month']},
                    'cupcake': {'S':str(updated_cupcake_value)},
                    'updatetime':{'S':str( datetime.datetime.now())},
            })