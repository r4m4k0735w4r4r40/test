import json
import csv
import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    dynamodb = boto3.resource('dynamodb')

    # Function to validate the credentials
    def verify_credentials(user_name, password):
        bucket = "testrk-bucket"
        file_name = "user_data.csv"
        bucket_res = s3_client.get_object(Bucket=bucket, Key=file_name)
        user_data = (bucket_res['Body'].read()).decode("utf-8").splitlines()
        user_data = csv.reader(user_data)
        next(user_data)
        for line in user_data:
            if (line[0] == user_name and line[1] == password):
                return True
        return False

    # Function to return user details from db
    def get_user_data(user_name):
        table = dynamodb.Table('test-table-2')
        response = table.get_item(
            Key={
                'user_name': user_name,
            }
        )
        item = response['Item']
        item.pop('user_name')
        return item

    # Function to validate required fields are give or not.
    def validate(credentials):
        error = dict()
        valid = True
        if 'user_name' not in credentials:
            error['user_name'] = "Username is required."
            valid = False
        if 'password' not in credentials:
            error['password'] = "Password is required."
            valid = False
        return valid, error

    credentials = event['body-json']
    valid, error = validate(credentials)
    if (valid):
        if (verify_credentials(credentials['user_name'], credentials['password'])):
            res = get_user_data(credentials['user_name'])
            return res
        else:
            return {"error": "Invalid Credentials"}
    else:
        return error
