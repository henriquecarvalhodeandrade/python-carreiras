""" 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carreiras')
def carreiras():
    careers = [
        {"title": "Desenvolvedor Python", "description": "Desenvolva aplicações web e sistemas com Python"},
        {"title": "Cientista de Dados", "description": "Analise dados e crie modelos de machine learning"},
        {"title": "Engenheiro de Backend", "description": "Construa APIs e sistemas escaláveis"},
        {"title": "DevOps Engineer", "description": "Automatize infraestrutura e deployments"},
    ]
    return render_template('carreiras.html', careers=careers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""
