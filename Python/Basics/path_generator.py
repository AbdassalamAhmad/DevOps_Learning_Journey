from pathlib import Path
path = Path()

# search for every file and dir in the current path.
for file in path.glob('*'):
    print (file)
