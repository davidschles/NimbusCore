import argparse
from services.s3 import S3Client
from services.gcs import GCSClient
from services.nimbusflux import NimbusFluxClient

def main():
    parser = argparse.ArgumentParser(description="NimbusCore: Interact with cloud services and APIs.")
    parser.add_argument("--service", type=str, required=True, choices=["s3", "gcs", "nimbusflux"],
                        help="The service to interact with (s3, gcs, nimbusflux).")
    parser.add_argument("--action", type=str, required=True, help="The action to perform (e.g., upload, download).")
    parser.add_argument("--file", type=str, help="File path for upload/download actions.")
    parser.add_argument("--bucket", type=str, help="Bucket name (for S3 or GCS).")

    args = parser.parse_args()

    if args.service == "s3":
        client = S3Client(bucket_name=args.bucket)
        if args.action == "upload" and args.file:
            client.upload_file(args.file, args.file)
        elif args.action == "download" and args.file:
            client.download_file(args.file, args.file)

    elif args.service == "gcs":
        client = GCSClient(bucket_name=args.bucket)
        if args.action == "upload" and args.file:
            client.upload_file(args.file, args.file)
        elif args.action == "download" and args.file:
            client.download_file(args.file, args.file)

    elif args.service == "nimbusflux":
        client = NimbusFluxClient()
        if args.action == "fetch":
            response = client.fetch_data()
            print("Response from NimbusFlux API:", response)

if __name__ == "__main__":
    main()
