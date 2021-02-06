# Using django-sockpuppet with Django

Building a Django app which uses django-sockpuppet in place of a conventional react / angular / ember front end.

## Credits

To acclerate the process of getting project going I took some HTML/CSS from a Digital Ocean blog post [Build a To-Do application Using Django and React](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react) written by Jordan Irabor .

## Development Notes

### Pipenv/Virtualenv

This project makes use of pipenv so the virtualenv needs to be started in the pipenv way (`pipenv shell`) and there is no `requirements.txt`.


### Environmentally Aware Settings

Multiple settings files are defined to deal with different environments, they are all contained in `backend.settings` and need to be referenced when using the `manage.py` command. 


### Running backend locally 

Don't forget when running the dev server you have to enable access from outside the VM by modifying the default binding. It's also necessary to reference the relevant settings file.

Here's an example of doing that.

```
python manage.py runserver 0.0.0.0:8000 --settings=backend.settings.local
```

### Using Bootstrap

Bootstrap is used via the `django-bootstrap4` app (https://pypi.org/project/django-bootstrap4/).
