import os

from flask import Flask, jsonify, render_template, request

def create_app(test_config=None):
    app = Flask(__name__)
    
    from . import nbody_module

    @app.route('/nbody', methods=('POST',))
    def nbody():
        # print('AJAX request received')
        return jsonify({
            'params': nbody_module.update_nbody(request.form)
        })

    @app.route('/', methods=('GET',))
    def index():
        return render_template('base.html')
    
    return app