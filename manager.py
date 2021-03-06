import fire
import re
import json
from typing import List, Tuple
from jinja2 import Environment, PackageLoader, select_autoescape
from main.entities import RepoEntry

env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)


class Manager:
    def __init__(self):
        self.repos_path = "./resources/repos.json"
        self.template_path = "main/templates/readme.md"
        self.entries = Manager.json_load(self.repos_path)

    @classmethod
    def json_load(cls, path: str) -> List[RepoEntry]:
        """ loads entries from file.

        Args:
            path: path to json file with entries
        """
        with open(path, "r") as f:
            data = json.load(f)
            return [RepoEntry(repo_link=e.get("link"),
                              repo_author=e.get("author"),
                              repo_description=e.get("description"),
                              repo_tags=e.get("tags", [])) for e in data]

    def _save(self):
        """ Saves entries to file. """
        with open(self.repos_path, "w") as f:
            json.dump([e.to_dict() for e in self.entries], f, indent=2)

    def add_repo(self,
                 repo_link: str,
                 repo_author: str,
                 repo_description: str,
                 repo_tags: Tuple[str]):
        """ Adds repo to list of entries.

        Args:
            repo_link:
            repo_author:
            repo_description:
            repo_tags: comma separated tags

        Returns:

        """
        self.entries += [RepoEntry(repo_link=repo_link,
                                   repo_author=repo_author,
                                   repo_description=repo_description,
                                   repo_tags=list(repo_tags))]
        self._save()

    def generate_readme(self):
        """ Generates readme with list of repos. """
        template = env.get_template("readme.md")
        print(self.entries)
        with open("./README.md", "w") as f:
            f.write(template.render(repos=self.entries))

    def parse_issue_body(self, body: str):
        """ Parse issue body. """
        github_pattern = r"https://github.com/([\w\-\_]+)/([\w\-\_]+)"
        github_info_res = re.findall(github_pattern, body)

        description = ""
        tags = ""
        try:
            description = body.split("### Description")[1].split("### Tags")[0].strip()
            tags = body.split("### Description")[1].split("### Tags")[1].strip()
        except Exception as e:
            print(e)

        if len(github_info_res) > 0:
            account, repo = github_info_res[0]
            print('::set-output name=SUBMISSION_REPO::https://github.com/{}/{}'.format(account, repo))
            print('::set-output name=SUBMISSION_NAME::{}'.format(repo))
            print('::set-output name=SUBMISSION_DESCRIPTION::{}'.format(description))
            print('::set-output name=SUBMISSION_TAGS::{}'.format(tags))


if __name__ == '__main__':
    fire.Fire(Manager)
