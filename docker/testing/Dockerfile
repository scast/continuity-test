FROM jenkins-test:common
MAINTAINER Simon Castillo <scastb@gmail.com>

# Setup application environment variables. Feel free to add any
# variable here that you might need for testing purposes.

# The image environment
ENV APP_ENVIRONMENT local

# If you are using django-configurations you should make sure this is
# right.
ENV DJANGO_CONFIGURATION Local

# Install whatever is needed for your production environment.

# For example: you could install your app requirements with your
# package manager of choice.
ADD ./requirements $APP_DIR/requirements
RUN pip install -r $APP_DIR/requirements/test.txt
