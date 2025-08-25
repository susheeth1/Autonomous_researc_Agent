# AI-Powered WhatsApp Research Assistant

## 📌 Introduction

This project is a sophisticated, autonomous multi-agent system designed to streamline the research process through a conversational WhatsApp interface. It addresses the time-consuming nature of modern research by delegating the entire workflow—from initial information gathering to final report synthesis—to a team of specialized AI agents.

With a simple WhatsApp message, a user initiates a complex research task and receives a comprehensive, formatted PDF report in return. The system demonstrates the practical application of advanced AI, cloud communication technologies, and secure automation.

---

## ⚙️ Workflow Overview

The workflow is a carefully orchestrated sequence of steps:

### 1. **User → Trigger**

* The user sends a WhatsApp message (e.g., *"Impact of 5G on IoT"*) to a Twilio number.

### 2. **WhatsApp → Interface**

* Acts as a familiar chat interface.
* Transmits the user’s message and number to Twilio.

### 3. **Twilio → Communication Gateway**

* Twilio bridges WhatsApp and the Flask backend.
* Incoming messages are forwarded to our webhook.

### 4. **Ngrok → Secure Tunnel**

* Ngrok exposes the local Flask server to the internet.
* Provides a secure public URL for Twilio webhooks.

### 5. **Flask Server → Backend Entrypoint**

* `app.py` receives the webhook event.
* Extracts the message & phone number.
* Immediately acknowledges the user with a response via Twilio.
* Spawns a background thread to handle the research process.

### 6. **Orchestrator → Project Manager**

* Manages the workflow like an assembly line.
* Ensures each AI agent performs its step in the correct order.

### 7. **Agent Team → Specialists**

* **Knowledge Agent:** Generates background & definitions.
* **Research Agent:** Uses `serper.dev` + scraping (Requests + BeautifulSoup4) to gather sources.
* **Summarizer Agent:** Summarizes each scraped source.
* **Analyzer Agent:** Synthesizes insights across sources.
* **Report Agent:** Assembles everything into a final Markdown report.

### 8. **PDF Generation → Final Product**

* The Markdown report is converted to a PDF using **fpdf2 with DejaVu Sans Unicode font**.
* Output is saved in `/static`.

### 9. **Delivery → Return Journey**

* Flask calls the WhatsApp client.
* Twilio delivers the generated PDF to the user’s WhatsApp as a media message.

---

## 🛠️ Technology Deep Dive

* **Flask** → Lightweight Python web framework, receives Twilio webhooks.
* **openai** → Connects to GPT models (`gpt-4o-mini`) for agent reasoning & generation.
* **twilio** → Sends acknowledgment + delivers the final PDF via WhatsApp.
* **serpapi** → Interfaces with `serper.dev` for Google Search API access.
* **requests** → Downloads raw HTML content for scraping.
* **BeautifulSoup4** → Parses and cleans HTML to extract readable text.
* **fpdf2\[markdown]** → Converts Markdown to Unicode-safe PDF output.
* **python-dotenv** → Loads environment variables securely from `.env`.

---

## 📂 Project Structure

```
Autonomous_research_Agent/
│── app.py                  # Flask server entrypoint
│── /agents                 # AI agent implementations
│── /services               # Twilio WhatsApp client, orchestrator
│── /tools                  # Utilities like PDF converter
│── /static                 # Generated PDFs
│── .env                    # API keys & secrets
│── requirements.txt        # Python dependencies
```

---

## 🚀 Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Autonomous_research_Agent.git
cd Autonomous_research_Agent
```

2. **Create virtual environment & install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

3. **Set up environment variables in `.env`**

```
OPENAI_API_KEY=your_openai_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
SERPER_API_KEY=your_serper_key
```

4. **Run Flask server**

```bash
python app.py
```

5. **Start ngrok tunnel**

```bash
ngrok http 5000
```

6. **Configure Twilio webhook**

* In the Twilio console, set your WhatsApp number’s webhook URL to the ngrok URL:

```
https://<your-ngrok-id>.ngrok-free.app/webhook
```

---

## 📄 Usage

* Open WhatsApp → Send a message to your Twilio number:

  ```
  "Impact of LLMs on the job market"
  ```
* Wait a few minutes.
* Receive a **PDF research report** back via WhatsApp.

---

## 🔒 Security Notes

* Store API keys in `.env`, never in source code.
* Use ngrok only for development. For production, deploy Flask on a secure server with HTTPS.
* Twilio webhooks must remain private to prevent spam abuse.

---

## 📚 Future Improvements

* Add caching of scraped articles.
* Improve PDF formatting (headings, bullet styling).
* Add support for images/graphs in reports.
* Deploy as a Docker container for portability.

---

## 👨‍💻 Author

**Susheeth G**
B.Tech in Information Science & Engineering (AI & Robotics)
Presidency University

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
