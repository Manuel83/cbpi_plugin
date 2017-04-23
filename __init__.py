from modules import cbpi

from modules.core.hardware import ActorBase

@cbpi.actor
class SSR(ActorBase):
    @classmethod
    def init_global(cls):
        print "GLOBAL %s ACTOR" % (cls.__name__)


@cbpi.actor
class Relay(ActorBase):
    @classmethod
    def init_global(cls):
        print "GLOBAL %s ACTOR" % (cls.__name__)

