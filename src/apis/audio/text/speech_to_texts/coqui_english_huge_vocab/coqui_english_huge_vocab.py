from gladia_api_utils.CoquiEngineHelper import SpeechToTextEngine
from gladia_api_utils.io import _open

# Load app configs and initialize STT model
engine = SpeechToTextEngine(
    model_uri="english/coqui/v1.0.0-huge-vocab",
    model="model.tflite",
    scorer="huge-vocabulary.scorer",
)


def predict(audio: bytes, language: str = "en") -> str:

    audio = _open(audio)

    text = engine.run(audio)

    return text
