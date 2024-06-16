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
        // Split the version string into major, minor, revision, and build parts
        String[] vs = version.split(SPLITTER_D_REGEX);
        String major = vs[0];
        String minor = (vs.length > 1 ? vs[1] : null);
        String revision = (vs.length > 2 ? vs[2] : null);
        String build = null;
        
        // Check if the revision version is present in the source input
        if (revision != null) {
            // Split the revision part into revision and build parts
            String[] bs = revision.split(SPLITTER_L_REGEX);
            revision = bs[0];
            build = (bs.length > 1 ? bs[1] : null);
        } 
        // Check if the minor version is present in the source input
        else if (minor != null) {
            // Split the minor part into minor and build parts
            String[] bs = minor.split(SPLITTER_L_REGEX);
            minor = bs[0];
            build = (bs.length > 1 ? bs[1] : null);
        } 
        // Check if the major version is present in the source input
        else if (major != null) {
            // Split the major part into major and build parts
            String[] bs = major.split(SPLITTER_L_REGEX);
            major = bs[0];
            build = (bs.length > 1 ? bs[1] : null);
        }
        
        // Construct the follow-up input string
        String v2 = major + (minor != null ? SPLITTER_D + minor : "") + (revision != null ? SPLITTER_D + revision : "") + (build != null ? SPLITTER_L + build : "");
        
        return v2;
    }
}