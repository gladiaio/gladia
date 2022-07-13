import os
import wave
from io import BytesIO
from pathlib import Path

import ffmpeg
import numpy as np
from gladia_api_utils.model_management import download_model
from icecream import ic
from stt import Model


class SpeechToTextEngine:
    def __init__(
        self,
        model_uri: str = "english/coqui/v1.0.0-huge-vocab",
        model: str = "model.tflite",
        scorer: str = "huge-vocabulary.scorer",
    ):

        language, author, version = model_uri.split("/")

        model_path_prefix = f"{os.getenv('MODEL_CACHE_ROOT')}/audio/text/{model_uri}"

        model_url = f"https://coqui.gateway.scarf.sh/{model_uri}"

        model_path = download_model(
            url=f"{model_url}/{model}", output_path=f"{model_path_prefix}/model"
        )

        scorer_path = download_model(
            url=f"{model_url}/{scorer}", output_path=f"{model_path_prefix}/scorer"
        )

        model_path = Path(model_path).absolute().as_posix()

        scorer_path = Path(scorer_path).absolute().as_posix()

        self.model = Model(model_path)
        self.model.enableExternalScorer(scorer_path)

    def normalize_audio(self, audio):
        out, err = (
            ffmpeg.input("pipe:0")
            .output(
                "pipe:1",
                f="WAV",
                acodec="pcm_s16le",
                ac=1,
                ar="16k",
                loglevel="error",
                hide_banner=None,
            )
            .run(input=audio, capture_stdout=True, capture_stderr=True)
        )
        if err:
            raise Exception(err)
        return out

    def run(self, audio):
        audio = self.normalize_audio(audio)
        audio = BytesIO(audio)
        with wave.Wave_read(audio) as wav:
            audio = np.frombuffer(wav.readframes(wav.getnframes()), np.int16)
        result = self.model.stt(audio)
        return result
