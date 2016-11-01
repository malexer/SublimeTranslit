SublimeTranslit
===============

SublimeTranslit is a plugin for Sublime Text 3
(http://www.sublimetext.com/3) for transliterating selected text.

Intented to be used via Command Palette.


Install
=======

Install using Package Control: `Translit`


Usage
=====

Open Command Palette and type "translit" to see several options.


Creating Transliteration Dictionaries
=====================================

SublimeTranslit supports extending it with additional dictionaries.

Every Dictionary is described by two files:

1. `dictionary_name.json` - is used to define characters mapping.
2. `dictionary_name.sublime-commands` - is used to add a command for this
dictionary to Command Palette.


dictionary_name.dict
--------------------

Contains mapping (dictionary "chars_mapping") of characters.

All other fields (name, description, link) is optional and specified in order
to explain used translit rules and point to source documents.


dictionary_name.sublime-commands
--------------------------------

It is a ordinary .sublime-commands file for Command Palette item for this
dictionary.

Should run command `transliterate_selection` with parameter
`dictionary_file` - a file name of **dictionary_name.json** (without path).

Example:

    [
        {
            "caption": "<command name>",
            "command": "transliterate_selection", "args":
            {
                "dictionary_file": "dictionary_name.json".
                "invert_mapping": false
            }
        }
    ]

`invert_mapping` field will trigger inverting of mapping from JSON file which
is useful to use one mapping file to define two transliterations (both sides).


Run unittests
=============

Use nose:

    $ nosetests test
