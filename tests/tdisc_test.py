import unittest

from click.testing import CliRunner

from tests_discoverer.tdisc import cli


class TdiscTest(unittest.TestCase):

    def test_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli)
        self.assertEqual(0, result.exit_code)
