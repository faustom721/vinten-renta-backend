MANAGE = python manage.py
PROJECT_VERSION = 1.0.0

# Builds the project using 'development' settings.
dev:
	pip install -r requirements.txt;
	$(MANAGE) migrate;

run:
	$(MANAGE) runserver;