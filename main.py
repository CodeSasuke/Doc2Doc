from collections.abc import Callable

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
