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
        int revision = (vs.length > 2 ? Integer.parseInt(vs[2]) : 0);
        int build = (vs.length > 3 ? Integer.parseInt(vs[3]) : 0);
        
        // Increment the minor version number
        minor++;
        
        // Reset the revision and build numbers
        revision = 0;
        build = 0;
        
        // Construct the transformed version string
        String transformedVersion = major + "." + minor + "." + revision + "." + build;
        
        return transformedVersion;
    }
}