# Generative AI

Welcome to the **Generative AI** repository! 🚀

This project contains various experiments and implementations of Generative AI models, including popular Chat Models and Embedding Models.

## 📁 Repository Structure

- **`ChatModels/`**: Contains scripts and implementations for various Large Language Models (LLMs) used for chat and text generation.
  - `googleAI.py`: Google's Gemini/PaLM integrations.
  - `huggingFace.py`: Hugging Face model integrations.
  - `mistralAI.py`: Mistral AI integrations.
  - `openAI.py`: OpenAI GPT integrations.
  - `tinyLamaModel.py`: TinyLlama model implementations.
- **`EmbeddingModels/`**: (Coming Soon) Implementations for text embedding models.

## 🛠️ Setup & Installation

This project uses modern Python packaging.

1. Ensure you have Python installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Munna-Kumar-1432/Generative_AI.git
   cd Generative_AI
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Alternatively, if you use `uv`, you can sync the environment using `uv.lock`)*

## 🔑 Environment Variables

To use the scripts in this repository, you'll need API keys for the respective services. 
Create a `.env` file in the root directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

## 🚀 Usage

Navigate to the `ChatModels` directory and run the desired script. For example:

```bash
python ChatModels/openAI.py
```

## 🤝 Contributing

Feel free to fork this repository and submit pull requests if you have any cool generative AI models to add!
