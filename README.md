# Langflow-proj-1

[AstraDB]
Create a database in astradb.
Add vector enabled collections to store vectors of uploaded data.
Now upload the required csv/pdf file too generate the vectors.
This will be used to perform similarity search based on the users query.
Now your database is ready to be used by agents in Langflow.

[Langflow]
Go to langflow interface, now from components section select chat_input,chat_output,AstraDB,Agents. Connect them as per flow_diagram.
Use any LLM of your choice.Add API key.

[Deployment]
Once the flow is ready go to playground,test it. 
If working properly, publish the flow & try to access using the provided API endpoint.Need to generate token for authentication purpose.Refer the api.py file.
