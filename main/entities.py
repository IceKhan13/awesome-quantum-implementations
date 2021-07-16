class RepoEntry:
    def __init__(self,
                 repo_link: str,
                 repo_author: str,
                 repo_description: str):
        """

        Args:
            repo_link:
            repo_author:
            repo_description:
        """
        self.link = repo_link
        self.author = repo_author
        self.description = repo_description

    def to_dict(self):
        """ Converts to json. """
        return {
            "link": self.link,
            "author": self.author,
            "description": self.description
        }

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "({} by {})".format(self.link, self.author)
