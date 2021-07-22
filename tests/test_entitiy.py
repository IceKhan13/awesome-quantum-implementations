import unittest
from main.entities import RepoEntry


class TestEntity(unittest.TestCase):
    """Tests entity."""

    def test_entry(self):
        """Tests entry."""
        entry = RepoEntry("a", "b", "c")
        self.assertEqual(entry.link, "a")
        self.assertEqual(entry.author, "b")
        self.assertEqual(entry.description, "c")

