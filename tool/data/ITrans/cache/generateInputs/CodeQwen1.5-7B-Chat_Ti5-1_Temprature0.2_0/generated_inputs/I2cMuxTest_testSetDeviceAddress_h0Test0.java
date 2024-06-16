package org.myrobotlab.service;

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
public class I2cMuxTest_testSetDeviceAddress_h0Test0 {

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
    public void testSetDeviceAddress_h0Test0() {
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceAddress = "0x7F";
    I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    i2cMux.setDeviceAddress(deviceAddress);
        i2cMux.setDeviceAddress(deviceAddress);
        assertEquals(deviceAddress, i2cMux2.getDeviceAddress());
    }
}

