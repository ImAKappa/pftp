"""transcription (ffmpeg)

This module transcribes audio files (.wav)
"""
import subprocess
import sys
import ast
from pathlib import Path
from dataclasses import dataclass
from io import StringIO
from vosk import Model, KaldiRecognizer, SetLogLevel

@dataclass
class WavConfig:
    sample_rate: int

@dataclass
class Config:
    wav: WavConfig
    model: Path
    read_bytes: int

def fmt_title(s: str, underline = "=") -> str:
    return f"{s}\n{underline*len(s)}"

def main() -> None:
    config = Config(
        wav=WavConfig(sample_rate=16_000),
        model=Path("vosk-model-en-us-0.22-lgraph"),
        read_bytes=4_000,
    )

    if not config.model.exists():
        raise FileNotFoundError(f"Could not find model at '{config.model}'")
    
    model = Model(model_path=str(config.model))
    rec = KaldiRecognizer(model, config.wav.sample_rate)

    audio_file = Path(sys.argv[1])
    if not audio_file.exists():
        raise FileNotFoundError(f"Could not find audio at '{audio_file}'")
        
    # Command to format wav file as PCM Mono
    cmd_fmt_wav = [
        "ffmpeg", "-loglevel", "quiet", "-i", str(audio_file),
        "-ar", str(config.wav.sample_rate) , "-ac", "1", "-f", "s16le", "-"
    ]

    # Allocate buffer for transcribed audio
    transcription = StringIO()

    print()
    print(fmt_title("Initiating transcription"))
    with subprocess.Popen(cmd_fmt_wav, stdout=subprocess.PIPE) as process:
        data = bytes("init", encoding="utf-8")
        while len(data) > 0:
            data = process.stdout.read(config.read_bytes)
            if rec.AcceptWaveform(data):
                result: str = rec.Result()
                result: dict[str, str] = ast.literal_eval(result)
                transcription.write(result["text"])
                transcription.write("\n")
                print(f"[Log::Heard]: {result['text']}")

    print()
    print(fmt_title(f"Transcription for '{audio_file}'"))
    print(transcription.getvalue())



if __name__ == "__main__":
    SetLogLevel(0)
    try:
        main()
    except FileNotFoundError as err:
        print(err)




