import boto3
import logging

class S3Client:
    def __init__(self, bucket_name: str, access_key: str, secret_key: str, region_name: str = "us-east-1"):
        """
        Initialize the S3 client with credentials and a bucket name.
        """
        self.bucket_name = bucket_name
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name,
        )
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def upload_file(self, local_file_path: str, remote_file_name: str):
        """
        Upload a file to the S3 bucket.
        """
        try:
            self.s3.upload_file(local_file_path, self.bucket_name, remote_file_name)
            self.logger.info(f"File '{local_file_path}' uploaded to bucket '{self.bucket_name}' as '{remote_file_name}'.")
        except Exception as e:
            self.logger.error(f"Error uploading file: {e}")
            raise

    def download_file(self, remote_file_name: str, local_file_path: str):
        """
        Download a file from the S3 bucket.
        """
        try:
            self.s3.download_file(self.bucket_name, remote_file_name, local_file_path)
            self.logger.info(f"File '{remote_file_name}' downloaded from bucket '{self.bucket_name}' to '{local_file_path}'.")
        except Exception as e:
            self.logger.error(f"Error downloading file: {e}")
            raise

