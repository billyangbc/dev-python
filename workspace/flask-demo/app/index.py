# Infrastructure test page.
import os
from flask import Flask
from markupsafe import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

SQLALCHEMY_WARN_20=1

app = Flask(__name__)

app.config.from_object('config.Config')

# Configure MySQL connection.
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev:dev@172.17.0.1/dev'
db = SQLAlchemy(app)

@app.route("/")
def test():
    mysql_result = False
    err = '';
    try:
        query = text('SELECT 1')
        #result = db.engine.execute(query)
        with db.engine.connect() as conn:
            result = conn.execute(query)
        if [row[0] for row in result][0] == 1:
            mysql_result = True
    except SQLAlchemyError as e:
        err = str(e)
    else:
        pass

    env_str = 's3_endpoint={0}'.format(os.environ['S3_ENDPOINT'])
    if mysql_result:
        result = Markup(f'<span style="color: green;">PASS</span><br><span>{env_str}</span>')
    else:
        result = Markup('<span style="color: red;">FAIL</span> [{}]'.format(err))

    # Return the page with the result.
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)