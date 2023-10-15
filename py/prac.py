from aifc import Error

import boto3
import json
import os
import json
import boto3
import botocore
import botocore.session as bc
from botocore.client import Config

def boto(bucket=None):
    s3_client = boto3.client('s3')
    session = boto3.session.Session()
    session.client("redshift")
    s3_client.create_bucket(Buckets=bucket)
    print("new bucket created")


def get_file_type(event):
    pass


def validate_file(event):
    if event['body']==None:
        return 'File should not be empty'

    file_type = get_file_type(event)

    if file_type!='text/csv':
        return 'file type should be csv'
    try:
        ctype = event['header']['contenttyp']
        emcode_body = event['body'].encode()
    except Error as err:
        return 'invalida filer'
    return None


def upload_file(event,timestamp):
     pass

def create_response(code,reposne):
    return {
     "satusCode":code,
    "body":json.dumps(reposne)
    }
def lambda_handler(event,context):

    err = validate_file(event)
    if err!=None:
        return create_response(400,err)

    err = upload_file(event)
    if err!=None:
        return create_response(400,err)

    return create_response(200,'file uploaded sucessfully')