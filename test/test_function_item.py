from cursesmenu import CursesMenu

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

from cursesmenu.items import FunctionItem
from test_external_item import TestExternalItem


def fun1():
    return 10


def fun2(x):
    return x + 2


class TestFunctionItem(TestExternalItem):
    def setUp(self):
        super(TestFunctionItem, self).setUp()
        self.menu = CursesMenu("self.menu", "TestFunctionItem")

    def test_run(self):
        mock_function_1 = MagicMock(name="mock_function_1", return_value=5)
        mock_function_2 = MagicMock(name="mock_function_2", return_value=10)

        args = [1, 2, 3]
        kwargs = {"end": "\n", "sep": " "}
        function_item_1 = FunctionItem("function_item_1", self.menu, mock_function_1)
        function_item_2 = FunctionItem("function_item_2", self.menu, mock_function_2, args, kwargs)
        self.assertEqual(function_item_1.action(), 5)
        self.assertEqual(function_item_2.action(), 10)
        mock_function_1.assert_any_call()
        mock_function_2.assert_called_once_with(*args, **kwargs)

    def test_init(self):
        function_item_1 = FunctionItem("function_item_1", self.menu, fun1)
        function_item_2 = FunctionItem("function_item_2", self.menu, fun1, ["-l", "-a", "~"], {"test": 12}, True)
        function_item_3 = FunctionItem(name="function_item_3", menu=self.menu, function=fun2, args=[1, 2, 3],
                                       kwargs={1: "thing", 16: "other"}, should_exit=False)
        self.assertEqual(function_item_1.name, "function_item_1")
        self.assertEqual(function_item_2.name, "function_item_2")
        self.assertEqual(function_item_3.name, "function_item_3")
        self.assertEqual(function_item_1.menu, self.menu)
        self.assertEqual(function_item_2.menu, self.menu)
        self.assertEqual(function_item_3.menu, self.menu)
        self.assertFalse(function_item_1.should_exit)
        self.assertTrue(function_item_2.should_exit)
        self.assertFalse(function_item_3.should_exit)
        self.assertEqual(function_item_1.function, fun1)
        self.assertEqual(function_item_2.function, fun1)
        self.assertEqual(function_item_3.function, fun2)
        self.assertEqual(function_item_1.args, [])
        self.assertEqual(function_item_2.args, ["-l", "-a", "~"])
        self.assertEqual(function_item_3.args, [1, 2, 3])
        self.assertEqual(function_item_1.kwargs, {})
        self.assertEqual(function_item_2.kwargs, {"test": 12})
        self.assertEqual(function_item_3.kwargs, {1: "thing", 16: "other"})
