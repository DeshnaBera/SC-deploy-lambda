def lambda_handler(event, context):
    # Log the received event
    print(f"Received event: {event}")
    
    # Perform your logic here
    
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
