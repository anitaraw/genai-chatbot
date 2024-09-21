# GenAI Chatbot

### This project implements a GenAI chatbot using the llama_cpp Mistral-7B-Instruct-v0.2 model. The chatbot provides an interactive interface built with Streamlit, allowing users to engage in a conversation with the AI.


## Features

* Interactive chatbot interface built with Streamlit.
* Utilizes the Mistral-7B-Instruct model for generating responses.
* Keeps track of the conversation history for a seamless user experience.
* Easy deployment using Docker.

## Installation

### Prerequisites

* Docker installed on your machine.
* Basic knowledge of Docker and Python.

* Clone the Repository

```
git clone [git_hub_link](https://github.com/anitaraw/genai-chatbot.git)
cd genai-chatbot

```

* Build the Docker Image
```
docker build -t genai-chatbot .

```

### Usage

* Run the streamlit app in your local

```
streamlit run ui.py

```

* Run the Docker Container:

```

docker run -p 8501:8501 genai-chatbot

```

* Access the Chatbot: Open your web browser and navigate to http://localhost:8501 to interact with the chatbot.

### Project Structure

```

genai-chatbot/
├── Dockerfile            # Docker configuration file
├── requirements.txt      # Python dependencies
├── app/
│   ├── ui.py            # Streamlit UI code
│   └── model_inference.py           # Llama Mistral model integration code
└── models/
    └── mistral-7b-instruct-v0.2.Q4_0.gguf  # Pre-trained model

```

*  **Note:** You can download the mistral model from [Hugging Face](https://huggingface.co/kaushiksiva07/Mistral-7B-Instruct-v0.2-Q4_0-GGUF)

### Dependencies

* The following dependencies are required for the project:

Streamlit
llama-cpp-python
scikit-learn
numpy
scipy
other dependencies listed in requirements.txt

You can install these dependencies using:

```
pip install -r requirements.txt

```

### License

This project is licensed under the MIT License.

### Acknowledgements

* Llama.cpp for the implementation of the Llama model.
* Streamlit for the web application framework.
