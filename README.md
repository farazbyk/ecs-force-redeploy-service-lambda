# Lambda Force-Redeploy for ECS Services

This repository contains an AWS Lambda function that **triggers a force-redeployment of ECS services** by updating the service with the current task definition. This is useful when you want to restart services without making any actual changes to the task definition.

## 🚀 Features

- Force-redeploy ECS services programmatically via Lambda.
- Controlled through environment variables for flexibility.
- Supports multiple ECS services in one execution.
- Has permission to update ECS services and tags.

## 🛠️ Environment Variables

The Lambda function relies on two required environment variables:

| Variable        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `ECS_CLUSTER`   | The name of the ECS cluster containing the services to redeploy.           |
| `ECS_SERVICES`  | Comma-separated list of ECS service ARNs to be force-redeployed.           |

### Example Values

```env
ECS_CLUSTER=abc-cluster
ECS_SERVICES= arn_service1, arn_service2


