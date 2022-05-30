# React Securiser

React Securiser is a little tool that helps you to secure your React application in an MVC architecture.

---

## Install alias of the program

#### Windows

**Win + R** > `regedit.exe`
```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor
```

- Create new string value named `AutoRun`
- And in data value set `%USERPROFILE%/alias.cmd` or another path to a `.cmd` file
- Go to the path and create the file (`.cmd`)

In the `alias.cmd` file:
```cmd
DOSKEY rs=python "path\to\ReactSecuriser\main.py" "%cd%" $*
```

---

#### UNIX Systems

> Bash
```shell
vim ~/.bashrc
```

> oh-my-zsh
```shell
vim ~/.zshrc
```

In the `.bashrc` and `.zshrc` file:
```shell
alias rs=python3 "path\to\ReactSecuriser\main.py" pwd $*
```