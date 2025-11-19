# Voice Cloning with IndexTTS-2

This project allows you to clone a voice from an audio file and generate new audio in that voice using IndexTTS-2. This version is configured to run on a CPU, so please be aware that inference will be slow.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/asrahmann/Index_TTS_CPU.git
    cd Index_TTS_CPU
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Download Model Checkpoints:**
    - Download all model files from the [IndexTTS-2 Hugging Face repository](https://huggingface.co/IndexTeam/IndexTTS-2/tree/main).
    - Place all of these downloaded files into the `index-tts/checkpoints/` directory.

4.  **Add Reference Audio:**
    - Place a short (5-10 seconds), clear `.wav` or `.mp3` audio file of the voice you want to clone into the `clone_voice/` directory.

## Usage

1.  **Modify the Prompt:**
    - Open the `main.py` file.
    - Find the line that says: `text = "Your Text Here"`
    - Change the text inside the quotes to whatever you want the cloned voice to say.

2.  **Run the script:**
    - Once the setup is complete and you have modified the prompt, you can run the voice cloning script:
    ```bash
    python main.py
    ```

## User Experience

When you run `python main.py`:

1.  The script will load the IndexTTS-2 model. You will see model loading messages in your console.
2.  It will then perform voice cloning and text-to-speech synthesis. **This step will take a significant amount of time on a CPU.** Please be patient.
3.  Once finished, the output audio will be saved as `output_cloned.wav` in the root directory. You can then play this file to hear the result.


## About IndexTTS-2

IndexTTS-2 is a breakthrough in emotionally expressive and duration-controlled auto-regressive zero-shot text-to-speech.

- [Hugging Face Model](https://huggingface.co/IndexTeam/IndexTTS-2)
- [GitHub Repository](https://github.com/index-tts/index-tts)

### Acknowledgements

- [tortoise-tts](https://github.com/neonbjb/tortoise-tts)
- [XTTSv2](https://github.com/coqui-ai/TTS)
- [BigVGAN](https://github.com/NVIDIA/BigVGAN)
- [wenet](https://github.com/wenet-e2e/wenet/tree/main)
- [icefall](https://github.com/k2-fsa/icefall)
- [maskgct](https://github.com/open-mmlab/Amphion/tree/main/models/tts/maskgct)
- [seed-vc](.DS_Store)

### Citation

If you find this work helpful, please cite the original paper:

```
@article{zhou2025indextts2,
  title={IndexTTS2: A Breakthrough in Emotionally Expressive and Duration-Controlled Auto-Regressive Zero-Shot Text-to-Speech},
  author={Siyi Zhou, Yiquan Zhou, Yi He, Xun Zhou, Jinchao Wang, Wei Deng, Jingchen Shu},
  journal={arXiv preprint arXiv:2506.21619},
  year={2025}
}
```
