# BeSGPT
### About BeSGPT
A generative AI based tool to help Open Source Security Specialists to perform pentest.

It helps Security Specialists in pentesting the System and Web Applications.   
It is aimed to provide the step by step guide to security analyst while performing the pentest on a system or web application.

BeSGPT is a chat based application and provides a interactive interface for the security analyst to communicate with the Genrative AI Model.

BeSGPT is expected to avoid costly api usage for the generation of steps and utilize open source models and frameworks as much as possible.

### Requirements
BeSGPT is designed on python and GPT4ALL. GPT4ALL is a open-sorce chatbot ecosystem and plugins to support the locally running general purpose systems.

> Python
> Linux

### Components of BeSGPT
##### Init Module
This module is responsible for the initialization of the application and setup the interactive prompt.

##### Parsing Module
It reads the user input and commands and feed them to the underlying model for understanding the pentest requirements.

##### Reasoning Module
Reasoning module is suppose to analyze the pentester input and the output of previous commands from the system under test or content from web application.

##### Generative Module
Generates the next commands or steps to be perfromed by the petester.

### Usage procedure
1. Pentest analyst clone BeSGPT project to local system. `https://github.com/Be-Secure/BeSGPT.git`
2. Analyst install the BeSGPT and required libararies and models using `cd BeSGPT; pip3 install -e`
3. Start the BeSGPT session  using `BeSGpt start`.
  It will start the bash prompt to the user with the available options.
4. Analyst chooses the option to perform and enter to the prompt.
5. BeSGPT takes the input and generates the steps to be performed by the analyst on system or web application.
6. Security Analyst takes up the steps and perform them on the targeted system or applications.
7. Security analyst capture the results from the steps or commands executed on targeted system or application.
8. Security analyst feeds the results into the BeSGPT and ask to continue.
9. BeSGPT analyze the results produced by system or application content and suggeste next steps to be performed.
10. On completion of pentest session for the system or application, security analyst breaks the connection to BeSGPT.
11. Intitiate the new session for next application or application assessment.
12. Publish the results of pentesting.

 
