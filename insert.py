import csv
import os
def lambda_handler(event, context):
    region_name='us-east-1'
    filename='cupcake.csv'
    bucket_name='borderfree1'
    table_name='cakedata'
    records=[]
    s3=boto3.client('s3')            
    dynamodb_client = boto3.client('dynamodb', region_name=region_name)
    s3_object= s3.get_object(Bucket=bucket_name, Key=filename)
    records = s3_object['Body'].read().decode('utf-8').split('\n')
    header=True
    count=0
    for i in range(len(records)-1):
        if (header):
            header=False
            continue
        data=records[i]
        count=count+1
        data_list=data.split(",")
        Month=data_list[0]
        cupcake=data_list[1].replace('\r', '')
        
        
    #inserting data to dynamodb by using put item method
        response = dynamodb_client.put_item(
            TableName=table_name,
            Item={
            'id' :{'S':str(count)},
            'Month' : {'S':Month},
            'cupcake': {'S':cupcake},
            
            }
        )
    
    print('Values Inserted To DynamoDB:')
