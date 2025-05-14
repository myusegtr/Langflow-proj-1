
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/fcd6a819-9d83-4380-af90-b65f32163a02/api/v1/run/22253f7f-5134-4c85-8628-2d80f47263e5"  

# Request payload configuration
payload = {
    "input_value": "show me the top 3 best apple phones",  # The input value to be processed by the flow
    "output_type": "chat",  # Specifies the expected output format
    "input_type": "chat"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR_APPLICATION_TOKEN>"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)
    print(f"Headers: {headers}")
    print(f"Payload: {payload}")

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    
