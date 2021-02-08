## 2021-02-07 23:18
Now getting tracebacks from within Django when trying to use either the 'increment' or the 'EditX' link/button.

Probably good to compare the demo code with the sandbox code in the light of the traceback messages.

## 2021-02-07 22:15
OK probably the last "npm i -d ..." was done in the wrong directory so I've renamed the resulting package-lock.json and am about to do it again in the right directory and using yarn.

(django-sockpuppet-sandbox) rshea@mayari:~/src/django-sockpuppet-sandbox$ yarn add --dev fs path sockpuppet-js stimulus stimulus_reflex webpack webpack-cli

## 2021-02-07 22:01

As per instructions https://sockpuppet.argpar.se/setup-django#javascript-configuration executed the following. Not sure what to make of the comments about Ruby gem ?

```
(django-sockpuppet-sandbox) rshea@mayari:~/src/django-sockpuppet-sandbox$ npm i -D fs path sockpuppet-js stimulus stimulus_reflex webpack webpack-cli

> stimulus_reflex@3.4.1 postinstall /home/rshea/src/django-sockpuppet-sandbox/node_modules/stimulus_reflex
> node ./javascript/scripts/post_install.js

Friendly reminder: When updating the stimulus_reflex package,
don't forget to update your Ruby gem as well.

See https://rubygems.org/gems/stimulus_reflex
npm WARN saveError ENOENT: no such file or directory, open '/home/rshea/src/django-sockpuppet-sandbox/package.json'
npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN enoent ENOENT: no such file or directory, open '/home/rshea/src/django-sockpuppet-sandbox/package.json'
npm WARN django-sockpuppet-sandbox No description
npm WARN django-sockpuppet-sandbox No repository field.
npm WARN django-sockpuppet-sandbox No README data
npm WARN django-sockpuppet-sandbox No license field.

+ stimulus@2.0.0
+ stimulus_reflex@3.4.1
+ webpack@5.21.1
+ path@0.12.7
+ sockpuppet-js@0.5.0
+ fs@0.0.1-security
+ webpack-cli@4.5.0
added 140 packages from 172 contributors and audited 140 packages in 43.768s

14 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

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
