from labgrid.resource.remote import NetworkSISPMCTLPowerPort
from labgrid.driver.powerdriver import SISPMCTLPowerDriver


def test_sispmctl_create(target):
    r = NetworkSISPMCTLPowerPort(target,
            name=None,
            host="localhost",
            busnum=0,
            devnum=1,
            path='0:1',
            vendor_id=0x0,
            model_id=0x0,
            index=1,
    )
    d = SISPMCTLPowerDriver(target, name=None)
    assert (isinstance(d, SISPMCTLPowerDriver))
