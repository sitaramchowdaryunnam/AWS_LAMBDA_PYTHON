import json
import logging
import boto3
from botocore.exceptions import ClientError


def lambda_handler(file_name, bucket, object_name=None):
    file_name = 'zabbix'
    bucket    = 'ntttd'
    """Upload a file to an S3 bucket

    :parametereter file_name: File to upload(The file you want upload should exist in the pc)
    :parameter bucket: Bucket to upload to
    :parameter object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True