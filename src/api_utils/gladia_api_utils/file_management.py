import inspect
import os
import random
import string
import sys
from pathlib import Path
from uuid import uuid4
import io

import gdown
import magic
import requests
from icecream import ic
from xtract import XZ, BZip2, GZip, Rar, Tar, Zip, xtract
from xtract.utils import get_file_type
from google_drive_downloader import GoogleDriveDownloader as gdd

from PIL import Image
import tempfile


def write_tmp_file(content):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(content)
    tmp.close()
    
    return tmp.name


def remove_all_tmp_file(tmp_files):
    for tmp_file in tmp_files:
        os.unlink(tmp_file)


def input_to_files(func):
    def inner(*args, **kwargs):
        tmp_files = list()

        for keyword, arg in kwargs.items():
            if isinstance(arg, (bytes, bytearray)):
                tmp_file = write_tmp_file(arg)
                tmp_files.append(tmp_file)
                kwargs[keyword] = tmp_file
                
        result = func(*args, **kwargs)

        try:
            remove_all_tmp_file(tmp_files)
        except:
            print("Error while deleting temp files")
        
        return result

    return inner


def download_file(
    url: str, file_full_path: str, force_create_dir=True, force_redownload=False
) -> Path:

    is_gdrivefile = "https://drive.google.com/" in url

    file_full_path = Path(file_full_path)

    if not os.path.exists(file_full_path.parent):
        if force_create_dir:
            create_directory(file_full_path.parent)
        else:
            raise Exception(
                "Parent directory doesn't exists : change the path or use force_create_dir = True"
            )

    if not file_full_path.exists():

        if is_gdrivefile:
            gdown.download(url, file_full_path, quiet=False)
        else:
            write_url_content_to_file(file_full_path, url)

    elif file_full_path.exists() and force_redownload:
        if is_gdrivefile:
            gdown.download(url, file_full_path, quiet=False)
        else:
            write_url_content_to_file(file_full_path, url)

    return file_full_path


def write_url_content_to_file(file_full_path: Path, url) -> bool:
    data = requests.get(url).content
    print(f"writing {url} to {file_full_path}")
    return write_to_file(file_full_path, data)


def write_to_file(file_full_path, data) -> bool:
    if isinstance(file_full_path, str):
        file_full_path = Path(file_full_path)

    os.makedirs(os.path.dirname(file_full_path))

    if isinstance(data, io.BytesIO):
        with open(file_full_path, "wb") as handler:
            data = data.read()
        handler.write(data)
    elif isinstance(data, Image.Image):
        data.save(file_full_path)


def generate_random_filename(upload_directory, extension):
    filename = str(uuid4())
    filename = os.path.join(upload_directory, filename + "." + extension)
    return filename


def delete_file(filepath: str) -> bool:
    if os.path.exists(filepath):
        return os.remove(filepath)
    else:
        return False


def delete_all_files(files: list) -> list:
    out = dict()
    for file in files:
        out[file] = delete_file(file)
    return out


def create_directory(path: str) -> bool:
    if len(os.path.dirname(path)) > 0:
        return os.makedirs(os.path.dirname(path), exist_ok=True)
    else:
        return False


def uncompress(path: str, destination=None, delete_after_uncompress=True) -> str:
    try:
        ic("Extracting Archive", path, destination)
        output = xtract(path, destination=destination, overwrite=True, all=False)

        if delete_after_uncompress:
            ic("Deleting Archive", path)
            delete_file(path)

        ic("Extraction Done", output)
        return output
    except:
        raise (f"Error while uncompressing {path}")
        return False


def compress_directory(
    path: str, compression_format="gzip", destination=None, delete_after_compress=False
) -> str:
    """compression format accepted rar, tar, zip, bz2, gz, xz"""
    output = ""

    if destination:
        # used for relative paths
        namespace = sys._getframe(1).f_globals
        cwd = os.getcwd()
        rel_path = namespace["__file__"]
        root_path = os.path.dirname(os.path.join(cwd, rel_path))

        if not os.path.isabs(destination):
            destination = os.path.join(root_path, destination)

    if compression_format == "rar":
        output = Rar(path, destination=destination)

    if compression_format == "tar":
        output = Tar(path, destination=destination)

    if compression_format == "zip":
        output = Zip(path, destination=destination)

    if compression_format == "bz2":
        output = BZip2(path, destination=destination)

    if compression_format == "gz":
        output = GZip(path, destination=destination)

    if compression_format == "xz":
        output = XZ(path, destination=destination)

    return output


def is_archive(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "archive"


def is_image(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "image"


def is_audio(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "audio"


def is_video(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "video"


def is_structured_data(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "structured_data"


def is_word(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "word"


def is_pdf(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "pdf"


def is_web_content(file_path: str) -> bool:

    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_category(file_path)

    return file_mime_type == "web_content"


def get_buffer_category(buffer) -> str:
    return get_mime_category(get_buffer_type(buffer))


def get_file_category(file_path: str) -> str:

    output = ""
    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    file_mime_type = get_file_type(file_path)

    return get_mime_category(file_mime_type)


def get_mime_category(mime_type: str) -> str:
    if mime_type in [
        "audio/aac",
        "audio/midi",
        "audio/ogg",
        "audio/x-wav",
        "audio/webm",
        "audio/3gpp",
        "audio/3gpp2",
    ]:
        output = "audio"

    elif mime_type in ["application/octet-stream"]:
        output = "binary"

    elif mime_type in [
        "video/x-msvideo",
        "video/mpeg",
        "video/ogg",
        "video/webm",
        "video/3gpp",
        "video/3gpp2",
    ]:
        output = "video"

    elif mime_type in [
        "image/bmp",
        "image/gif",
        "image/x-icon",
        "image/jpeg",
        "image/png",
        "image/svg+xml",
        "image/tiff",
        "image/webp",
    ]:
        output = "image"

    elif mime_type in ["font/otf", "font/ttf", "font/woff", "font/woff2"]:
        output = "font"

    elif mime_type in ["application/vnd.amazon.ebook", "application/epub+zip"]:
        output = "ebook"

    elif mime_type in [
        "application/x-bzip",
        "application/x-bzip",
        "application/x-bzip2",
        "application/java-archive",
        "application/x-rar-compressed",
        "application/x-tar",
        "application/zip",
        "application/x-7z-compressed",
    ]:
        output = "archive"

    elif mime_type in [
        "application/x-csh",
        "application/ogg",
        "application/x-sh",
        "application/x-shockwave-flash",
    ]:
        output = "executable"

    elif mime_type in [
        "text/css",
        "text/html",
        "application/javascript",
        "application/xhtml+xml",
        "application/vnd.mozilla.xul+xml",
    ]:
        output = "web_content"

    elif mime_type in [
        "text/csv",
        "application/vnd.oasis.opendocument.spreadsheet",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ]:
        output = "flat_structured_data"

    elif mime_type in ["application/json", "application/xml"]:
        output = "multidimensional_structured_data"

    elif mime_type in [
        "application/msword",
        "application/x-abiword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.oasis.opendocument.text",
        "application/rtf",
    ]:
        output = "word"

    elif mime_type in [
        "application/vnd.ms-powerpoint",
        "application/vnd.oasis.opendocument.presentation",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ]:
        output = "presentation"

    elif mime_type in ["application/pdf"]:
        output = "pdf"

    elif mime_type in ["application/vnd.visio"]:
        output = "diagram"

    elif mime_type in ["text/plain"]:
        output = "text"

    else:
        output = "other"

    return output


def get_file_type(file_path: str) -> str:
    """return the file mime type with mime type
    see full list here : https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    """
    # used for relative paths
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    root_path = os.path.dirname(os.path.join(cwd, rel_path))

    if not os.path.isabs(file_path):
        file_path = os.path.join(root_path, file_path)

    return magic.from_file(str(file_path), mime=True)


def get_buffer_type(buffer) -> str:
    """return the buffer mime type with mime type
    see full list here : https://developer.mozilla.org/fr/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    """

    return magic.from_buffer(buffer, mime=True)


def random_string(lenght: int) -> str:
    letters = string.ascii_lowercase
    generated_random_string = "".join(random.choice(letters) for i in range(10))

    return generated_random_string


def create_random_directory(root_path: str) -> str:
    full_path = os.path.join(root_path, random_string(10))
    create_directory(full_path)

    return full_path


def generate_random_filename(root_path: str, extension: str) -> str:
    filename = ".".join([random_string(10), extension])
    full_path = os.path.join(root_path, filename)

    return full_path, filename
