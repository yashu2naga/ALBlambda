import json

import boto3

client=boto3.client('emr')

response = client.list_instances(

   ClusterId='j-1S68XXTK9F863',

   InstanceGroupTypes=['MASTER'])

instance_id=response['Instances'][0]['Ec2InstanceId']

print(instance_id)

ssm_client=boto3.client('ssm')

put_parameter=ssm_client.put_parameter(

    Description='master instance id of an emr cluster',

    Name='Instance-id',

    Value=instance_id,

    Type='String',

    Overwrite= False,

    Tier='Standard',

    DataType='text')
