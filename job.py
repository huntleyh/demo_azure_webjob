import os
from azure.storage.queue import QueueClient
from dotenv import load_dotenv

load_dotenv()

def listen():
    queue_name = os.environ.get('QUEUE_NAME')
    connection_string = os.environ.get('QUEUE_CONNECTION_STRING')
    
    client = QueueClient.from_connection_string(conn_str=connection_string, queue_name=queue_name)
    
    while True:
        messages = client.receive_messages(max_messages=10)
        for message in messages:
            process_item(message.content)
            client.delete_message(message=message.id, pop_receipt=message.pop_receipt)

def process_item(content):
    print('Message content:', content)
    print('Processing completed')

if __name__ == "__main__":
    print('--- WebJob Execution Started ---')
    listen()
    print('--- WebJob Execution Ended ---')