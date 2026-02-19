import boto3
from datetime import datetime
import json


class AWSResourceReport:
    def __init__(self):
        self.ec2_client = boto3.client("ec2")
        self.s3_client = boto3.client("s3")

    def get_ec2_instances(self):
        instances_data = []

        response = self.ec2_client.describe_instances()

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances_data.append(
                    {
                        "InstanceId": instance["InstanceId"],
                        "State": instance["State"]["Name"],
                    }
                )
        return instances_data

    def get_s3_buckets(self):
        buckets_data = []

        response = self.s3_client.list_buckets()

        for bucket in response["Buckets"]:
            buckets_data.append({"BucketName": bucket["Name"]})
        return buckets_data

    def generate_report(self):
        report = {
            "GeneratedAt": datetime.utcnow().isoformat(),
            "EC2Instances": self.get_ec2_instances(),
            "S3Buckets": self.get_s3_buckets(),
        }
        return report


def main():
    aws_report = AWSResourceReport()

    report = aws_report.generate_report()

    print(json.dumps(report, indent=4))

    # Saving the file
    with open("aws_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nReport saved successfully to aws_report.json")


if __name__ == "__main__":
    main()
