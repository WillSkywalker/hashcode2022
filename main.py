

def read_data(filename):
    with open(filename) as f:
        num_contributors, num_projects = f.readline().split()
        num_contributors = int(num_contributors)
        num_projects = int(num_projects)

        contributors_skills = {}  # get levels by name and skill
        skills_levels = {}  # get names by skill and level
        projects = {}

        for i in range(num_contributors):
            line = f.readline()
            name, num_skills = line.split()
            num_skills = int(num_skills)
            contributors_skills[name] = {}

            for j in range(num_skills):
                line = f.readline()
                skill, level = line.split()
                level = int(level)
                contributors_skills[name][skill] = level
                skills_levels.setdefault(skill, {})
                skills_levels[skill].setdefault(level, []).append(name)


        for i in range(num_projects):
            project_name, days, score, best_before, num_roles = f.readline().split()
            days, score, best_before, num_roles = int(days), int(score), int(best_before), int(num_roles)
            projects[project_name] = {}
            projects[project_name]['days'] = days
            projects[project_name]['score'] = score
            projects[project_name]['best_before'] = best_before
            projects[project_name]['num_roles'] = num_roles
            projects[project_name]['skills'] = {}

            for j in range(num_roles):
                skill, required_level = f.readline().split()
                required_level = int(required_level)
                projects[project_name]['skills'][skill] = required_level

    return contributors_skills, skills_levels, projects


def calculate(contributors_skills, skills_levels, projects):
    pass



def main():
    contributors_skills, skills_levels, projects = read_data('a_an_example.in.txt')






if __name__ == '__main__':
    main()
