import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = (reservation["Instances"])
    for instance in instances:
        print(f"Status of instance {instance['InstanceId']} is: {instance['State']['Name']}")
