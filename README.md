# Data-Scientists-Toolkit-CS1660

Hello, welcome to my implementation of the data scientist's toolkit for CS 1660.

In order for this project to run some prerequisites will need to be met:
1. Run Windows XServer.
2. In the Dockerfile replace the COPY and WORKDIR with the location this project is saved to.
3. In docker-compose.yml replace the DISPLAY variable the web service with your own IP address.
   * Line 6.
4. In the command line: docker-compose build

Once this is completed the project can be run by:
1. In the command line: docker-compose up          
   *(sometimes the visual studio container does not work, it looks like something is leaving orphans that I cannot figure out, if so try docker-compose up --remove-orphans       instead)*
3. This should launch the data scientist's toolbox GUI.

Special Instructions:
1. For Spyder the password is randomly generated and can be found in cmd.
2. For Visual Studio the password is 123456.
3. For tensorflow the token is generated in cmd and needs to be pasted into the token/password section.

A walkthrough can be found at the following link:
https://youtu.be/kpXyqzV-xn8

Thank you for viewing!
