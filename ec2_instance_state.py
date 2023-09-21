import boto3
import schedule

# Initialize the EC2 client
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2', region_name="us-east-1")


# Get the list instance statuses
def check_instance_status():
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in statuses['InstanceStatuses']:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        print(f"Instance {status['InstanceId']} status is {ins_status} and system status is {sys_status}")

    print("#### END OF CYCLE #####\n")

# Schedule the job to run in a specific time interval
schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()