migrations:
	backend/manage.py makemigrations

migrate:
	backend/manage.py migrate

runserver:
	backend/manage.py runserver

shell:
	backend/manage.py shell

preall:
	pre-commit run --all-files
