# app.py
import os
import logging
from flask import Flask, request, send_from_directory
from threading import Thread
from dotenv import load_dotenv

from workflow.orchestrator import Orchestrator
from services.whatsapp_client import WhatsAppClient
from tools.converter import PDFConverter # ADDED: Import the new converter

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')

app = Flask(__name__)
whatsapp_client = WhatsAppClient()
orchestrator = Orchestrator()

def run_research_and_respond(topic: str, sender_id: str):
    """Runs the research and responds with a PDF report."""
    try:
        whatsapp_client.send_message(
            to_number=sender_id,
            body=f"🤖 Roger that! Starting research on: \"{topic}\".\n\nThis may take a few minutes. I'll send the report as a PDF when I'm done!"
        )

        final_report_md = orchestrator.run(topic)

        # CHANGED: Use .pdf extension for the report filename
        report_filename = f"{topic.replace(' ', '_').lower().replace('/', '')}_report.pdf"
        static_folder = 'static'
        os.makedirs(static_folder, exist_ok=True)
        
        file_path = os.path.join(static_folder, report_filename)

        # ADDED: Convert the Markdown report to a PDF file
        success = PDFConverter.markdown_to_pdf(final_report_md, file_path)
        if not success:
            raise Exception("Failed to convert report to PDF.")

        ngrok_url = os.getenv("NGROK_URL")
        if not ngrok_url:
            raise ValueError("NGROK_URL environment variable not set.")
        
        file_url = f"{ngrok_url}/static/{report_filename}"

        whatsapp_client.send_media(
            to_number=sender_id,
            file_url=file_url,
            caption=f"✅ Here is your research report on \"{topic}\"."
        )

    except Exception as e:
        logging.error(f"Error in research thread: {e}", exc_info=True)
        whatsapp_client.send_message(
            to_number=sender_id,
            body=f"😔 Apologies, I encountered an error while processing your request for \"{topic}\"."
        )

@app.route("/webhook", methods=["POST"])
def webhook():
    """Listens for incoming WhatsApp messages from Twilio."""
    incoming_message = request.values.get('Body', '').strip()
    sender_id = request.values.get('From', '')

    if not incoming_message or not sender_id:
        return "OK", 200

    logging.info(f"Received message '{incoming_message}' from {sender_id}")

    thread = Thread(target=run_research_and_respond, args=(incoming_message, sender_id))
    thread.start()

    return "OK", 200

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serves the generated report file."""
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(port=5000)