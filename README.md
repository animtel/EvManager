# EvManager

## Description:

EvManager - is a bot that allows you to find free time in your schedule and notify colleagues as quickly as possible using a convenient messenger.

## Goals:

1. Create Slack bot that could receive commands (“my free time slots”, “send email to [Name]” )
2. Connect Bot to RASA Platform where you could resolve entered text and convert it into right action
3. All dialogs you should store in database for future use
4. Create cron job that go over your dialog and do data mining. For example, extract improtant fact such
as key, value pairs [Name, Email]
5. Connect Slack bot to your callender and on command “my free time slots” get free time slots from
calendar
   
# How to run:

Note: All next commands you should run from `root` of project.

## 1) Run ngrok
Note: not necessary if you have an open endpoint that can be configured for receiving webhooks.
- To create HTTP traffic tunnel to perform websocket connection

### Windows:
- `ngrok\ngrok.exe http 5005`
- copy address. You will see smth like this: forwarding https://<some_id>.ngrok.io

### Linux:
- TODO: add instructions for linux. Better is wrap ngrok to docker.

## 2) Run rasa listener, actions:
- add bot configuration to credentials.yml (in my case, I've used telegram bot and was needed only its token, id and webhook server url which we were generated in 1 part)
- `docker-compose up -d` will start rasa actions server and listener