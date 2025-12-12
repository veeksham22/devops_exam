FROM jenkins/jenkins:lts

USER root

# Install python3, pip and git
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
