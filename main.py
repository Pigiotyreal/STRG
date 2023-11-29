import os
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)
    
filename = sys.argv[1]
if not os.path.exists(filename):
    print("Error: File '%s' not found" % filename)
    sys.exit(2)
    
with open(filename) as f:
    fileSize = os.path.getsize(filename)
    print("File size (B): %d" % fileSize)
    print("File size (KB): %d" % (fileSize / 1024))
    print("File size (MB): %d" % (fileSize / 1024 / 1024))
    print("File size (GB): %d" % (fileSize / 1024 / 1024 / 1024))
    print("File size (TB): %d" % (fileSize / 1024 / 1024 / 1024 / 1024))