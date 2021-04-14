# FLASK App to refresh data

from flask import Flask, request
from data_refresh import update_data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def refresh_data():
    update_data()
    return '''
            <html>
                <body>
                    <form method="post" action=".">
                        <p><input type="submit" value="Refresh Data" /></p>
                    </form>
                </body>
            </html>
            '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)