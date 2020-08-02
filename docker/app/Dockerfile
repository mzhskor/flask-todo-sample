FROM python:3.8.5

# non-root user
ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP todo
ENV FLASK_ENV development
CMD ["flask", "run", "--host=0.0.0.0"]
