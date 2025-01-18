import argparse
import os
from dotenv import load_dotenv
from services.s3 import S3Client
from services.gcs import GCSClient
from services.nimbusflux import NimbusFluxClient

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="NimbusCore: Interact with cloud services and APIs.")
    parser.add_argument("--service", type=str, required=True, choices=["s3", "gcs", "nimbusflux"],
                        help="The service to interact with (s3, gcs, nimbusflux).")
    parser.add_argument("--action", type=str, required=True, help="The action to perform (e.g., upload, download).")
    parser.add_argument("--file", type=str, help="File path for upload/download actions.")
    parser.add_argument("--bucket", type=str, help="Bucket name (for S3 or GCS).")

    args = parser.parse_args()

    if args.service == "s3":
        bucket_name = args.bucket or os.getenv("AWS_DEFAULT_BUCKET")
        client = S3Client(bucket_name=bucket_name,
                          access_key=os.getenv("AWS_ACCESS_KEY_ID"),
                          secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
        if args.action == "upload" and args.file:
            client.upload_file(args.file, args.file)
        elif args.action == "download" and args.file:
            client.download_file(args.file, args.file)

    elif args.service == "gcs":
        bucket_name = args.bucket or os.getenv("GCS_DEFAULT_BUCKET")
        client = GCSClient(bucket_name=bucket_name, service_account_key=os.getenv("GCS_SERVICE_ACCOUNT_KEY"))
        if args.action == "upload" and args.file:
            client.upload_file(args.file, args.file)
        elif args.action == "download" and args.file:
            client.download_file(args.file, args.file)

    elif args.service == "nimbusflux":
        client = NimbusFluxClient(api_key=os.getenv("NIMBUSFLUX_API_KEY"), base_url=os.getenv("NIMBUSFLUX_BASE_URL"))
        if args.action == "fetch":
            response = client.fetch_data()
            print("Response from NimbusFlux API:", response)

if __name__ == "__main__":
    main()
