import unittest
import mock


class ChooseVmTestCase(unittest.TestCase):
    def test_choice_vm(self):
        expected = "1"
        with mock.patch("pantera.chaos.connect") as conn:
            with mock.patch("random.choice") as choice:
                from pantera import chaos
                choice.return_value = expected
                vm = chaos.choice_vm()
        self.assertEqual(expected, vm)
