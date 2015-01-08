django-smh_redirections
==============

## Description
Django app to handle HTTP redirections. A registered user can redirect an URL under their domain (identified by an alias) in the form `http://<path to redirections>/<user>/<alias>` to the desired target URL. 



## Deploy
Clone the project under the name **smh_redirections**
```
$ git clone https://github.com/samuelmh/django-smh_redirections.git smh_redirections
```


### Dependencies
- smh_jwt - JSON Web Token authentication (https://github.com/samuelmh/django-smh_jwt).


## Functionality

### REST API
The main functionality is provided by a REST API. It enables an authenticated user (by a JWT) to perform the following actions:
* To create a redirection.
* To modify a redirection.
* To delete a redirection.
* To list all their redirections.

### HTML Web Application
The template `templates\main.html` provides an web application that works like a graphical interface to the REST API for the authenticated user. It also allows to sort by field the redirections list.

These are the dependencies for the webapp.
* JQuery.
* Bootstrap.
* AngularJS.

## Redirection view
When visiting (`METHOD:GET`) the redirection view `http://<path to redirections>/<user>/<alias>`, if public, the visiter will be redirected to the URL the owner set.

The owner of a redirection can alter the target URL through the API or by visiting the redirection view `http://<path to redirections>/<user>/<alias>` (`METHOD:POST`) and posting the configured password and the desired target. If not target is provided, the IP if the request will be taken as the target URL. This is useful to locate dynamic IP services. For example to locate a raspberry PI home server from a fixed URL.

## Documentation
There is also an extensive documentation page under `templates/help.html`.