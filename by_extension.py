exts = [
    "py", "rb", "c", "cpp", "cc", "h", "hpp", "pl",
    "java", "js", "json", "html", "css", "md", "cs",
    "php", "rs", "sh", "bash", "ts", "coffee",
    "lisp", "lua", "nginx", "ps", "powershell", "vim", "sql", "scss",
    "r", "cmake", "makefile", "mk"
]


def should_use_ext(name, body):
    if len(name.split(".")) == 2:
        ext = name.split(".")[1]
        if ext in exts and name.endswith(f".{ext}"):
            return True
