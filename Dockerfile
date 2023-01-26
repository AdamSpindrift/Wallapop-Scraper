#Deriving the latest base image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

#Labels as key value pair
LABEL Maintainer="www.adampower.io"

# Install Python
RUN apt-get update -y
RUN apt-get install -y python3

# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /user/app/src

#to COPY the remote file at working directory in container
COPY . .
# Now the structure looks like this '/user/app/src/wallapop_schedule.py'

# Install Chrome
RUN ["./installers/ChromeSetup.exe", "/silent", "/install"]

# install packages
RUN pip install --no-cache-dir -r requirements.txt --user

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./wallapop_schedule.py"]