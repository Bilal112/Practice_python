import os

import vertexai
from vertexai.preview.generative_models import GenerativeModel

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__)) 

# Set the path to the Google Cloud credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
    current_dir, 'chat-app-d8550-0534a29e2468.json')

# Google Cloud project ID and location
project_id = 'chat-app-d8550'
location = 'us-central1'

async def init_vertexai():
    """
    Initialize the Vertex AI client and load the Gemini model.
    
    Returns:
        GenerativeModel: An instance of the Gemini 1.5 Pro model
    """
    # Initialize Vertex AI with project and location
    vertexai.init(project=project_id, location=location)
    
    # Load the Gemini 1.5 Pro model
    model = GenerativeModel(os.getenv("VERTEX_GEMINI_MODEL"))
    print("Model loaded successfully")
    
    return model