import boto3

ec2_client_verginia = boto3.client('ec2', region_name="us-east-1")
ec2_resource_virginia = boto3.resource('ec2', region_name="us-east-1")

ec2_client_cali = boto3.client('ec2', region_name="us-west-1")
ec2_resource_cali = boto3.resource('ec2', region_name="us-west-1")

instance_ids_virginia = []
instance_ids_cali = []

reservations_verginia = ec2_client_verginia.describe_instances()['Reservations']
for res in reservations_verginia:
    instances = res['Instances']
    for ins in instances:
        instance_ids_virginia.append(ins['InstanceId'])

if instance_ids_virginia:
    response = ec2_resource_virginia.create_tags(
        Resources=instance_ids_virginia,
        Tags=[
            {
                'Key': 'environment',
                'Value': 'prod'
            },
        ]
    )

    print(f"Tagging in Virginia: {response}")
else:
    print("No instances found in Virginia.")

reservations_cali = ec2_client_cali.describe_instances()['Reservations']
for res in reservations_cali:
    instances = res['Instances']
    for ins in instances:
        instance_ids_cali.append(ins['InstanceId'])

if instance_ids_cali:
    response = ec2_resource_cali.create_tags(
        Resources=instance_ids_cali,
        Tags=[
            {
                'Key': 'environment',
                'Value': 'stage'
            },
        ]
    )

    print(f"Tagging in California: {response}")
else:
    print("No instances found in California.")
