import os

from gladia_api_utils.inference.triton_helper import download_active_triton_models


def main():
    os.environ["TRITON_MODELS_PATH"] = os.getenv("TRITON_MODELS_PATH", default="/tmp/gladia/triton")
    if not os.path.exists(os.environ["TRITON_MODELS_PATH"]):
        os.makedirs(os.environ["TRITON_MODELS_PATH"])

    if os.getenv("TRITON_LAZY_DOWNLOAD", 'True').lower() in ('false', '0', 'no'):
        download_active_triton_models(
            triton_models_dir=os.environ["TRITON_MODELS_PATH"],
            config_file_path="./config.json"
        )


if __name__ == "__main__":
    main()
