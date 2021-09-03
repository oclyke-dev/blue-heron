
import blue_heron
import pytest
from pathlib import Path
from lxml import etree as ET

from blue_heron import Root, Drawing

@pytest.fixture(scope='module')
def test_board():
  with open(Path(__file__).parent.parent/'data/test/ArtemisDevKit.brd', 'r') as f:
    root = ET.parse(f).getroot()
  yield root

def test_get_drawing(test_board):
  root = Root(test_board)
  drawing = root.drawing
  assert type(drawing) == type(blue_heron.drawing.Drawing(None))
