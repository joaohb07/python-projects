import pytest
from scripts.dir_files.walk_dir import WalkDir
from mock import patch

class TestWalkDir(WalkDir):
    def __init__(self, path, exclude_dir):
        self.path = path
        self.exclude_dir = exclude_dir

test_data = [
     ("sample_path",[],['dump.txt']),
     ("",[],None),
]

@pytest.mark.parametrize("path,exclude_dir,expected", test_data)
def test_walk_dir_success(path,exclude_dir,expected):
     instance_ = TestWalkDir(path, exclude_dir)
     result_ = instance_.walk_dir()
     assert result_ == expected