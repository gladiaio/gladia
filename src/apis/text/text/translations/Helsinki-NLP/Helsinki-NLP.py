import os
import pickle
import time
from pathlib import Path
from typing import List

import redis
from unifai_api_utils.model_management import download_model
from unifai_api_utils.system import path_to_absolute
from icecream import ic
from transformers import MarianMTModel, MarianTokenizer
from fastapi import FastAPI, HTTPException


class Translator:
    def __init__(self, models_dir):
        self.models_dir = models_dir
        self.model_dir = path_to_absolute(f"{self.models_dir}/opus-mt-")
        self.model = None
        self.tokenizer = None

    def load_model(self, source, target):
        route = f"{source}-{target}"
        if not os.path.exists(self.model_dir):
            self.model_dir = self.download_translation_models(source, target)

        self.model = MarianMTModel.from_pretrained(self.model_dir)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_dir)


    def translate(self, source, target, src_text):
        route = f"{source}-{target}"

        self.model_dir += route

        self.load_model(source, target)

        translated = self.model.generate(
            **self.tokenizer(src_text, return_tensors="pt", padding=True)
        )

        words = [self.tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        
        return words


    def download_translation_models(self, source, target):
        output_path = download_model(
            f"https://huggingface.co/Helsinki-NLP/opus-mt-{source}-{target}",
            self.model_dir,
        )
        ic(output_path)
        return output_path


def predict(input_string, source_language, target_language):

    translator = Translator("models")
    try:
        translation = translator.translate(source_language, target_language, input_string)
        return translation[0]
    except:
        raise HTTPException(status_code=422, detail="language not found")
