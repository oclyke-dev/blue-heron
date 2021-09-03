import pytest

from blue_heron import xmltools
import xml.etree.ElementTree as ET

def test_with_tag():
  # todo: add tests for other kinds of iterables as input to the with tags function...

  root = ET.Element('root')
  search_tags = ['body', 'wave', 'part', 'lib']
  extra_tags = ['type', 'sand', 'grain', 'ergot']
  all_tags = search_tags + extra_tags
  for tag in all_tags:
    ET.SubElement(root, tag)

  result = xmltools.with_tags(root, search_tags)

  # check that none of the extra tags were included in the result
  for element in result:
    assert element.tag not in extra_tags

def test_with_attributes():
  # todo:

  root = ET.Element('root')
  tag = 'test'
  desired = {
    'Status': 'complete',
    'done': True,
  }

  golden = ET.SubElement(root, tag) # this *is* the element we want to find
  for key, value in desired.items():
    golden.set(key, value)
  
  ET.SubElement(root, tag).set('Status', 'something else')
  ET.SubElement(root, tag).set('done', False)
  confuser = ET.SubElement(root, tag)
  confuser.set('Status', 'incomplete')
  confuser.set('done', False)

  result = xmltools.with_attributes(root, desired)

  assert len(list(result)) == 1
