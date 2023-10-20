# resume-demo

how to deploy this project in vercel

## How to deploy
1. allow vercel to access your github account
go to setting.py and change allowed host

=['.vercel.app', 'localhost', ']

2. create vercel.json in root

mistake: I missed comma here :

{
    "builds" : [{
        "src": "resume_demo.python",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    }],
    "routes": [
        {

3. go to wsgi.py and change this line
app = application
