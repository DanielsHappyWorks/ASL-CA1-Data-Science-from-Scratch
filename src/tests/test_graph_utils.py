from src.utils.graph_utils import GraphUtils
import unittest
import os


class GraphUtilsTests(unittest.TestCase):
    """
        Tests that the graph Utility can export a linear regression graph file
    """
    def test_graph_is_exported(self):
        if os.path.exists("./graph_test/lr_A_B.png"):
            os.remove("./graph_test/lr_A_B.png")
        if not os.path.exists("./graph_test"):
            os.mkdir("./graph_test")
        GraphUtils.export_linear_regression_graph({"A": [1, 2], "B": [2, 4]}, "A", "B", [2, 4], "./graph_test/")
        self.assertTrue(os.path.exists("./graph_test/lr_A_B.png"))
        if os.path.exists("./graph_test/lr_A_B.png"):
            os.remove("./graph_test/lr_A_B.png")
        if os.path.exists("./graph_test"):
            os.rmdir("./graph_test")

    """
        Tests that the graph Utility can export a distribution graph file
    """
    def test_distribution_graph_is_exported(self):
        if os.path.exists("./graph_test/dist_A.png"):
            os.remove("./graph_test/dist_A.png")
        if not os.path.exists("./graph_test"):
            os.mkdir("./graph_test")
        GraphUtils.export_distribution_graph([1, 13, 45], "A", 10, 20, 5, "./graph_test/")
        self.assertTrue(os.path.exists("./graph_test/dist_A.png"))
        if os.path.exists("./graph_test/dist_A.png"):
            os.remove("./graph_test/dist_A.png")
        if os.path.exists("./graph_test"):
            os.rmdir("./graph_test")


if __name__ == '__main__':
    unittest.main()
