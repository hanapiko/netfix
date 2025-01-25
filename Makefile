VENV_ACTIVATE = . myenv/bin/activate

start: migrate
	$(VENV_ACTIVATE) && python3 manage.py runserver

migrate:
	$(VENV_ACTIVATE) && python3 manage.py makemigrations
	$(VENV_ACTIVATE) && python3 manage.py migrate

admin:
	$(VENV_ACTIVATE) && python3 manage.py createsuperuser

create-app:
	$(VENV_ACTIVATE) && python3 manage.py startapp your_app_name

test:
	$(VENV_ACTIVATE) && python3 manage.py test

lint:
	$(VENV_ACTIVATE) && flake8 .

shell:
	$(VENV_ACTIVATE) && python3 manage.py shell

collectstatic:
	$(VENV_ACTIVATE) && python3 manage.py collectstatic

makemessages:
	$(VENV_ACTIVATE) && python3 manage.py makemessages -a

compilemessages:
	$(VENV_ACTIVATE) && python3 manage.py compilemessages

backup-db:
	$(VENV_ACTIVATE) && python3 manage.py dumpdata > backup.json

restore-db:
	$(VENV_ACTIVATE) && python3 manage.py flush
	$(VENV_ACTIVATE) && python3 manage.py loaddata backup.json

push:
	git stash
	git pull
	git stash apply
	git add .
	git commit -m "$(Message)"
	git push

.PHONY: start migrate admin create-app test lint shell collectstatic makemessages compilemessages backup-db restore-db push
