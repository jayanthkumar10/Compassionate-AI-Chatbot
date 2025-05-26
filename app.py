import gradio as gr
import ollama
import time

# --- Ollama Configuration ---
OLLAMA_MODEL = "llama3.2:latest" # Use the exact model name from your 'ollama list' output

# --- Define the chatbot response function ---
def respond(message: str, history: list):
    messages = []
    messages.append({
        "role": "system",
        "content": (
            "You are a helpful and empathetic AI assistant providing general mental well-being support. "
            "Provide supportive responses and information, always reminding the user that you are not a substitute for professional medical advice or emergency services. "
            "When suggesting resources, keep in mind the user's likely location in India. Keep responses concise and to the point for a chat interface, ideally under 100 words unless detail is specifically requested."
        )
    })

    for human, bot in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": bot})

    messages.append({"role": "user", "content": message})

    start_inference_time = time.time()
    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=messages,
            options={
                "temperature": 0.7,
                "top_k": 50,
                "top_p": 0.95,
                "num_predict": 150 # Max new tokens to generate for concise responses
            }
        )
        decoded_output = response['message']['content'].strip()

    except Exception as e:
        print(f"Error calling Ollama API: {e}")
        if "Connection refused" in str(e) or "Failed to connect" in str(e):
            decoded_output = (
                "I'm sorry, I can't connect to the local AI. "
                "Please ensure your Ollama server is running in a separate terminal (`ollama serve`)."
            )
        else:
            decoded_output = "I'm sorry, I encountered an error while processing your request. Please try again."
    finally:
        end_inference_time = time.time()
        print(f"Ollama Inference Time: {end_inference_time - start_inference_time:.2f} seconds")

    disclaimer = (
        "\n\n**Important:** I'm an AI, not a professional. "
        "For urgent help, contact a healthcare provider or emergency services. "
        "**India Helplines:** 108 (Emergency), AASRA (022-27546669), Vandrevala F. (1860-2662-345)."
    )

    message_lower = message.lower()
    if any(keyword in message_lower for keyword in ["crisis", "suicide", "emergency", "harm myself", "help me now", "suicidal thoughts"]):
        decoded_output += "\n\n**Please seek immediate professional help.** " + disclaimer
    else:
        decoded_output += disclaimer

    return decoded_output

# --- Gradio Interface with Custom UI ---
with gr.Blocks(
    css=open("style.css").read(),
    analytics_enabled=False,
    # Use Base theme for minimal default styling, easier to override.
    # Set hues to ensure light theme.
    theme=gr.themes.Base(primary_hue="green", neutral_hue="gray")
) as demo:
    # Custom Header
    gr.Markdown(
        """
        <div class="chat-header-custom">
            <h1>Compassionate AI Chatbot</h1>
            <p class="tagline">Your confidential space for general well-being support.</p>
        </div>
        """
    )

    # Important Disclaimer Banner (significantly shortened)
    gr.Markdown(
        """
        <div class="disclaimer-banner-custom">
            <h2>Important Disclaimer:</h2>
            <p>
                I am an AI. I cannot provide medical advice, diagnosis, or treatment. I am not a substitute for professional mental health care.
                **If you are in crisis, please seek immediate help.**
                <br><br>
                **India Helplines:** 108 (Emergency) | AASRA (022-27546669) | Vandrevala Foundation (1860-2662-345) | iCALL (022-25521111)
            </p>
        </div>
        """
    )

    # The core chat interface, styled by your CSS
    gr.ChatInterface(
        fn=respond,
        chatbot=gr.Chatbot(height=500),
        textbox=gr.Textbox(placeholder="Type your message here...", container=False),
    )

# Launch the Gradio app
demo.launch(share=True)
