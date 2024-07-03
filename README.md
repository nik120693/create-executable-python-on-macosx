# Instructions:

Download the main dependency
```
pip3 install pyinstaller
```

Create the project directory
```
mkdir projectdir/ && cd projectdir/
```

Create the main script
```
touch main.py
```

Install all dependecies you need
```
pip3 install <MODULES>
```

Write your script inside the main
```
nano main.py
```

Create the setup file
```
touch setup.py
```

Edit the setup file
```
nano setup.py 
```

In options/packages add your dependencies modules
```
touch main.spec
```

Edit spec file and copy from my file and edit as you need, it is fitted to work on the entire filesystem
```
nano main.spec
```

Try the script
```
python3 main.py
```

If it works
```
pyinstaller --onefile --noconsole --windowed main.py
```

If successfully 
```
pyinstaller main.spec
```

Now in your dist directory you have the .app file that can run on macOS without using the terminal
