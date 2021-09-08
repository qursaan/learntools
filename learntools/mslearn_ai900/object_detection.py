
from learntools.core import *


class ObjectDetection(CodingProblem):
    _var = 'result'
    def check(self, result):
        assert (len(results.predictions)==13)
        assert (len([x for x in results.predictions if x.probability*100>50])==4)
        assert ('banana' in ([x.tag_name for x in results.predictions if x.probability*100>50]))
        assert ('apple' in ([x.tag_name for x in results.predictions if x.probability*100>50]))
        assert ('orange' in ([x.tag_name for x in results.predictions if x.probability*100>50]))

qvars = bind_exercises(globals(), [
        ObjectDetection,
    ],)
__all__ = list(qvars)
