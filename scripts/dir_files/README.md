# Return directory files

>A simple script developed using python and the `os` library.

## Documentation

Check my oficial [**documentation**](https://joaohb07.github.io/documentation/python/walk_dir/walk_dir/) for more information on my python projects!

## Installation

This script is developed in ***[python3.7 >](https://www.python.org/downloads/)***, make sure you have this installed before run it.

Clone `main` branch from my ***[repo](https://github.com/joaobotelho072002/joaobotelho072002.github.io)***.

## Usage

Access `dir_files` folder:

```bash
cd dir_files
```

How to run the script:

```bash
python3 run.py
```

## Code

```python title="Main Script"
class WalkDir():
    
    def __init__(self):
        self.path = input("Type your path:\n")
        self.exclude_dir = [input("Type dir(s) to exclude (e.g. folder1,folder2...) or else <enter>:\n")]
            
    def walk_dir(self):
        if self.path:
            for _, dirs, filenames in os.walk(top=self.path, topdown=True):
                dirs[:] = [d for d in dirs if d not in self.exclude_dir]
                print(f'Files: {filenames}\n')
                    
        else:
            print(f'Invalid path: {self.path}\n')
```

> The script above simply inputs: a path from the user and dir(s) to exclude, then it prints the file(s) name(s),
> ***[repo](#installation)***.

```bash title="Sample output"
Type your path:
/Users/joaobotelho/Desktop/snake
Type dir(s) to exclude (e.g. folder1,folder2...) or else <enter>:
snake
Files: ['.DS_Store', 'requirements.txt', 'snake.py', 'README.md', '.gitignore']
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
