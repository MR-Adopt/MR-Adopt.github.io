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
        String[] parts = version.split("\\.");
        int lastPart = Integer.parseInt(parts[parts.length - 1]);
        lastPart++;
        parts[parts.length - 1] = String.valueOf(lastPart);
        return String.join(".", parts);
    }
}