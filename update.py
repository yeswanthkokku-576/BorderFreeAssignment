import json
import boto3
import random
import datetime
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
    table = dynamodb.Table('cakedata')
    for i in range(100):
        x=random.randrange(1, 207)

        #Get values from dynamodb using above generated random primarkey--id
        response = table.get_item(
                    Key={
                        'id': str(x),
                        
                    }
                )
        print(x)
        updated_cupcake_value=random.randrange(1,101)
        item = response['Item']
        
        response=table.put_item(
            
            Item={
                    'id' : item['id'],
                    'Month': item['Month'],
                    'cupcake': str(updated_cupcake_value),
                    'updatetime':str( datetime.datetime.now()),
            })
        #print(response)
