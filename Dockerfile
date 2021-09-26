FROM python:3.9-slim-buster as base

# Configuration
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    APP_DIR=/code \
    USER_DIR=/home/user \
    PATH=/home/user/.poetry/bin:$PATH

RUN pip install --upgrade pip && \
    python -m pip install -q poetry

# Create dev user
RUN addgroup --system user --gid 1000 && \
    adduser --system user --ingroup user --uid 1000 && \
    mkdir -p $USER_DIR && chown user:user $USER_DIR && chmod 777 $USER_DIR

# # Create src dir
RUN mkdir -p $APP_DIR && \
    chown user:user $APP_DIR && \
    chmod 777 -R $APP_DIR
WORKDIR $APP_DIR

USER user

# install dependecies
COPY --chown=user:user pyproject.toml $APP_DIR
COPY --chown=user:user poetry.lock $APP_DIR
RUN poetry install

# install app
COPY --chown=user:user . $APP_DIR
RUN poetry install

CMD /code/cworker.sh

