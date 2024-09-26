FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy all codes into the dir
COPY templates ./templates
COPY activity1-4.py ./
COPY boot.sh ./

# Define port
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd hello_user
USER hello_user

# add "--host", "0.0.0.0" to ensure it listens on all network interfaces
# run with docker run -p 5000:5000 hello_flask    
CMD ["flask", "--app", "activity1-4", "run", "--host", "0.0.0.0"]

# # Approach of using venv
# RUN python -m venv venv
# RUN venv/bin/pip install -r requirements/docker.txt
# ENTRYPOINT ["./deploy.sh"]