This is a sample python flask API that stores requests in a database.

Build:

	docker build  -t python-postgres-flask .

Run:
	docker run -p 5000:5000 python-postgres-flask

Test:
	curl localhost:5000/test
