$env:FLASK_APP = "server.py"
$env:FLASK_ENV = "development"
$env:PYTHONHASHSEED = "4359283"
python -m flask run