import pandas as pd


def read_data(filename):
    with open(filename) as f:
        num_contributors, num_projects = f.readline().split()
        num_contributors = int(num_contributors)
        num_projects = int(num_projects)

        contributors = {}
        projects = []

        for i in range(num_contributors, 2):
            line = f.readline()
            name, num_skills = line.split()
            num_skills = int(num_skills)

            contributors[name] = {}





if __name__ == '__main__':
    main()
