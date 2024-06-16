package org.datagear.util.version;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;


import org.datagear.util.version.Version;
import org.datagear.util.version.Version.*;
import java.util.List;
import java.util.Arrays;

public class VersionTest_isLowerThanTest {
    public static String inputTransformation_isLowerThanTest(String version)  {
        String[] vs = version.split("\\.");
        int major = Integer.parseInt(vs[0]);
        int minor = (vs.length > 1 ? Integer.parseInt(vs[1]) : 0);
        int revision = (vs.length > 2 ? Integer.parseInt(vs[2]) : 0);
        
        // Increment the version number
        revision++;
        
        return major + "." + minor + "." + revision;
    }
}