import boto3
import botocore
from settings import config

def read_file_S3(bucketname, itemname):
  s3_client = boto3.client(
    's3',
    aws_access_key_id=config["AWS_ACCESS_KEY"],
    aws_secret_access_key=config["AWS_SECRET_ACCESS_KEY"],
    aws_session_token=config["AWS_SESSION_TOKEN"]
  )

  try:
    obj = s3_client.get_object(Bucket=bucketname, Key=itemname)
    body = obj['Body'].read()

    return body

  except botocore.exceptions.ClientError as error:
    raise error

  except botocore.exceptions.ParamValidationError as error:
    raise ValueError('The parameters you provided are incorrect: {}'.format(error))
  
