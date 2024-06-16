package org.datagear.util.version;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;


import org.datagear.util.version.Version;
import org.datagear.util.version.Version.*;
import java.util.List;
import java.util.Arrays;

public class VersionTest_isEqualTest {
    public static String inputTransformation_isEqualTest(String version)  {
        String[] vs = version.split("\\.");
        String major = vs[0];
        String minor = (vs.length > 1 ? vs[1] : null);
        String revision = (vs.length > 2 ? vs[2] : null);
        String build = null;
        if (revision != null) {
            String[] bs = revision.split("-");
            revision = bs[0];
            build = (bs.length > 1 ? bs[1] : null);
        } else if (minor != null) {
            String[] bs = minor.split("-");
            minor = bs[0];
            build = (bs.length > 1 ? bs[1] : null);
        } else {
            build = (major.split("-").length > 1 ? major.split("-")[1] : null);
        }
        return major + (minor != null ? "." + minor : "") + (revision != null ? "." + revision : "") + (build != null ? "-" + build : "");
    }
}