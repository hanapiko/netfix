start: migrate sample-services
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

sample-services:
	python3 manage.py create_sample_services

sample-services-clear:
	python3 manage.py create_sample_services --clear

create-app:
	python3 manage.py startapp your_app_name

test:
	python3 manage.py test

lint:
	flake8 .

shell:
	python3 manage.py shell

collectstatic:
	python3 manage.py collectstatic

makemessages:
	python3 manage.py makemessages -a

compilemessages:
	python3 manage.py compilemessages

backup-db:
	python3 manage.py dumpdata > backup.json

restore-db:
	python3 manage.py flush
	python3 manage.py loaddata backup.json

push:
	git stash
	git pull
	git stash apply
	git add .
	git commit -m "$(Message)"
	git push

.PHONY: start migrate admin sample-services sample-services-clear create-app test lint shell collectstatic makemessages compilemessages backup-db restore-db push
