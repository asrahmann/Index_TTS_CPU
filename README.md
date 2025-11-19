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
- [seed-vc](https://github.com/Plachtaa/seed-vc)

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
