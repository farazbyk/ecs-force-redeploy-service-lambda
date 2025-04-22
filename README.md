# Lambda Force-Redeploy for ECS Services

This Lambda function triggers a **force-redeployment** of ECS services by re-registering the existing task definition. Useful for refreshing running services without changing their definitions.

---

## 📦 Project Structure

```
.
├── lambda_function.py   # Main handler logic
├── README.md            # Documentation
└── ...                  # Infra or deployment files (if any)
```

---

## ⚙️ Environment Variables

| Variable       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `ECS_CLUSTER`  | Name of the ECS cluster                                                     |
| `ECS_SERVICES` | Comma-separated ECS service ARNs to be force-redeployed                     |

### Example

```env
ECS_CLUSTER=production_cluster
ECS_SERVICES=arn_service1, arn_service2

```

---

## 🔐 Required IAM Permissions

The Lambda function should be assigned an IAM role with the following permissions:

```json
{
  "Effect": "Allow",
  "Action": [
    "ecs:UpdateService",
    "ecs:DescribeServices",
    "ecs:TagResource"
  ],
  "Resource": "*"
}
```

> 🎯 Tip: For production, it's better to scope the `Resource` to specific ECS cluster and service ARNs.

---

## 🚀 Usage

You can trigger the function manually, on a schedule using Amazon EventBridge, or programmatically from other AWS services or automation tools.

---

## 👤 Author

Maintained by **Faraz Bin Younus**
