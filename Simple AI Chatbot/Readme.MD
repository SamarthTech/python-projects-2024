```markdown
# Simple AI Chatbot

A simple and intuitive AI chatbot built with Streamlit and Langchain Groq. This application allows users to chat with an AI model, providing responses based on user inputs.

## Features

- **Real-time Chat**: Communicate with the AI in real-time.
- **Styled Interface**: A dark-themed UI that is user-friendly.
- **Chat History**: Retains previous messages for context.
- **Customizable**: Easily modify the design and behavior by editing the code.

## Technologies Used

- [Streamlit](https://streamlit.io/) - A framework for building web applications in Python.
- [Langchain Groq](https://github.com/langchain-ai/langchain-groq) - A library to interact with AI models.
- [dotenv](https://pypi.org/project/python-dotenv/) - To manage environment variables.

## Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/simple-ai-chatbot.git
   cd simple-ai-chatbot
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Create a `.env` file in the root directory and add your API key:

   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

Replace `app.py` with the name of your main Python file if it’s different.

## Interaction

- **Type your message** in the input box and click the **Send** button to communicate with the chatbot.
- The chatbot will respond to your messages, and the conversation will be displayed above the input box.

## Customization

You can customize the following features in the code:

- **Color Theme**: Modify the CSS styles in the `st.markdown` section for different background and text colors.
- **AI Model**: Change the `model_name` parameter when initializing `ChatGroq` to use a different model.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```