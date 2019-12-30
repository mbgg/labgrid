#import attr
#
#from ..factory import target_factory
#from .common import Resource
#
#
#@target_factory.reg_resource
#@attr.s(eq=False)
#class SISPMCTLPowerPort(Resource):
#    """This resource describes a SiS-PM (Silver Shield PM) Control power port.
#
#    Args:
#        index (int): port index
#        delay (int): delay for power cycle"""
#    index = attr.ib(validator=attr.validators.instance_of(int))
#    delay = attr.ib(validator=attr.validators.instance_of(int),
#                    converter=int)
