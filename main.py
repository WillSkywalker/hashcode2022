import pandas as pd


def read_data(filename):
    with open(filename) as f:
        num_contributors, num_projects = f.readline().split()
        num_contributors = int(num_contributors)
        num_projects = int(num_projects)

        contributors_skills = {}
        skills_levels = {}
        projects = []

        for i in range(num_contributors):
            line = f.readline()
            name, num_skills = line.split()
            num_skills = int(num_skills)
            contributors[name] = {}

            for j in range(num_skills):
                line = f.readline()
                skill, level = line.split()
                level = int(level)
                contributors[name][skill] = level
                skills.setdefault(skill, {})
                skills[skill].setdefault(level, []).append(name)


        for i in range(num_projects):
            project_name, days, score, best_before, num_roles = f.readline().split()
            days, score, best_before, num_roles = int(days), int(score), int(best_before), int(num_roles)

            for j in range(num_roles):
                skill, required_level = f.readline().split()
                required_level = int(required_level)
                







if __name__ == '__main__':
    main()
