package org.myrobotlab.service;

import org.myrobotlab.service.I2cMuxTest_testSetDeviceBus;

import org.myrobotlab.service.I2cMux;
import org.myrobotlab.service.I2cMux.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import java.util.Arrays;
import java.util.List;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnit;
import org.mockito.junit.MockitoRule;
import org.myrobotlab.service.interfaces.I2CControl;
import org.myrobotlab.service.interfaces.I2CController;

@RunWith(JUnit4.class)
public class I2cMuxTest_testSetDeviceBus_h0Test1_valid {

    @Rule
    public MockitoRule rule = MockitoJUnit.rule();

    @Mock
    private I2CController mockController;

    @Mock
    private I2CControl mockControl;

    I2cMux i2cMux;

    @Before
    public void setUp() {
        i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
        when(mockController.getName()).thenReturn("controller");
        when(mockControl.getName()).thenReturn("controlName");
        when(mockControl.getBus()).thenReturn("bus");
        when(mockControl.getAddress()).thenReturn("address");
    }

    @Test
    public void testSetDeviceBus_h0Test1() {
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "7";
    I2cMux i2cMux2  = I2cMuxTest_testSetDeviceBus.inputTransformation_testSetDeviceBus(i2cMux, deviceBus);
    i2cMux.setDeviceBus(deviceBus);
        i2cMux.setDeviceBus(deviceBus);
        assertEquals(deviceBus, i2cMux2.getDeviceBus());
    }
}

