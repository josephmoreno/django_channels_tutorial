Followed this tutorial:
https://channels.readthedocs.io/en/stable/tutorial/part_1.html

Used hypercorn for deploying with ASGI:
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/

Purpose:
Needed some way to update the front-end of a user when the database is written to.
At first, I looked into websockets which eventually led to Django channels.