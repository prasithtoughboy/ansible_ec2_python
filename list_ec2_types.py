import sys
import boto3

#Enter your Access and Secret key
access_key = 'XXX'
secret_key = 'YYY'

client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name='us-east-1')
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
if len(sys.argv) < 2:
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "running":
                 print (instance.id, instance.instance_type)
else:
    instance_type_arg=sys.argv[1]
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            if instance.state["Name"] == "running" and instance.instance_type == instance_type_arg:
                 print (instance.id, instance.instance_type)
