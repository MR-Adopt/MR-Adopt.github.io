package org.datagear.util.version;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;


import org.datagear.util.version.Version;
import org.datagear.util.version.Version.*;
import java.util.List;
import java.util.Arrays;

public class VersionTest_isHigherThanTest {
    public static String inputTransformation_isHigherThanTest(String version)  {
        String[] vs = version.split("\\.");
        int major = Integer.parseInt(vs[0]);
        int minor = Integer.parseInt(vs[1]);
        int revision = Integer.parseInt(vs[2]);
        
        // Increment the minor version
        minor++;
        
        // Construct the FOLLOW UP INPUT
        String v2 = major + "." + minor + "." + revision;
        
        return v2;
    }
}