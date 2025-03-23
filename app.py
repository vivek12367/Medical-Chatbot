from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import system_prompt
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
HF_TOKEN = os.getenv("HF_TOKEN")

embeddings = download_hugging_face_embeddings()


index_name = "test"

# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})


llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",  # Replace with another HF model if needed
    temperature=0.4,
    model_kwargs={"token": HF_TOKEN, "max_length": "500"}
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), 
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"].strip()

    # Optional: Handle greetings directly
    greetings = ["hi", "hello", "hey"]
    if msg.lower() in greetings:
        return "Hi there! How can I help you today?"

    # Get RAG response
    response = rag_chain.invoke({"input": msg})
    raw_answer = response["answer"]

    # Clean up unwanted role labels and extra commas
    cleaned_answer = (
        raw_answer.replace("Mini:", "")
                  .replace("Mini", "")
                  .replace("User:", "")
                  .replace("User", "")
                  .lstrip(", ")
                  .strip()
    )

    return cleaned_answer


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)