from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name ='biketrauma_ponch',
  version = current_version,
  description ='Visualization of a bicycle accident db',
  url ='http://github.com/Poncheele.git',
  author ='Poncheele',
  author_email ='clementponcheele@gmail.com',
  license ='MIT',
  packages = ['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe = False
)