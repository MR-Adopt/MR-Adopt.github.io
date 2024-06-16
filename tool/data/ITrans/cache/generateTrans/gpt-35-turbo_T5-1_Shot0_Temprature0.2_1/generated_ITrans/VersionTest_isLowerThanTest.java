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
        String major = vs[0];
        String minor = (vs.length > 1 ? vs[1] : null);
        String revision = (vs.length > 2 ? vs[2] : null);
        
        if (minor != null) {
            int minorVersion = Integer.parseInt(minor);
            minor = String.valueOf(minorVersion + 1);
        } else {
            minor = "1";
        }
        
        if (revision != null) {
            int revisionVersion = Integer.parseInt(revision);
            revision = String.valueOf(revisionVersion + 1);
        } else {
            revision = "1";
        }
        
        return major + "." + minor + "." + revision;
    }
}