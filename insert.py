import boto3
import csv
import os
def lambda_handler(event, context):
    region='us-east-1'
    file_name='cupcake.csv'
    bucket_name='borderfree1'
    table_name='cakedata'
    records=[]
    s3=boto3.client('s3')            
    dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
    table = dynamodb.Table('cakedata')
    s3_object= s3.get_object(Bucket=bucket_name, Key=file_name)
    records = s3_object['Body'].read().decode('utf-8').split('\n')
    count=0
    for i in range(len(records)-1):
        if i==0:
           continue
        data=records[i]
        count=count+1
        data_list=data.split(",")
        #print(data_list[1])
        Month=data_list[0]
        cupcake=data_list[1].replace('\r', '')
        #inserting data to dynamodb using boto3 put_item method
        #print(Month)
    
        response = table.put_item(
            Item={
            'id' :str(count),
            'Month' :Month,
            'cupcake':cupcake,
            }
            
        )
    
    print('Values Inserted To DynamoDB:')
