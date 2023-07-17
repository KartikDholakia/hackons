# Hackon - APIs for Website Hosting Hackathons
APIs built in this application allows users to :
- Create Hackathons
- List Hackathons
- Register to a Hackathon
- Make Submissions
- List the hackathons a user is registered in


## Setup on Local System

Clone the repository and move into the directory:

	git clone https://github.com/KartikDholakia/hackons
	cd hackons

Install the required dependecies:

	pip install requirements.txt

Make migrations to create tables in local SQLite file:

	python manage.py makemigrations
	python manage.py migrate

Now run the server:

	python manage.py runserver


## APIs

To create hackathon: (Only authenticated users can)

	POST /api/hackathons

To view list of hackathons:

	GET /api/hackathons

To create a Submission in a Hackathon:

	POST /api/hackathons/<str:id>/

where `id` is the ID of hackathon, in which we want to submit.

To register a user in a hackathon:

	POST /api/hackathons/<str:id>/register

where `id` is the ID of hackathon, in which we want to submit. Here user should be logged in.


To signup:

	POST /api/signup

To login:

	POST /api/login

To view hackathons in which user is registered:

	GET /api/user/