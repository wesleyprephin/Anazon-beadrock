#Imports
from langchain.chains import RetrievalQA
from langchain_community.llms import Bedrock
from langchain_community.retrievers import AmazonKendraRetriever

#Define the retriever
retriever = AmazonKendraRetriever(
  knowledge_base_id = "MGWNXWKKQ4",
  retrieval_config = {"vectorSearchConfiguration": {"numberOfResults":4}}
)

#Define model parameters
model_kwargs_claude = {
  "temprature": 0,
  "top_k": 10,
  "max_tokens_to_sample": 750
}

#Configure llm

llm = Bedrock(model_id = "anthropic.claude-instance-v1", model_kwargs =  model_kwargs_claude)

#Configure the chain
qa = RetrievalQA.from_chain_type(
  llm = llm,
  retriever = retriver,
  return_source_documents = True
)
#Get user input and display the result
while True:
  query = input("\n Ask a question - ")
  output = qa.invoke(query)
  print(output['result'])
