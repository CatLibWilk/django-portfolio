# django-portfolio
Repo for Portfolio built with Django framework for Python


# Database Setup
The database for this application is Postgresql living on a DigitalOcean virtual server.  To follow this same configuration, launch a D.O. droplet, install and setup Postgres (I followed this tutorial https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04 ), and make sure that postgres is listening ( requires changes to pg_hba.conf and postgresql.conf files at /etc/postgresql/[postgresql version]/main.

Make sure that the settings.py file reflects your database and connection information.
