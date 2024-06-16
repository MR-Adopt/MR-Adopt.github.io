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
        String[] parts = version.split("\\.");
        int revision = Integer.parseInt(parts[2]);
        revision++;
        return parts[0] + "." + parts[1] + "." + revision;
    }
}