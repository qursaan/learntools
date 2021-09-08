
from learntools.core import *


class ImageAnalysis1(CodingProblem):
    _var = 'description'
    def check(self, desc):
        assert (desc.serialize()['description']['captions'][0]['text'] == 'a woman showing her phone to a child')
        assert (round(desc.serialize()['description']['captions'][0]['confidence'],2) == 0.39)


class ImageAnalysis2(CodingProblem):
    _var = 'description'
    def check(self, desc):
        assert (desc.serialize()['description']['captions'][0]['text'] == 'a person holding a phone')
        assert (round(desc.serialize()['description']['captions'][0]['confidence'],2) == 0.33)


class ImageFeature(CodingProblem):
    _var = 'analysis'
    def check(self, analysis):
        assert (len(analysis.tags)==21)
        assert (analysis.serialize()['description']['captions'][0]['text'] == 'a woman showing her phone to a child')
        assert (round(analysis.serialize()['description']['captions'][0]['confidence'],2) == 0.39)

qvars = bind_exercises(globals(), [
        ImageAnalysis1,
        ImageAnalysis2,
        ImageFeature,
    ],)
__all__ = list(qvars)
