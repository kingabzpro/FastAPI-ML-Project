# FastAPI ML Project

In this project, we will learn how we can build an application programming interface (API) for your machine learning model and then deploy it with simple code. It took me one hour to learn FastAPI and five minutes to learn how to deploy it to Deta servers. We will also test our API on both local server and remote server using Python Request. Let's go a little bit deeper into the technologies that we are going to use in our project.

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy)

## spaCy
spaCy is more friendly towards application and deployment as compared to the famous NLTK Python library which is used for experimentation and evaluation. spaCy comes with prebuild statistical neural network NLP models with powerful features that are easy to use and implement in your project spaCy. We will be using quite a simple and small prebuilt English model to extract entities from our text.
## FastAPI
FastAPI is a fast web framework for building APIs with python, it comes with faster query time, easy and minimize code for you to design your first API within few minutes FastAPI. In our project we will be learning how FastAPI works and how can we use our prebuilt model to get entities from the English text.
## Deta
We will be using Deta Micros service for our API and Deploy our project without docker or YAML files. Deta platform comes with easy to deploy CLI, high scalability, secure API authentication keys, option to change subdomain, and logging  of the web traffic. These functions are completely free to use on Deta. In our project, we are going to use Deta CLI to deploy our Fast API with few lines of scripts.
 
 
