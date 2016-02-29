import os


PROJECT_NAME = "ShamsGolapWebsite"
HOMEPAGE = "http://shams-golap.fr"


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project: ' + directory + '"')
        os.makedirs(directory)
    else:
        print('Project "' + directory + '" already exists')
        print('Stop processing. Remove old project and retry')


def create_data_files(project_name, base_url):
    crawled = project_name + '/crawled.txt'
    queue = project_name + '/queue.txt'

    write_file(crawled, base_url)
    write_file(queue, '')


def write_file(path, content):
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write(content)

create_project_dir(PROJECT_NAME)
create_data_files(PROJECT_NAME, HOMEPAGE)
