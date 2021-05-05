from aws_credentials import aws_credentials
import boto3
from botocore.client import Config


def upload_to_s3(file_data, username, filename):

    credentials = aws_credentials()

    s3_resource = boto3.resource(
        's3',
        aws_access_key_id = credentials.access_key,
        aws_secret_access_key = credentials.secret_key,
        config=Config(signature_version='s3v4')
    )

    key = username +"___"+ filename
    s3_bucket_name = "uploaded-raw-invoices"
    response = s3_resource.meta.client.upload_fileobj(Fileobj = file_data, Bucket = s3_bucket_name,Key = key,ExtraArgs={'ACL': 'public-read'})
    bucket_location = s3_resource.meta.client.get_bucket_location(Bucket=s3_bucket_name)
    object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['LocationConstraint'],
        s3_bucket_name,
        key)
    print(type(object_url))
    print(object_url)
    return object_url


# file_Data = open("new_invoice.jpeg", "rb")
# filename = "new_invoice.jpeg"
# upload_to_s3(file_Data, "test_user", filename)

