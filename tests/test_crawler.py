import pytest
from pathlib import Path
from crawler import crawl

def create_test_dir_structure(base_dir):
    # Create files and directories for testing
    (base_dir / "file1.txt").write_text("hello")
    (base_dir / "file2.txt").write_text("world")
    subdir = base_dir / "subdir"
    subdir.mkdir()
    (subdir / "file3.txt").write_text("foo")
    subsubdir = subdir / "subsubdir"
    subsubdir.mkdir()
    (subsubdir / "file4.txt").write_text("bar")
    return [
        str(base_dir / "file1.txt"),
        str(base_dir / "file2.txt"),
        str(subdir / "file3.txt"),
        str(subsubdir / "file4.txt"),
    ]

def test_crawl_max_depth(tmp_path):
    files = create_test_dir_structure(tmp_path)
    collected = []
    result = crawl(str(tmp_path), max_depth=1, action=lambda f: collected.append(f))
    expected = [str(tmp_path / "file1.txt"), str(tmp_path / "file2.txt")]
    assert set(result) == set(expected)
    assert set(collected) == set(expected)
    assert isinstance(result, list)

def test_crawl_full_depth(tmp_path):
    files = create_test_dir_structure(tmp_path)
    collected = []
    result = crawl(str(tmp_path), max_depth=10, action=lambda f: collected.append(f))
    assert set(result) == set(files)
    assert set(collected) == set(files)
    assert isinstance(result, list)

def test_crawl_os_walk(tmp_path):
    files = create_test_dir_structure(tmp_path)
    collected = []
    result = crawl(str(tmp_path), max_depth=1001, action=lambda f: collected.append(f))
    assert set(result) == set(files)
    assert set(collected) == set(files)
    assert isinstance(result, list)

def test_crawl_nonexistent_dir():
    with pytest.raises(FileNotFoundError):
        crawl("/nonexistent/path", max_depth=1, action=lambda f: None)

def test_crawl_not_a_directory(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("data")
    with pytest.raises(NotADirectoryError):
        crawl(str(file_path), max_depth=1, action=lambda f: None)

def test_crawl_return_type(tmp_path):
    (tmp_path / "file.txt").write_text("data")
    result = crawl(str(tmp_path), max_depth=1, action=lambda f: None)
    assert isinstance(result, list)