import boto3


def get_ec2_summary(region="us-west-2"):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances()
    instances = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(
                {
                    "InstanceId": instance["InstanceId"],
                    "InstanceType": instance["InstanceType"],
                    "State": instance["State"]["Name"],
                }
            )
    return instances
