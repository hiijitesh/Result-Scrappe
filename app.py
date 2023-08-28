from utils.keep_alive_server import keep_alive
import logging
from flask import Flask, render_template
from src.reg_generator import generate_registration_numbers
from utils.mongo_utils import collection

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/")
def add_result():
    """
    college code available
    106-113
    121-136
    139-152

    """
    reg_year = list(range(18, 19, 1))
    branch_code = list(range(101, 105, 1))
    college_code = list(range(135, 137, 1))
    student_num = list(range(1, 61))
    result = generate_registration_numbers(
        reg_year, branch_code, college_code, student_num
    )
    return result


@app.route("/result")
def get_result():
    results = list(collection.find())
    return render_template("result.html", results=results)


if __name__ == "__main__":
    print("===Application Started===✅✅✅!")
    logging.basicConfig(
        # Change to desired log level (DEBUG, INFO, ERROR, etc.)
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(message)s",
        handlers=[
            logging.FileHandler("info.log"),  # Log to a file
            logging.StreamHandler(),  # Log to the console
        ],
    )
    app.run(debug=False)
    keep_alive()
    print("✳️Keep Alive is running!✳️")
