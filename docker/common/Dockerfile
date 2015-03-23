FROM ubuntu:trusty
MAINTAINER Simon Castillo <scastb@gmail.com>

# Setup application environment variables. Feel free to add any
# variable here that you might need across all your
# environments. Remember, do not secret API keys here.

# The application name for these images.
ENV APP_NAME jenkins-test

# Where in the docker container will the application be stored.
ENV APP_DIR /app


# Install some common headers and utilities to be available across all
# environments. If you need some others, just add them at the end.
RUN apt-get update && apt-get install -y -q libjpeg-dev \
                                            libjpeg8-dev \
                                            python-dev \
                                            postgresql-server-dev-9.3 \
                                            postgresql-client-9.3 \
                                            python \
                                            python-pip \
                                            python-setuptools \
                                            ruby \
                                            ruby1.9.1-dev \
                                            libxml2-dev \
                                            libxslt-dev \
                                            lib32z1-dev \
                                            software-properties-common \
    && add-apt-repository ppa:chris-lea/node.js -y \
    && apt-get update \
    && apt-get install -y -q nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



# You can install anything else you need now.  For example, you could
# install your application base requirements below.
ADD ./requirements $APP_DIR/requirements
RUN pip install -r $APP_DIR/requirements/base.txt
