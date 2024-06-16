package org.datagear.util.version;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;


import org.datagear.util.version.Version;
import org.datagear.util.version.Version.*;
import java.util.List;
import java.util.Arrays;

public class VersionTest_stringOfTest {
    public static Version inputTransformation_stringOfTest(String version)  {
        Version version1 = Version.valueOf(version);
        return version1;
    }
}