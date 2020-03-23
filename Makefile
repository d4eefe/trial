
up:
	scp *.py Makefile stsievert@submit2.chtc.wisc.edu:~/chtc-getting-started/htmap-trial/

watch:
	# There's a possibly important counter, "total for all users".
	watch condor_q --submitter stsievert

build:
	docker image build -t adadamp:1.0 .

run:
	docker container run -p 8000:8000 --name ada adadamp:1.0

rm:
	docker container rm --force ada

debug:
	docker exec -it ada /bin/bash
