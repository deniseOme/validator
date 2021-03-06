import unittest
import os
from opentargets_validator.helpers import file_or_resource, URLZSource
from opentargets_validator.validator import validate


class MinimalTests(unittest.TestCase):

    def test_minimal(self):
        loglines = 1000
        resources_path = os.path.dirname(os.path.realpath(__file__))
        data_source_file = resources_path + os.path.sep + "resources" + os.path.sep + "minimal.data.json"

        schema_source_file = resources_path + os.path.sep + "resources" + os.path.sep + "minimal.schema.json"
        schema_uri = "file://"+schema_source_file

        with URLZSource(data_source_file, loglines).open() as data_file_handle:
            validate(data_file_handle, schema_uri, loglines)