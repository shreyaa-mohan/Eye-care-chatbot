from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 

DATA_PATH = 'C:/Users/shrey/OneDrive/Desktop/newbot/Llama2-Medical-Chatbot/data/'
  # Ensure this path is correct and contains PDF files
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Create vector database
def create_vector_db():
    loader = DirectoryLoader(DATA_PATH,
                             glob='*.pdf',  # Adjust file type if needed
                             loader_cls=PyPDFLoader)

    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                                   chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks.")

    # Create embeddings using HuggingFace model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    # Create FAISS vector store
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)
    print(f"FAISS index saved to {DB_FAISS_PATH}")

if __name__ == "__main__":
    create_vector_db()

