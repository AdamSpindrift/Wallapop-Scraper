#Deriving the latest base image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

#Labels as key value pair
LABEL Maintainer="adampower.io"

# Install Chrome
RUN ["./installers/ChromeSetup.exe", "/silent", "/install"]

# Install Python
RUN apt-get update -y
RUN apt-get install -y python3

# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /user/app/src

#to COPY the remote file at working directory in container
COPY . .
# Now the structure looks like this '/user/app/src/wallapop_schedule.py'

# install packages
RUN pip install --no-cache-dir -r requirements.txt --user

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./wallapop_schedule.py"]