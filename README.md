# **Medical Chatbot**  

## **Overview**  
The **Medical Chatbot** is a Flask-based web application that utilizes **Pinecone**, **OpenAI**, and **Hugging Face embeddings** to retrieve medical-related information and answer user queries. The chatbot is designed to provide concise and context-aware responses to users' medical inquiries.  

## **Features**  
- Uses **Pinecone** for vector search and retrieval.  
- Integrates **OpenAI API** for generating responses.  
- Employs **Hugging Face sentence embeddings** for better context understanding.  
- Web-based UI for seamless chatbot interaction.  
- Flask-powered backend with an intuitive chat interface.  

## **Tech Stack**  
- **Programming Language:** Python  
- **Frameworks & Libraries:** Flask, LangChain, Pinecone, OpenAI, Hugging Face Transformers  
- **Database:** Pinecone Vector Store  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  

## **Installation & Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/medical-chatbot.git
cd medical-chatbot
```

### **2. Create & Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Set Environment Variables**  
Create a `.env` file in the root directory and add:  
```
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

### **5. Initialize the Vector Store**  
Run the following script to process and store the data in **Pinecone**:  
```bash
python store_index.py
```

### **6. Start the Application**  
```bash
python app.py
```
The chatbot will be accessible at `http://localhost:8080/`.  

## **Usage**  
1. Open the chat interface in your browser.  
2. Ask medical-related questions, and the chatbot will generate responses.  
3. The chatbot retrieves relevant context and provides concise answers.  

## **Project Structure**  
```
medical-chatbot/
│── Biomax/               # Virtual environment files  
│── Data/                 # Data files (if applicable)  
│── research/             # Jupyter notebooks for experimentation  
│── src/                  # Core backend scripts  
│   ├── helper.py         # Functions for loading and processing data  
│   ├── prompt.py         # Defines chatbot prompts  
│   └── __init__.py       # Package initialization  
│── static/               # CSS and frontend assets  
│── templates/            # HTML files for the web UI  
│── app.py                # Flask application  
│── store_index.py        # Script to initialize Pinecone vector store  
│── test.py               # Test scripts  
│── requirements.txt      # List of dependencies  
│── setup.py              # Package setup file  
│── LICENSE               # License file  
│── README.md             # Project documentation  
```

## **Contributing**  
Contributions are welcome! Feel free to fork the repository, open issues, and submit pull requests.  

## **License**  
This project is licensed under the **MIT License**.  

