import sys
import os
print("collabs.wsgi 1")
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
print("collabs.wsgi 2")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
print("collabs.wsgi 3")
from collabs import app as application
