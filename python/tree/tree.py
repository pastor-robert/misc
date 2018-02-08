'''A simple tree implementation'''

from collections import defaultdict

__all__ = ['tree']

class tree(defaultdict):
  '''A simple tree implementation, stolen from https://gist.github.com/hrldcpr/2012250

     taxonomy = tree()
     taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Felis']['cat']
     taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Panthera']['lion']
     taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['dog']
     taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['coyote']
     taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
     taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
     taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']
     pprint (taxonomy.as_dict())

     {'Animalia': {'Chordata': {'Mammalia': {'Carnivora': {'Canidae': {'Canis': {'coyote': {},
                                                                                 'dog': {}}},
                                                           'Felidae': {'Felis': {'cat': {}},
                                                                       'Panthera': {'lion': {}}}}}}},
      'Plantae': {'Solanales': {'Convolvulaceae': {'Ipomoea': {'sweet potato': {}}},
                                'Solanaceae': {'Solanum': {'potato': {},
                                                           'tomato': {}}}}}}

  '''

  def __init__(self):
    defaultdict.__init__(self, tree)
  def __str__(self):
    return dict.__str__(self)
  def __repr__(self):
    return dict.__repr__(self)
  def as_dict(self):
    return{k:v.as_dict() for k,v in self.items()}
