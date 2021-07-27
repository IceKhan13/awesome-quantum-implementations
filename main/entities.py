from typing import List


class RepoEntry:
    def __init__(self,
                 repo_link: str,
                 repo_author: str,
                 repo_description: str,
                 repo_tags: List[str]):
        """

        Args:
            repo_link:
            repo_author:
            repo_description:
            repo_tags:
        """
        self.link = repo_link
        self.author = repo_author
        self.description = repo_description
        self.tags = repo_tags

    def to_dict(self):
        """ Converts to json. """
        return {
            "link": self.link,
            "author": self.author,
            "description": self.description,
            "tags": self.tags
        }

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "({} by {})".format(self.link, self.author)
