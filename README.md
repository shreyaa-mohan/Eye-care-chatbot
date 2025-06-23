# 👁️‍🗨️ Eye-Care Chatbot

A conversational AI chatbot designed to assist users with eye-care-related queries. Built with LLaMA-2, Chainlit UI, and a custom ingestion pipeline to provide helpful, context-aware responses.

---

## 📁 Project Structure

├── chainlit/ # Chainlit configuration and UI flow  
├── ingest.py # Script to load and process data  
├── model.py # Code for loading LLaMA-2 and responding to prompts  
├── requirements.txt # Python dependencies  
├── README.md # Project documentation  
└── .env # (Optional) Environment variables  


## 🚀 Features

- 🤖 AI-powered chatbot using **LLaMA-2 7B Chat** model
- 🧠 Ingestion pipeline for custom domain knowledge
- 🌐 Lightweight **Chainlit-based UI**
- 🔒 Secure use of `.env` for managing secrets or paths
- 📂 Modular code (`ingest.py`, `model.py`)

---

## 🔧 Installation

### 1. Clone the repository

- git clone https://github.com/shreyaa-mohan/Eye-care-chatbot.git
- cd Eye-care-chatbot
### 2. Set up a virtual environment (optional but recommended)

- python -m venv venv
- source venv/bin/activate     
### 3. Install dependencies

- pip install -r requirements.txt
### ⚙️ Setup
1. Add environment variables
- Create a .env file in the root directory:
- MODEL_PATH=path/to/llama-2-7b-chat.ggmlv3.q8_0.bin
  - Replace path/to/... with your actual model path.

### ▶️ Running the Chatbot
- Step 1: Ingest data  

 python ingest.py
- Step 2: Start the chatbot  

 chainlit run model.py -w
📌 Notes
- The LLaMA-2 .bin model is large and not included in the repo.

- This project is meant for educational or research use only.

📝 License
This project is licensed under the MIT License.

🙋‍♀️ Author 
Shreya Mohan  
GitHub: @shreyaa-mohan
