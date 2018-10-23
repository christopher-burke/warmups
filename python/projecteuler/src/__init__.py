import sys
import os

file_path = os.path.abspath(__file__)
warmups_dir = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
sys.path.insert(0, warmups_dir)


print(sys.path)
