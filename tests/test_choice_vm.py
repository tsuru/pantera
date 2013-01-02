import unittest
import mock


class ChooseVmTestCase(unittest.TestCase):
    def test_choice_vm(self):
        expected = "1"
        with mock.patch("pantera.caos.connect") as conn:
            with mock.patch("random.choice") as choice:
                from pantera import caos
                choice.return_value = expected
                vm = caos.choice_vm()
        self.assertEqual(expected, vm)
