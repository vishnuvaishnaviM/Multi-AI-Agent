import subprocess
import threading
import time
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from dotenv import load_dotenv

logger = get_logger(__name__)

load_dotenv()

def backend():
    try:
        logger.info("Triggering backend")
        subprocess.run(["uvicorn", "app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"], check=True)
    except CustomException as e:
        logger.error("Problem with backend service")
        raise CustomException("Failed to start backend", e)

def frontend():
    try:
        logger.info("triggering frontend")
        subprocess.run(["streamlit","run","app/frontend/ui.py"], check=True)
    except CustomException as e:
        logger.error("Problem with frontend service")
        raise CustomException("Failed to start frontend", e)

if __name__=="__main__":
    try:
        threading.Thread(target=backend).start()
        time.sleep(2) # backend starts 2 sec before frontend
        frontend()
    except CustomException as e:
        logger.exception(f"CustomException occured: {str(e)}")
