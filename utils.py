import json


def get_candidates(path):
    with open(path, 'r', encoding="UTF-8") as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    string = '<pre>'
    for candidate in candidates_list:
        string += (
          f'Имя кандидата - {candidate["name"]}\n'
          f'Позиция кандидата - {candidate["position"]}\n'
          f'Навыки кандидата - {candidate["skills"]}\n''\n'
        )
        print()
    string += '<pre>'

    return string


def get_candidate_by_id(candidates_list, candidate_id):
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_skills(candidates_list, candidate_skill):
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result
