import json

def lambda_handler(event, context):
    print("EVENT:", event)

    try:
        # Safely parse body (even if None)
        raw_body = event.get("body")
        body = json.loads(raw_body) if raw_body else {}

        name = body.get("name", "Guest")

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": f"Hello, {name}! Your data was received successfully."})
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Internal Server Error"})
        }
