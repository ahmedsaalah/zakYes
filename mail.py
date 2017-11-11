from flask import Flask

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


from flask import session as login_session


import requests
import platform
import json
import httpagentparser
app =Flask(__name__)

''' Views  '''
@app.route('/')
def HomePage():
        
    return render_template('items.html' )


''' Views  '''
@app.route('/details')
def Details():
        
    return render_template('details.html' )


@app.route('/player')
def Player():
        
    return render_template('player.html' )



@app.route('/yes.html')
def Genre():
    

    
    
    return render_template('genre.html' )



if __name__ == '__main__':
   app.run(debug = True)