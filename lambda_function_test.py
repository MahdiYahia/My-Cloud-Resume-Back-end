import os
import re
import json
from unittest import mock
from function import app


with open('template.yaml', 'r') as template:
    TABLENAME = re.search(r'TableName: (.*)?', template.read()).group(1)
    
@mock.patch.dict(os.
