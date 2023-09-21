# ec_463_mp_aq
BU ECE Senior Design mini-project, Axel S. Toro Vega and Quentin Clark.

`firebase-app` is hosted on https://ec463miniproject-c8a9f.web.app

1. Deploy to firebase with `firebase deploy --only hosting`

- Tried using GitHub Actions to deploy to firebase but failing
- Google Sign In took a while to get working but works now with popup

# Backend

Backend is done in Python, frontend in HTML, connected with Flask.

-api/server.py has code that manages server instance and all client communications, 

-api/flask_deploy.py has all the flask front end connectivity.

-api/templates/ contains all the HTML page templates.
