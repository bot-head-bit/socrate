import boto3
import os

access_key=''
secret_key=''

s3=boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

def upload_s3(filename):
    try:
        s3.upload_file(
        Bucket='adithyaspersonal',
        Filename=filename,
        Key='Posts/'+filename
        )
        os.remove(filename)
    except:
        raise

def download_s3(filename):
    s3.download_file('adithyaspersonal','Posts/'+filename,"post.jpg")

def delete_s3(filename):
    s3=boto3.resource("s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1')
    s3.Object('adithyaspersonal','Posts/'+filename).delete()