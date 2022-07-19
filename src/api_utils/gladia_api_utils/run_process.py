import importlib.util
import os
import sys

from PIL import Image

if __name__ == "__main__":

    module_path = sys.argv[0]
    model = sys.argv[1]
    kwargs = sys.argv[2]
    output_tmp_result = sys.argv[3]

    print(f"{module_path=}", file=sys.stderr)
    print(f"{model=}", file=sys.stderr)
    print(f"{kwargs=}", file=sys.stderr)
    print(f"{output_tmp_result=}", file=sys.stderr)

    PATH_TO_GLADIA_SRC = os.getenv("PATH_TO_GLADIA_SRC", "/app")

    os.environ[
        "LD_LIBRARY_PATH"
    ] = "/usr/local/nvidia/lib64:/usr/local/cuda/lib64:/opt/conda/lib"

    spec = importlib.util.spec_from_file_location(
        "{PATH_TO_GLADIA_SRC}/{module_path}",
        "{PATH_TO_GLADIA_SRC}/{module_path}/{model}.py",
    )
    this_module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(this_module)

    output = this_module.predict(**{kwargs})

    if isinstance(output, Image.Image):
        output.save("{output_tmp_result}", format="PNG")
    else:
        with open("{output_tmp_result}", "w") as f:
            f.write(str(output))
