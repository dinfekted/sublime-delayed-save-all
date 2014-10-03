# ExplicitSaveAll

Save all files one by one with 0.3s interval between saving. It is handy when
you have handlers that watch file saving and they need a time to do stuff
between savings. It also can be used to reload sublime plugins dependencies
chains.


### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-explicit-save-all/master/demo/demo.gif "Demo")

### Installation

This plugin is part of sublime-enhanced plugin set. You can install
sublime-enhanced and this plugin will be installed automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov
/sublime-enhanced) package.


### Usage

Hit keyboard shortcut listed below to save files one by one.

### Commands

| Description         | Keyboard shortcuts | Command palette           |
|---------------------|--------------------|---------------------------|
| Save all one by one | ctrl+alt+shift+s   | ExplicitSaveAll: save all |