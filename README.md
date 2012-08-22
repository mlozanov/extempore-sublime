# Extempore-Sublime

A Sublime Text 2 plugin for
[Extempore](https://github.com/digego/extempore).  The plugin provides
syntax highlighting, as well as some commands and keybindings for
connecting to and working with a running Extempore process.

# Installation

To install the plugin, simply clone this repo into your
[ST2 packages directory](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-packages-directory).

Installation instructions for Extempore can be found at
[Extempore's github page](https://github.com/digego/extempore).

# Working with Extempore in ST2

The plugin provides three commands:

- `extempore_connect` (`ctrl-x, ctrl-j`) will connect to a running
  (local) Extempore process on the default port. You have to start
  this Extempore process yourself, generally in another terminal.

- `extempore_evaluate` (`ctrl-x, ctrl-x`) will send the highlighted
  region to the Extempore process. This is how you compile and run
  Extempore code.

- `extempore_disconnect` does what it says on the tin.

The keybindings are the same as the Extempore Emacs mode, but you can
change them to whatever you like.

# Known Issues

The syntax highlighting currently doesn't cover a few edge cases---so
if you end up tinkering with `Extempore.JSON-tmLanguage` to fix
anything then feel free to submit a patch.

Also, `extempore_evaluate` currently requires *highlighting* the code
to evaluate, it would be nice if it would eval the top-level
s-expression if no region was highlighted.  This will hopefully be
added soon.

# Licence
Copyright (c) 2012, Mikhail Lozanov, Ben Swift

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation 
   and/or other materials provided with the distribution.

Neither the name of the authors nor other contributors may be used to endorse
or promote products derived from this software without specific prior written 
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLEXTD. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.
