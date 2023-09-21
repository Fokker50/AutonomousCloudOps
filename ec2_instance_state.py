import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = (reservation["Instances"])
    for instance in instances:
        print(f"Status of instance {instance['InstanceId']} is: {instance['State']['Name']}")

statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    print(f"Instance {status['InstanceId']} status is {ins_status} and system status is {sys_status}")
