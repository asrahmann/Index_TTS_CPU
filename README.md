# Voice Cloning with IndexTTS-2

This project allows you to clone a voice from an audio file and generate new audio in that voice using IndexTTS-2.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Download Model Checkpoints:**
    - Download the model checkpoints from the [IndexTTS-2 Hugging Face repository](https://huggingface.co/IndexTeam/IndexTTS-2/tree/main).
    - Place all the downloaded files into the `index-tts/checkpoints/` directory.

4.  **Add Reference Audio:**
    - Place the `.wav` or `.mp3` audio file of the voice you want to clone into the `clone_voice/` directory.

## Usage

Once the setup is complete, you can run the voice cloning script:

```bash
python main.py
```

The output audio will be saved as `output_cloned.wav` in the root directory.

## About IndexTTS-2

For more information about the IndexTTS-2 model, please see the [important_readme.md](important_readme.md) file.
