## 2021-02-07 18:34
Went ahead and downloaded the demo and ran it locally. https://github.com/zodman/django-sockpuppet-expo .

At first it looked like it hadn't worked, or rather the page rendered OK but initial clicking on the 'increment' didn't do anything. However I then tried it after a wait of perhaps 20 seconds and it did work.

This was true using FF either directly on the dev vm or when setting up a tunnel to the vm from the host machine and using FF on the host machine.

### NEXT
    * Need to analyse the debug messages on the network tab and compare with those issued by this app.
    * Install Chrome on the VM and then try using Chrome on the VM and the host machine (this may help with analysing the messages).
    * Try to understand what the sigificance of the 'yarn run' in the demo - there is not corresponding suggestion in the 'quick start'


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
