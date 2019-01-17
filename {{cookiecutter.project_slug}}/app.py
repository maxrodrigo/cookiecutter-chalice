{% if cookiecutter.use_boto3 == 'y' -%}
import boto3
{%- endif %}
from chalice import Chalice

app = Chalice(app_name="{{ cookiecutter.project_slug }}")


@app.route("/")
def index():
    return {"hello": "word"}
