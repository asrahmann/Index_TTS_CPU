import os
import sys
from pathlib import Path

# Add the cloned repository to the Python path
# This is necessary for the `indextts` import to work
sys.path.append('index-tts')

try:
    from indextts.infer_v2 import IndexTTS2
except ImportError as e:
    print("Error: Could not import from the 'indextts' library.")
    print("Please ensure you have run the installation steps correctly.")
    print(f"Import error: {e}")
    sys.exit(1)

def find_reference_audio(clone_dir="clone_voice"):
    """Finds the first audio file in the specified directory."""
    supported_formats = ('.wav', '.mp3', '.flac', '.ogg')
    for file in os.listdir(clone_dir):
        if file.lower().endswith(supported_formats):
            return os.path.join(clone_dir, file)
    return None

def main():
    """
    Main function to run the voice cloning inference.
    """
    # --- Configuration ---
    clone_audio_dir = "clone_voice"
    checkpoints_dir = "index-tts/checkpoints"
    config_path = os.path.join(checkpoints_dir, "config.yaml")
    output_path = "output_cloned.wav"
    text_to_clone = "I-It's not like I wanted to test this voice cloning thing for you! I'm just... curious, that's all! So don't go thinking this means anything, got it?"

    # --- Pre-run Checks ---
    # 1. Check if the checkpoints directory and config file exist
    if not os.path.exists(config_path):
        print(f"Error: Model config file not found at '{config_path}'")
        print("\nPlease follow the instructions in 'plans.md' to download the model checkpoints")
        print("and place them in the 'index-tts/checkpoints/' directory.")
        sys.exit(1)

    # 2. Find the reference audio file
    reference_audio = find_reference_audio(clone_audio_dir)
    if not reference_audio:
        print(f"Error: No reference audio file found in the '{clone_audio_dir}' directory.")
        print("Please place a reference audio file (e.g., a .wav) in that folder.")
        sys.exit(1)

    print("--- Starting Voice Cloning ---")
    print(f"Using reference audio: {reference_audio}")
    print(f"Text to synthesize: '{text_to_clone}'")

    try:
        # --- Initialize the Model ---
        # Set use_cuda_kernel=False to ensure it runs on CPU
        print("Loading IndexTTS-2 model... (This may take a moment)")
        tts = IndexTTS2(
            cfg_path=config_path, 
            model_dir=checkpoints_dir, 
            use_fp16=False, 
            use_cuda_kernel=False, # Explicitly disable CUDA kernels for CPU
            use_deepspeed=False
        )
        print("Model loaded successfully.")

        # --- Perform Inference ---
        print("Generating speech...")
        tts.infer(
            spk_audio_prompt=reference_audio, 
            text=text_to_clone, 
            output_path=output_path, 
            verbose=True
        )

        print("\n--- Success! ---")
        print(f"Cloned voice audio saved to: {Path(output_path).resolve()}")

    except Exception as e:
        print(f"\nAn error occurred during inference: {e}")
        print("Please ensure all model files are correctly placed and dependencies are installed.")

if __name__ == "__main__":
    main()
