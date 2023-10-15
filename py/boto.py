import boto3
from botocore.retries import bucket

def create_buckets(buck=None):
    s3_client = boto3.client('s3')
    s3_client.create_bucket(Buckets=buck)
    print("new bucket created")

create_buckets("bucks")

def list_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    print("buckets accessible by my credentail")
    for  b in response['Buckets']:
        print(f'{bucket["name"]}')


def download_files(bucket,download_path,save_as=None):
    s3_client = boto3.client('s3')


def search_files(bucket_name,file_name):
    s3_client = boto3.client('s3')
    result = s3_client.list_Object(Bucket=bucket_name,delimiter='/')
    for prefix in result['CommonPrefix']:
        object_ = prefix.get('Prefix')
        if object_ == '22/07/2021':
            files_in_each_bucket = s3_client.list()
            for content in files_in_each_bucket.get(content,[]):
                if "mobile.h5" in content['Key']:
                    print(content['Key'])