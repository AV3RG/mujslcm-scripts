import inquirer
from inquirer.questions import Question
from inquirer.themes import GreenPassion


def prompt(question: Question):
    return inquirer.prompt([question], theme=GreenPassion())