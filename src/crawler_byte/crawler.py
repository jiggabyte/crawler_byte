from collections.abc import Callable
from pathlib import Path
import os

def crawl(directory: str, max_depth: int, action: Callable[[str], None]) -> list[str]:
    # check if directory exists / is a directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path {directory} is not a directory.")
    
    # Initialize the crawler
    results = []
    root = Path(directory)

    if max_depth < 1000:
        def _crawl(current_path: Path, current_depth: int):
            if current_depth > max_depth:
                return
            if current_path.is_dir():
                for item in current_path.iterdir():
                    _crawl(item, current_depth + 1)
            else:
                action(str(current_path))
                results.append(str(current_path))

        _crawl(root, 0)
    else:
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                action(file_path)
                results.append(file_path)
    return results