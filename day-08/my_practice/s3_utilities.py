import boto3

class AWSutil:
    def __init__(self):
        self.s3 = self.get_connection('s3')
        self.ec2 = self.get_connection('ec2')

    def get_connection(self, service):
        return boto3.client(service)  # creating a client for s3 so that it can call APIs


    def show_buckets(self):
        response = self.s3.list_buckets()

        for bucket in response["Buckets"]:
            print(bucket["Name"])


    def create_bucket(self, bucket_name):
        try:
            response = self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    "LocationConstraint": "us-west-2",
                },
            )
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print("Bucket created successfully")
            else:
                print("Error occured while creating the bucket")
        except:
            print("Error occured")


    def show_regions(self):
        response = self.ec2.describe_regions()
        # print(response)


    def upload_to_bucket(self, file_path, bucket_name, key_name):
        self.s3.upload_file(file_path, bucket_name, key_name)
        print("File uploaded successfully")

if __name__ == "__main__":

    aws = AWSutil()
    aws.show_buckets()
