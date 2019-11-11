from src.utils.graph_utils import GraphUtils
import unittest
import os


class GraphUtilsTests(unittest.TestCase):
    """
        Tests that the graph Utility can export a file
    """
    def test_graph_is_exported(self):
        if os.path.exists("./graph_test/A_B.png"):
            os.remove("./graph_test/A_B.png")
        if not os.path.exists("./graph_test"):
            os.mkdir("./graph_test")
        GraphUtils.export_graph({"A": [1, 2], "B": [2, 4]}, "A", "B", [2, 4], "./graph_test/")
        self.assertTrue(os.path.exists("./graph_test/A_B.png"))
        if os.path.exists("./graph_test/A_B.png"):
            os.remove("./graph_test/A_B.png")
        if os.path.exists("./graph_test"):
            os.rmdir("./graph_test")


if __name__ == '__main__':
    unittest.main()
