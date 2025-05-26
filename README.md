# 💬 Compassionate AI Chatbot (Local Ollama Prototype)

![image](https://github.com/user-attachments/assets/99f61317-8f39-4480-ac49-75ca70d605b9)

*A visual representation of the chatbot's supportive flow.*

## 🌟 Overview

This project presents a local-first, AI-powered chatbot designed to offer general mental well-being support. Built as a prototype, it leverages **Ollama** for running large language models (LLMs) locally and **Gradio** for creating a user-friendly web interface.

**Important Disclaimer:** This chatbot is an AI and **NOT a substitute for professional medical advice, diagnosis, or treatment.** It cannot provide personalized therapy or handle emergencies. If you are experiencing a crisis or need immediate professional support, please contact a qualified healthcare provider or emergency services. For immediate help in India, please refer to the helplines provided within the application.

## ✨ Features

* **Local AI Inference:** Runs powerful LLMs directly on your machine using Ollama, ensuring data privacy and offline capability.
* **Empathetic Responses:** Designed to provide supportive, general mental well-being advice.
* **India-Specific Context:** Offers relevant helplines and acknowledges its location (Navi Mumbai, Maharashtra, India).
* **Crisis Handling:** Detects crisis keywords and strongly advises seeking immediate professional help, providing critical helpline information.
* **Clean UI/UX:** A simple, modern web interface built with Gradio and custom CSS for a compassionate user experience.
* **Concise Responses:** LLM generation parameters are tuned for brief and to-the-point answers suitable for a chat interface.

## 🚀 Getting Started

Follow these steps to set up and run the chatbot locally on your machine.

### Prerequisites

* **Ollama:** Ensure Ollama is installed on your system. Download it from [ollama.ai](https://ollama.ai/).
* **Python:** Python 3.8+ is required.

### Local Setup Instructions

You'll need **three separate terminal windows** for this setup.

#### **Step 1: Clone the Repository & Navigate**

1.  Open your first terminal.
2.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/YourGitHubUsername/your-repo-name.git](https://github.com/YourGitHubUsername/your-repo-name.git)
    # Replace 'YourGitHubUsername/your-repo-name.git' with your actual repository details
    ```
3.  Navigate into the project directory:
    ```bash
    cd your-repo-name
    ```

#### **Step 2: Set up Python Environment & Install Dependencies**

1.  (Still in your first terminal) It's highly recommended to use a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # .\venv\Scripts\activate  # On Windows (Command Prompt)
    # .\venv\Scripts\Activate.ps1 # On Windows (PowerShell)
    ```
2.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

#### **Step 3: Start the Ollama Server**

1.  Open your **second terminal window**.
2.  Start the Ollama API server:
    ```bash
    ollama serve
    ```
    * **Leave this terminal open and running.** Your chatbot won't be able to connect to the LLM without it.

#### **Step 4: Pull the LLM Model**

1.  Open your **third terminal window**.
2.  Pull the specific model used by the application (`llama3.2:latest`):
    ```bash
    ollama pull llama3.2:latest
    ```
    * This will download the model weights. It might take some time depending on your internet speed. You can close this terminal after the model is downloaded.

#### **Step 5: Run the Gradio Chatbot Application**

1.  Go back to your **first terminal window** (where you set up the Python environment).
2.  Run the Gradio application:
    ```bash
    python app.py
    ```
    * Gradio will start and print a local URL (e.g., `http://127.0.0.1:7860`).

#### **Step 6: Access Your Chatbot**

1.  Open your web browser (Chrome, Firefox, Edge, etc.).
2.  Paste the URL provided by Gradio (e.g., `http://127.0.0.1:7860`) into your browser's address bar and press Enter.

You should now see your custom-styled chatbot interface ready for interaction!

## 📂 Project Structure
![image](https://github.com/user-attachments/assets/cd95a7ef-f9cc-446d-b3f4-d05c268b5479)
## ⚙️ Customization

* **LLM Model:** To use a different Ollama model (e.g., `phi3`), change the `OLLAMA_MODEL` variable at the top of `app.py` and run `ollama pull <new_model_name>` in your terminal.
* **System Prompt:** Modify the `messages.append({"role": "system", "content": ...})` section in the `respond` function in `app.py` to change the chatbot's core persona and guidelines.
* **UI Styling:** Edit `style.css` to further customize the chatbot's appearance. Refer to Gradio's documentation for component class names for more targeted styling.
* **Disclaimer Text:** Adjust the `gr.Markdown` sections in `app.py` for the header and disclaimer banners as needed.

## ⚠️ Important Disclaimer (Repeated)

This chatbot is for general informational and supportive purposes only. It is **not a substitute for professional medical advice, diagnosis, or treatment.** Always seek the advice of a qualified healthcare provider for any questions regarding a medical condition or mental health concerns. In case of an emergency, please contact emergency services immediately.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

* [Ollama](https://ollama.ai/) for making local LLM inference incredibly accessible.
* [Gradio](https://www.gradio.app/) for simplifying web UI creation for machine learning models.

---


