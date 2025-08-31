import moonshine_onnx
import tokenizers
import wave
import numpy as np
import time

tokenizer = tokenizers.Tokenizer.from_file("models/base/tokenizer.json")
model = moonshine_onnx.MoonshineOnnxModel(model_name="models/base")

with wave.open('beckett.wav', 'rb') as wf:
    audio = wf.readframes(wf.getnframes())
    sr = wf.getframerate()
    if sr != 16000:
        raise ValueError(f"Sample rate {sr} is not 16000")
    audio = np.frombuffer(audio, dtype=np.int16).astype(np.float32) / 32768.0

start_time = time.time()
tokens = model.generate(audio.reshape(1, -1))[0]
transcription_duration = time.time() - start_time
audio_duration = audio.shape[0] / sr
print(f"Generation time: {transcription_duration:.2f} seconds, {audio_duration/transcription_duration:.2f}x real time")
text = tokenizer.decode(tokens).strip()
print(text)