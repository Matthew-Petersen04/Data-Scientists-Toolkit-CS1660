FROM ubuntu:20.04
RUN apt update && apt install -y python3
RUN apt update && apt install -y python3-tk
RUN apt update && apt install -y firefox
COPY . /Users/mtp11/docker-assignments/CourseProject/
WORKDIR /Users/mtp11/docker-assignments/CourseProject/
CMD ["python3", "app.py"]