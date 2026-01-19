import streamlit
import requests
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

streamlit.set_page_config(page_title="MULTI AI AGENT", layout="centered")
streamlit.title("Multi AI Agent using Groq and Tavily")

system_prompt = streamlit.text_area("Define your AI Agent: ", height=70)
selected_model = streamlit.selectbox("Select your AI Model: ", settings.ALLOWED_MODEL_NAMES)
allow_web_search = streamlit.checkbox("Allow web search")
query=streamlit.text_area("Enter your question: ", height=150)
API_URL = "http://127.0.0.1:9999/chat"


if streamlit.button("Ask agent") and query.strip():
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [query],
        "allow_search": allow_web_search
    }

    try:
        logger.info("sending request to FASTAPI")
        response = requests.post(API_URL, json=payload)
        if response.status_code==200:
            agent_response = response.json().get("response","")
            logger.info("Successfully received response from backend")
            streamlit.subheader("Agent response: ")
            streamlit.markdown(agent_response.replace("\n","<br>"), unsafe_allow_html=True)
        else:
            logger.error("Backend error")
            streamlit.error("Error in getting response from Backend")
    except Exception as e:
        logger.error("Error occured while sending request to backend")
        streamlit.error(str(CustomException("Failed to communicate with backend")))

