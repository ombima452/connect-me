# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.
# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; test "\!:*" != "nondestructive" && unalias deactivate'

# Unset irrelevant variables.
deactivate nondestructive

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
setenv VIRTUAL_ENV "/home/moringa/Desktop/connect-me/virtual"
=======
setenv VIRTUAL_ENV "/home/moringa/Documents/connect-me/virtual"
>>>>>>> 0eeee351cf8b4f340da053fd9bfd04f40ca0b8ca
=======
setenv VIRTUAL_ENV "/home/moringa/Documents/Group-projects/connect-me/virtual"
>>>>>>> 7e1b6fe4ec36291492d35461788878d6cdef5840
=======
setenv VIRTUAL_ENV "/home/moringa/Documents/GroupProjects/connect-me/virtual"
=======
setenv VIRTUAL_ENV "/home/moringa/Documents/connect-me/virtual"
>>>>>>> Dev
>>>>>>> b7cf39af251eb5530313b3a00fd81b0d5ee0d12b

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"


set _OLD_VIRTUAL_PROMPT="$prompt"

if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
    if ("virtual" != "") then
        set env_name = "virtual"
    else
        if (`basename "VIRTUAL_ENV"` == "__") then
            # special case for Aspen magic directories
            # see http://www.zetadev.com/software/aspen/
            set env_name = `basename \`dirname "$VIRTUAL_ENV"\``
        else
            set env_name = `basename "$VIRTUAL_ENV"`
        endif
    endif
    set prompt = "[$env_name] $prompt"
    unset env_name
endif

alias pydoc python -m pydoc

rehash
