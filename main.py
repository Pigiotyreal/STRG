import os
import sys

if len(sys.argv) < 2:
    print("Usage: python main.py <filename> [size]")
    sys.exit(1)
    
filename = sys.argv[1]
if not os.path.exists(filename):
    print("Error: File '%s' not found" % filename)
    sys.exit(2)
    
with open(filename) as f:
    fileSize = os.path.getsize(filename)
    if(len(sys.argv) == 2):
        print("File size (B): %d" % fileSize)
        print("File size (KB): %d" % (fileSize / 1024))
        print("File size (MB): %d" % (fileSize / 1024 / 1024))
        print("File size (GB): %d" % (fileSize / 1024 / 1024 / 1024))
        print("File size (TB): %d" % (fileSize / 1024 / 1024 / 1024 / 1024))
    else:
        sys.argv[2] = sys.argv[2].upper()
        if sys.argv[2] == "B":
            print("File size (B): %d" % fileSize)
        elif sys.argv[2] == "KB":
            print("File size (KB): %d" % (fileSize / 1024))
        elif sys.argv[2] == "MB":
            print("File size (MB): %d" % (fileSize / 1024 / 1024))
        elif sys.argv[2] == "GB":
            print("File size (GB): %d" % (fileSize / 1024 / 1024 / 1024))
        elif sys.argv[2] == "TB":
            print("File size (TB): %d" % (fileSize / 1024 / 1024 / 1024 / 1024))
        else:
            print("Error: Invalid size '%s'. Please use 'B', 'KB', 'MB', 'GB', or 'TB'" % sys.argv[2])
            sys.exit(3)