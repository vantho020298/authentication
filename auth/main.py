from flask import render_template, request, Response
from modules.utils import is_trusted
from modules.entities.ApiKey import ApiKey
from config import app, session
from modules.dbutils import add_or_update, delete as delete_records
import os

CRUD_TOKEN= os.getenv('CRUD_TOKEN')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate')
def auth():
    apiKeys = session.query(ApiKey)
    if is_trusted(request.headers, apiKeys):
        return Response(status=200)
    else: 
        return Response(status=400)

@app.route('/add', methods=['POST'])
def add():
    apiKey = ApiKey('crud_token', CRUD_TOKEN)
    if is_trusted(request.headers, [apiKey]):
        data = dict(request.form)
        add_or_update(data)
        return Response(status=200)
    else: 
        return Response(status=400)

@app.route('/delete', methods=['POST'])
def delete():
    apiKey = ApiKey('crud_token', CRUD_TOKEN)
    if is_trusted(request.headers, [apiKey]):
        data = dict(request.form)
        delete_records(data)
        return Response(status=200)
    else: 
        return Response(status=400)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.getenv('PORT'))