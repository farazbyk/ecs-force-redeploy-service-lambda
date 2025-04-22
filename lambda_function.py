import boto3
import os
import time

ecs = boto3.client('ecs')

def lambda_handler(event, context):
    cluster = os.environ['ECS_CLUSTER']
    services = os.environ['ECS_SERVICES'].split(',')
    delay_seconds = int(os.environ.get('DELAY_BETWEEN_DEPLOYS', 60))

    for svc in services:
        svc_name = svc.strip()
        print(f"Redeploying service: {svc_name}")

        ecs.update_service(
            cluster=cluster,
            service=svc_name,
            forceNewDeployment=True
        )
        print(f"Waiting {delay_seconds} seconds before next service...")
        time.sleep(delay_seconds)

    return {
        'statusCode': 200,
        'body': f"Redeploy done for {len(services)} services with {delay_seconds}s interval."
    }

