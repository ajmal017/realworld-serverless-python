# ![RealWorld Example App](logo.png)

> ### Serverless Python(AWS Lambda) codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.


### [Demo](https://github.com/gothinkster/realworld)&nbsp;&nbsp;&nbsp;&nbsp;[RealWorld](https://github.com/gothinkster/realworld)


This codebase was created to demonstrate a fully fledged fullstack application built with **Serverless Python** including CRUD operations, authentication, routing, pagination, and more.

We've gone to great lengths to adhere to the **Serverless Python** community styleguides & best practices.

For more information on how to this works with other frontends/backends, head over to the [RealWorld](https://github.com/gothinkster/realworld) repo.


# How it works

> Describe the general architecture of your app here

(TODO draw AWS Lambda architecture and paste)

# Getting started

## Installing dependencies

Create and activate virtual environment.
Since this implemetation uses AWS Lambda python 3.6 runtime, it is recommended to use python 3.6
```
$ pip3 install virtualenv
$ python -m venv venv
$ source venv/bin/activate
```

Install python dependencies via `pip`, referencing `requirements.txt`
```
(venv) $ pip install -r requirements.txt
```

Head up to `package.json` and install node dependencies via `npm` or `yarn`. Globally installing `npx` is also recommended

**via npm**
```
$ npm install
$ npm install -g npx
```

**via yarn**
```
$ yarn
$ yarn global add npx
```

## Invoke functions locally

To trigger http events in local machine, use this command.
```
$ npx serverless invoke -f <FUNC_NAME>
```

You can find function names in `serverless.yml`, including list of events are responsible for, and urls.

To Test functions in local environment, you can use,
```
$ npx serverless invoke local -f <FUNC_NAME>
```

## Deployment

You can deploy serverless functions via:
```
$ npx serverless deploy
```

This will zip up all python dependencies and code into .zip file, and,

- upload artifacts in `s3`
- create `CloudFormation` stack
- upload lambda function and add to stack
- Trigger `api gateway` event and add to stack

You can also specify which stage to deploy. Stage will probably be either `dev` or `prod`. Default is `dev`