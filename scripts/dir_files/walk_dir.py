import os

class WalkDir():
    
    def __init__(self):
        self.path = input("Type your path:\n")
        self.exclude_dir = [input("Type dir(s) to exclude (e.g. folder1,folder2...) or else <enter>:\n")]
            
    def walk_dir(self):
        if os.path.isdir(self.path):
            for current_dir, dirs, filenames in os.walk(top=self.path, topdown=True):
                dirs[:] = [d for d in dirs if d not in self.exclude_dir]
                for file in filenames:
                    print(f'Files paths: {current_dir}/{file}\n')
            print(f'Files: {filenames}\n')
            return filenames
                    
        else:
            print(f'Invalid path: {self.path}\n')
            return  None
    
    
    
        