import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        toml_dict = tomli.loads(content)
        project_dict = toml_dict['tool']['poetry']
        name = project_dict['name']
        description = project_dict['description']
        license = project_dict['license']
        authors = project_dict['authors']
        dependencies = project_dict['dependencies']
        dev_dependencies = project_dict['group']['dev']['dependencies']
        dep_list = []
        dev_list = []
        for key in dependencies:
            dep_list.append(key)
        for key in dev_dependencies:
            dev_list.append(key)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dep_list, dev_list)
