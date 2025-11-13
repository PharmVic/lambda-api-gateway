## 🧠 AWS Lambda + API Gateway Integration

This project demonstrates how to build and deploy a simple AWS Lambda function that connects to **Amazon API Gateway**.
It shows how to handle HTTP requests, parse JSON payloads, and return structured responses.

---

### 🚀 Features

* **AWS Lambda (Python 3.13)** as the backend
* **Amazon API Gateway** as the HTTP endpoint
* **CORS-enabled** for browser and API tool access
* **Structured JSON response handling**
* **CloudWatch Logging** for debugging

---

### 🏗️ Project Structure

```
lambda-api-gateway/
│
├── lambda_function.py       # Main Lambda code
├── role-policy.json         # IAM Role permissions
├── README.md                # Project documentation
└── .gitignore               # Optional (e.g., ignore local files)
```

---

### 🔑 IAM Role Permissions (`role-policy.json`)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

---

### 🧩 Lambda Function (Python 3.13)

```python
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    try:
        body = json.loads(event.get('body', '{}'))
        name = body.get('name', 'Guest')

        response = {
            "message": f"Hello, {name}! Your Lambda + API Gateway setup works perfectly 🚀"
        }

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(response)
        }

    except Exception as e:
        logger.error("Error handling API request: %s", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }
```

---

### ⚙️ Setup Steps

1. **Create Lambda Function**

   * Runtime: `Python 3.13`
   * Handler: `lambda_function.lambda_handler`
   * Attach IAM role with CloudWatch log permissions

2. **Create API Gateway**

   * Type: `REST API`
   * Create a new **Resource** (e.g., `/hello`)
   * Add **POST method**
   * Integrate with your Lambda
   * Enable **CORS**

3. **Deploy API**

   * Create a new stage (e.g., `dev`)
   * Copy the endpoint URL

---

### 🧪 Test Using Postman or API Gateway

**Request**

* Method: `POST`
* URL: `https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/dev/hello`
* Body → Raw → JSON

```json
{
  "name": "Victor"
}
```

**Response**

```json
{
  "message": "Hello, Victor! Your Lambda + API Gateway setup works perfectly 🚀"
}
