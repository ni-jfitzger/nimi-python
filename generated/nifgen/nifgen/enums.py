# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class AnalogPath(Enum):
    MAIN = 0
    r'''
    Specifies use of the main path.  NI-FGEN chooses the amplifier based on the user-specified gain.
    '''
    DIRECT = 1
    r'''
    Specifies use of the direct path.
    '''
    FIXED_LOW_GAIN = 2
    r'''
    Specifies use of the low-gain amplifier in the main path, no matter  what value the user specifies for gain. This setting limits the output  range.
    '''
    FIXED_HIGH_GAIN = 3
    r'''
    Specifies use of the high-gain amplifier in the main path.
    '''


class BusType(Enum):
    INVALID = 0
    r'''
    Indicates an invalid bus type.
    '''
    AT = 1
    r'''
    Indicates the signal generator is the AT bus type.
    '''
    PCI = 2
    r'''
    Indicates the signal generator is the PCI bus type.
    '''
    PXI = 3
    r'''
    Indicates the signal generator is the PXI bus type.
    '''
    VXI = 4
    r'''
    Indicates the signal generator is the VXI bus type.
    '''
    PCMCIA = 5
    r'''
    Indicates the signal generator is the PCI-CMA bus type.
    '''
    PXIE = 6
    r'''
    Indicates the signal generator is the PXI Express bus type.
    '''


class ByteOrder(Enum):
    LITTLE = 0
    BIG = 1


class ClockMode(Enum):
    HIGH_RESOLUTION = 0
    r'''
    High resolution sampling—Sample rate is generated by a high–resolution clock source.
    '''
    DIVIDE_DOWN = 1
    r'''
    Divide down sampling—Sample rates are generated by dividing the source frequency.
    '''
    AUTOMATIC = 2
    r'''
    Automatic Selection—NI-FGEN selects between the divide–down and high–resolution clocking modes.
    '''


class DataMarkerEventLevelPolarity(Enum):
    HIGH = 101
    r'''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    r'''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class EventPulseWidthUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    r'''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    r'''
    Specifies the pulse width in seconds.
    '''


class HardwareState(Enum):
    IDLE = 0
    WAITING_FOR_START_TRIGGER = 100
    RUNNING = 200
    DONE = 600
    HARDWARE_ERROR = 1000


class IdleBehavior(Enum):
    HOLD_LAST = 400
    r'''
    While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.
    '''
    JUMP_TO = 401
    r'''
    While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value property.
    '''


class OutputMode(Enum):
    FUNC = 0
    r'''
    Standard Method mode—  Generates standard method waveforms  such as sine, square, triangle, and so on.
    '''
    ARB = 1
    r'''
    Arbitrary waveform mode—Generates  waveforms from user-created/provided  waveform arrays of numeric data.
    '''
    SEQ = 2
    r'''
    Arbitrary sequence mode —  Generates downloaded waveforms  in an order your specify.
    '''
    FREQ_LIST = 101
    r'''
    Frequency List mode—Generates a  standard method using a list of  frequencies you define.
    '''
    SCRIPT = 102
    r'''
    **Script mode—**\ Allows you to use scripting to link and loop multiple
    waveforms in complex combinations.
    '''


class ReferenceClockSource(Enum):
    CLOCK_IN = 'ClkIn'
    r'''
    Specifies that the CLK IN input signal from the front panel connector is
    used as the Reference Clock source.
    '''
    NONE = 'None'
    r'''
    Specifies that a Reference Clock is not used.
    '''
    ONBOARD_REFERENCE_CLOCK = 'OnboardRefClk'
    r'''
    Specifies that the onboard Reference Clock is used as the Reference
    Clock source.
    '''
    PXI_CLOCK = 'PXI_Clk'
    r'''
    Specifies that the PXI Clock is used as the Reference Clock source.
    '''
    RTSI_7 = 'RTSI7'
    r'''
    Specifies that the RTSI line 7 is used as the Reference Clock source.
    '''


class RelativeTo(Enum):
    START = 0
    CURRENT = 1


class SampleClockSource(Enum):
    CLOCK_IN = 'ClkIn'
    r'''
    Specifies that the signal at the CLK IN front panel connector is used as
    the Sample Clock source.
    '''
    DDC_CLOCK_IN = 'DDC_ClkIn'
    r'''
    Specifies that the Sample Clock from the DDC connector is used as the Sample
    Clock source.
    '''
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    Specifies that the onboard clock is used as the Sample Clock source.
    '''
    PXI_STAR_LINE = 'PXI_Star'
    r'''
    Specifies that the PXI\_STAR trigger line is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_0_RTSI_0 = 'PXI_Trig0'
    r'''
    Specifies that the PXI or RTSI line 0 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_1_RTSI_1 = 'PXI_Trig1'
    r'''
    Specifies that the PXI or RTSI line 1 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_2_RTSI_2 = 'PXI_Trig2'
    r'''
    Specifies that the PXI or RTSI line 2 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_3_RTSI_3 = 'PXI_Trig3'
    r'''
    Specifies that the PXI or RTSI line 3 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_4_RTSI_4 = 'PXI_Trig4'
    r'''
    Specifies that the PXI or RTSI line 4 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_5_RTSI_5 = 'PXI_Trig5'
    r'''
    Specifies that the PXI or RTSI line 5 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_6_RTSI_6 = 'PXI_Trig6'
    r'''
    Specifies that the PXI or RTSI line 6 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_7_RTSI_7 = 'PXI_Trig7'
    r'''
    Specifies that the PXI or RTSI line 7 is used as the Sample Clock
    source.
    '''


class SampleClockTimebaseSource(Enum):
    CLOCK_IN = 'ClkIn'
    r'''
    Specifies that the external signal on the CLK IN front panel connector
    is used as the source.
    '''
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    Specifies that the onboard Sample Clock timebase is used as the source.
    '''


class ScriptTriggerDigitalEdgeEdge(Enum):
    RISING = 101
    r'''
    Rising Edge
    '''
    FALLING = 102
    r'''
    Falling Edge
    '''


class ScriptTriggerType(Enum):
    TRIG_NONE = 101
    r'''
    No trigger is configured. Signal generation starts immediately.
    '''
    DIGITAL_EDGE = 102
    r'''
    Trigger is asserted when a digital edge is detected.
    '''
    DIGITAL_LEVEL = 103
    r'''
    Trigger is asserted when a digital level is detected.
    '''
    SOFTWARE_EDGE = 104
    r'''
    Trigger is asserted when a software edge is detected.
    '''


class StartTriggerDigitalEdgeEdge(Enum):
    RISING = 101
    r'''
    Rising Edge
    '''
    FALLING = 102
    r'''
    Falling Edge
    '''


class StartTriggerType(Enum):
    TRIG_NONE = 101
    r'''
    None
    '''
    DIGITAL_EDGE = 102
    r'''
    Digital Edge
    '''
    SOFTWARE_EDGE = 104
    r'''
    Software Edge
    '''
    P2P_ENDPOINT_FULLNESS = 106
    r'''
    P2P Endpoint Fullness
    '''


class TerminalConfiguration(Enum):
    SINGLE_ENDED = 300
    r'''
    Single-ended operation
    '''
    DIFFERENTIAL = 301
    r'''
    Differential operation
    '''


class Trigger(Enum):
    START = 1004
    SCRIPT = 103


class TriggerMode(Enum):
    SINGLE = 1
    r'''
    Single Trigger Mode - The waveform you describe in the sequence list is  generated only once by going through the entire staging list. Only one  trigger is required to start the waveform generation. You can use Single  trigger mode with the output mode in any mode. After a trigger is  received, the waveform generation starts from the first stage and  continues through to the last stage. Then, the last stage generates  repeatedly until you stop the waveform generation.
    '''
    CONTINUOUS = 2
    r'''
    Continuous Trigger Mode - The waveform you describe in the staging list generates infinitely by repeatedly cycling through the staging list.  After a trigger is received, the waveform generation starts from the  first stage and continues through to the last stage. After the last stage  completes, the waveform generation loops back to the start of the  first stage and continues until it is stopped. Only one trigger is  required to start the waveform generation.
    '''
    STEPPED = 3
    r'''
    Stepped Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates. Then, the device waits for the  next trigger signal. On the next trigger, the waveform described by the  second stage generates, and so on. After the staging list completes,  the waveform generation returns to the first stage and continues in a  cyclic fashion. After any stage has generated completely, the first  eight samples of the next stage are repeated continuously until the next  trigger is received.
    trigger mode.

    Note: In Frequency List mode, Stepped trigger mode is the same as Burst
    '''
    BURST = 4
    r'''
    Burst Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates until another trigger is  received. At the next trigger, the buffer of the previous stage completes, and then the waveform described by the second stage generates. After the staging list completes, the waveform generation  returns to the first stage and continues in a cyclic fashion. In  Frequency List mode, the duration instruction is ignored, and the trigger  switches the frequency to the next frequency in the list.
    trigger mode.

    Note: In Frequency List mode, Stepped trigger mode is the same as Burst
    '''


class WaitBehavior(Enum):
    HOLD_LAST = 400
    r'''
    While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.
    '''
    JUMP_TO = 401
    r'''
    While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value property.
    '''


class Waveform(Enum):
    SINE = 1
    r'''
    Sinusoid waveform
    '''
    SQUARE = 2
    r'''
    Square waveform
    '''
    TRIANGLE = 3
    r'''
    Triange waveform
    '''
    RAMP_UP = 4
    r'''
    Positive ramp waveform
    '''
    RAMP_DOWN = 5
    r'''
    Negative ramp waveform
    '''
    DC = 6
    r'''
    Constant voltage
    '''
    NOISE = 101
    r'''
    White noise
    '''
    USER = 102
    r'''
    User-defined waveform as defined by the define_user_standard_waveform method.
    '''
