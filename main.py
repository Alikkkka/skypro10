from utils import get_candidates
from utils import format_candidates
from utils import get_candidate_by_id
from utils import get_candidates_by_skills

from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    candidates_list = get_candidates('candidates.json')

    return format_candidates(candidates_list)


@app.route('/candidates/<int:candidate_id>')
def print_candidate(candidate_id):
    candidates_list = get_candidates('candidates.json')
    candidate = get_candidate_by_id(candidates_list, candidate_id)
    result = f'<img src="{candidate["picture"]}">'

    return result + format_candidates([candidate])


@app.route('/skills/<string:skill>')
def skills(skill):
    candidates_list = get_candidates('candidates.json')

    return format_candidates(get_candidates_by_skills(candidates_list, skill))


app.run(port=5001)
