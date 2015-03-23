FROM jenkins-test:common
MAINTAINER Simon Castillo <scastb@gmail.com>

# Setup application environment variables. Feel free to add any
# variable here that you might need for your local environment.

# The image environment
ENV APP_ENVIRONMENT local

# If you are using django-configurations you should make sure this is
# right.
ENV DJANGO_CONFIGURATION Local

# Install whatever is needed for your production environment.


# Install some common development utilities.
RUN apt-get update \
    && apt-get install -y -q software-properties-common \
                             command-not-found \
                             build-essential \
                             tig \
                             man \
                             atool \
                             wget \
                             curl \
                             htop \
                             aptitude \
                             psmisc \
                             nano \
                             vim \
                             git
                             subversion \
                             atfs \
    && apt-get install -y -q --no-install-recommends mercurial \
    && apt-get clean && /var/lib/apt/lists/* /tmp/* /var/tmp/*


# For example: you could install your app requirements with your
# package manager of choice.
ADD ./requirements $APP_DIR/requirements
RUN pip install -r $APP_DIR/requirements/$APP_ENVIRONMENT.txt
