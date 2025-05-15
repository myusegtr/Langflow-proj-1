import streamlit as st
import requests
import json

# Page config
st.set_page_config(page_title="AI Shopping Assistant", layout="wide")
st.title("🛒 AI Shopping Assistant")

# User input
user_query = st.text_input("Ask me something:", placeholder="e.g., show me the top 3 best Xiaomi phones")

# Define the API endpoint and headers
url = "https://api.langflow.astra.datastax.com/lf/fcd6a819-9d83-4380-af90-b65f32163a02/api/v1/run/22253f7f-5134-4c85-8628-2d80f47263e5"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR_TOKEN>"
}

# Show response on form submission
if st.button("Get Results") and user_query.strip():
    payload = {
        "input_value": user_query,
        "output_type": "chat",
        "input_type": "chat"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        # ✅ Extract only the relevant "messages" part
        messages = result["outputs"][0]["outputs"][0]["messages"]
        message_texts = [msg["message"] for msg in messages]

        # readable_text = "\n".join([f"{key.capitalize()}: {value}" for key, value in message_texts.items()])
        # st.write(readable_text)
        # Show cleaned output
        #st.json({"messages": message_texts})
        st.write(message_texts[0])

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
    except (ValueError, KeyError, IndexError):
        st.error("Failed to parse the expected structure from response.")
