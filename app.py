from flask import Flask
from views.index import index_bp
from views.about import about_bp

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(about_bp)
app.run(debug=True)



