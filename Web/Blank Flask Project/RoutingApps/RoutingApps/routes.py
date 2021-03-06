#Import flask
from flask import Flask, url_for;
from app import app;

@app.route('/')
def hello():
    """Renders a sample page."""
    #thired Steps
    createLink="<a href='"+url_for("create")+"'>Create a Question</a>";
    return """<html> 
                   <head>
                        <title>
                           Hello World
                        </title>
                   </head>
                   <body>  
                     <h1>Hello World to here...</h1>
                     
                        """+createLink+"""
                   <body>        
             </html>"""
    

@app.route("/create")
def create():
    return """<html> 
                   <head>
                        <title>
                           Create Page
                        </title>
                   </head>
                   <body>
                        <h1>Write Your Create Form here...</h1>
                   <body>        
             </html>"""


#Second Steps
@app.route("/question/<title>")
def question(title):
    return """<h1> Here is the title - """+title+"""</h1>""";