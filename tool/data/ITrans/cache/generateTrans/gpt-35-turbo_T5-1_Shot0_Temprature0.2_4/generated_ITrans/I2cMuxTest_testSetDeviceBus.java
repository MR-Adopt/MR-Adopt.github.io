package org.myrobotlab.service;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
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


import org.myrobotlab.service.I2cMux;
import org.myrobotlab.service.I2cMux.*;
import java.util.List;
import java.util.Arrays;

public class I2cMuxTest_testSetDeviceBus {
    public static I2cMux inputTransformation_testSetDeviceBus(I2cMux i2cMux, String deviceBus)  {
        i2cMux.setDeviceBus(deviceBus);
        return i2cMux;
    }
}