# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import os
from azure.storage.blob import BlobServiceClient

def main(params):
    blob_service_client = BlobServiceClient.from_connection_string(params)
    try:
        input_texts = []
        for i in range(4):
            blob_text = download_blob_to_string(blob_service_client, "blobstore", "mrinput-"+str(i+1)+".txt")
            input_texts.append(blob_text)
        mr_input = []
        for t in input_texts:
            mr_input.extend(t.split("\n"))
        for i in range(len(mr_input)):
            mr_input[i] = (i, mr_input[i])
        return mr_input
    except Exception as ex:
        print("Exception:")
        print(ex)
    
def download_blob_to_string(blob_service_client: BlobServiceClient, container_name, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # encoding param is necessary for readall() to return str, otherwise it returns bytes
    downloader = blob_client.download_blob(max_concurrency=1, encoding='UTF-8')
    blob_text = downloader.readall()
    return blob_text