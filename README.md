# 🛒 AI Shopping Assistant — Electronics Store (Langflow + AstraDB)

This is an **AI-powered shopping assistant** project built using **Langflow** and **AstraDB**, designed to simulate an experience similar to **Flipkart/Amazon**. The assistant can answer product-related queries using vector similarity search powered by LLMs and AstraDB.

---

## 🔧 Tech Stack

- **Langflow** (Drag-and-drop LLM application builder)
- **DataStax AstraDB** (Vector-enabled NoSQL DB)
- **LLMs** (via Groq/OpenAI/HuggingFace)
- **Python** (for API integration)
- **Postman** (for testing API)

---

## 🚀 Project Features

- Vector similarity search for product discovery  
- Intelligent product recommendations  
- Natural language query handling  
- API access to the deployed Langflow flow  
- Token-based authentication  
- Easily customizable for any e-commerce domain

---

## 🗂️ Project Structure

```
├── api.py                 # Script to invoke Langflow API
├── shopping_data.csv      # (Example) Electronics product data
├── README.md              # Project documentation (this file)
└── screenshots/           # Postman setup screenshots (optional)
```

---

## 🧱 Steps to Build the Project

### 📁 1. Create AstraDB Vector Database

- Sign in to [AstraDB](https://www.datastax.com/astra)
- Create a new **vector-enabled database**
- Add a **collection** for products (e.g., `electronics_catalog`)
- Upload your dataset (`CSV` or `PDF`)
- Select the appropriate field (`description` or custom `embedding_input`) for **vectorization**
- Enable Tool Mode for this vector store (required for Langflow)

---

### 🎨 2. Create Flow in Langflow

- Go to [Langflow Studio](https://astra.datastax.com/langflow)
- Create a new flow:
  - Add the following components:
    - `Chat Input`
    - `Prompt Template` (optional)
    - `Agent` (set instructions)
    - `LLM` (Groq/OpenAI)
    - `AstraDB` (as tool)
    - `Chat Output`
  - Connect the components as per the layout:
    ```
    Chat Input → Agent → Chat Output
                      ↘︎
                     AstraDB
    ```
- Add your API keys (Groq, OpenAI, etc.)
- Save and **publish** the flow

---

### 🧪 3. Test in Playground

- Go to the **Playground** tab inside Langflow
- Ask: `Show me top 3 Samsung phones under ₹15,000`
- If it works as expected, **publish the flow** to make it accessible via API

---

## 🔐 Authentication

To use the published flow via API, you must generate an **Application Token**:

1. Go to your Langflow dashboard
2. Click on your project → **API Settings**
3. Generate an Application Token
4. Use it in the `Authorization` header as shown below

---

## 📡 API Access

Use `api.py` to send queries to the Langflow flow.

### 🔧 Replace:

- `<YOUR_APPLICATION_TOKEN>` with your actual application token
- `input_value` with your custom query

### ▶️ Run the script:

```bash
python api.py
```

### 🧪 Sample Code

```python
import requests

url = "https://api.langflow.astra.datastax.com/lf/fcd6a819-9d83-4380-af90-b65f32163a02/api/v1/run/22253f7f-5134-4c85-8628-2d80f47263e5"

payload = {
    "input_value": "show me the top 3 best apple phones",
    "output_type": "chat",
    "input_type": "chat"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR_APPLICATION_TOKEN>"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
```

---

## 📬 Test via Postman

1. Open Postman
2. Select **POST** method
3. Enter the same API endpoint
4. In **Authorization** tab:
   - Type: **Bearer Token**
   - Token: `<YOUR_APPLICATION_TOKEN>`
5. In **Body** → `raw` → `JSON`:
```json
{
  "input_value": "Suggest me best noise cancelling headphones under 5000",
  "output_type": "chat",
  "input_type": "chat"
}
```
6. Click **Send**

---

## 📌 Notes

- Ensure the vector collection is created with semantic-rich fields (e.g., `description`)
- You can customize the agent's behavior in Langflow (e.g., "Act as a shopping assistant for electronics.")
- AstraDB handles vector similarity using `LangChain`-compatible APIs

---

## ✅ Future Enhancements

- Integrate image-based search
- Add user feedback collection and fine-tuning
- Deploy with a front-end using Streamlit or React

---

## 📞 Support

Need help? Raise an issue or contact the project maintainer.
