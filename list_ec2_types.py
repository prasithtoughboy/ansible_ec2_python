from pprint import pprint
import sys
import boto3

types = []
count = 0
access_key = 'XXX'
secret_key = 'YYY'
client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name='us-east-1')
ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
if len(sys.argv) < 2:
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
             print (instance.id, instance.instance_type, region)
elif len(sys.argv) == 2:
    instance_type_arg=sys.argv[1]
    for region in ec2_regions:
        conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,region_name=region)
        instances = conn.instances.filter()
        for instance in instances:
            types.append(instance.instance_type)
            if instance.instance_type == instance_type_arg:
                 print (instance.id, instance.instance_type)
    for itype in range(len(types)):
       if types[itype] != instance_type_arg:
          count = count + 1
          if count == len(types):
             print "Enter a valid instance type"
