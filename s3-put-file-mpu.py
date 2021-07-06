# Uploads a file to S3 using TransferConfig

import boto3, os
from boto3.s3.transfer import TransferConfig

s3_resource = boto3.resource('s3')

config = TransferConfig(multipart_threshold=1024 * 25,
                       max_concurrency=10,
                       multipart_chunksize=1024 * 25,
                       use_threads=True)

# for bucket in s3_resource.buckets.all():
#    print(bucket.name)

# s3_resource.Object('s3policytest12', '4GBfile').\
#    upload_file(Filename='4GBfile')

bucket_name = 's3policytest12'

def multipart_upload_boto3():

    file_path = os.path.dirname(__file__) + '4GBfile'

    key = 'mission1/4GBfile'

    s3_resource.Object(bucket_name, key).upload_file(file_path,
                            ExtraArgs={'ContentType': 'text/pdf'},
                            Config=config,
                            # Callback=ProgressPercentage(file_path)
                            )

multipart_upload_boto3()
