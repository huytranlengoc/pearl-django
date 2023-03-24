# Development tools
iext:
	cat tools/extensions.txt | xargs -I {} code --install-extension '{}'
eext:
	code --list-extensions >  tools/extensions.txt

# API
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

# APP
runui:
	cd frontend && npm run serve