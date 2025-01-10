import subprocess
import sys
import threading

def run_streamlit():
    """Run the Streamlit client app."""
    subprocess.run(["streamlit", "run", "client.py"])

def run_fastapi():
    """Run the FastAPI server app."""
    subprocess.run(["uvicorn", "server:app", "--reload"])

if __name__ == "__main__":
    # Start Streamlit in a separate thread
    streamlit_thread = threading.Thread(target=run_streamlit)
    streamlit_thread.start()

    # Start FastAPI
    run_fastapi()

    # Optionally, wait for the streamlit thread to finish if necessary
    streamlit_thread.join()
