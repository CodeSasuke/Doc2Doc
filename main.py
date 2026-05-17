from collections.abc import Callable
import functools

def stylize_title(document):
    return add_border(center_title(document))


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)


def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents.append(new_doc)
    return documents

def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    
    return sorted(font_sizes)[(len(font_sizes)-1) // 2]
    
    
def format_line(line: str) -> str:
    stripped = line.strip()
    capitalized = stripped.upper()
    rm_punc = capitalized.replace(".", "")
    suffixed = f"{rm_punc}..."
    return suffixed

def choose_parser(file_extension: str) -> str:
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    # ?
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise Exception("not a hex color string")
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False

from collections.abc import Callable


def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str:
    file_to_string = to_string(file)
    wrapped = f"```\n{file_to_string}\n```"
    return wrapped




def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    map : dict[str,str] = {}
    for file_extension in file_extension_tuples: # ("document", [".doc", ".docx"])
        type_file = file_extension[0]
        extensions = file_extension[1]
        for extension in extensions:
            map[extension] = type_file
        
    return lambda input_file: map.get(input_file, "Unknown")

    
from collections.abc import Iterator
def change_bullet_style(document: str) -> str:
    lines_list = document.split("\n")

    lines_changed: Iterator[str] = map(convert_line,lines_list)
    rejoined_docs = '\n'.join(lines_changed)
    return rejoined_docs


# Don't edit below this line


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

def remove_invalid_lines(document: str) -> str:
    document_list = document.split('\n')
    
    filtered_copy:Iterator[str] = filter(lambda line : not line.startswith('-'),document_list )
    return '\n'.join(filtered_copy)




def join(doc_so_far: str, sentence: str) -> str:
    return doc_so_far + ". " +  sentence

def join_first_sentences(sentences: list[str], n: int) -> str:
    if n == 0:
        return ""
    joined: str = functools.reduce(join,sentences[:n])
    return f"{joined}."

valid_formats: list[str] = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]


# Don't edit above this line


def pair_document_with_format(
    doc_names: list[str], doc_formats: list[str]
) -> list[tuple[str, str]]:
    return list(filter(lambda document : document[1] in valid_formats, list(zip(doc_names,doc_formats))))

def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )