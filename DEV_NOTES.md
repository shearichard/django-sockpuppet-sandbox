## 2021-02-07 00:27
Probably worth trying to download the demo and run it locally. https://github.com/zodman/django-sockpuppet-expo

## 2021-02-07 00:09
Managed to plug all the bits together so it's obviously *trying* to connect but not able to.

Things that need investigating:

    * When the browser is run outside of the hosting machine what sort of network access is required for the web-sockets stuff ?
    * Is it possible to specify what ports the w-s stuff uses ?
    * Does the logging need configuration change as per https://sockpuppet.argpar.se/troubleshooting#server-side

## 2021-02-06 23:02
Currently the todo list has it's content hard-coded. Clearly that needs changing if a demo is to show off insert/update/deletes.

## 2021-02-06 19:11
### Significant templates
#### Increment Example
./backend/todo/templates/todo_reflex.html
#### Todo Templates
./backend/backend/templates/todo/index.html
./backend/backend/templates/todo/base.html
