package com.zfoo.net.util;

import org.junit.Assert;
import org.junit.Ignore;
import org.junit.Test;
import java.io.IOException;


import com.zfoo.net.util.NetUtils;
import com.zfoo.net.util.NetUtils.*;
import java.util.List;
import java.util.Arrays;

public class NetUtilsTest_ipv4Test {
    public static long inputTransformation_ipv4Test(String ipStr1) {
        // Extracted logic from ipv4ToLong method
        if (isValidAddress(ipStr1)) {
            long[] ip = new long[4];
            int position1 = ipStr1.indexOf(".");
            int position2 = ipStr1.indexOf(".", position1 + 1);
            int position3 = ipStr1.indexOf(".", position2 + 1);
            ip[0] = Long.parseLong(ipStr1.substring(0, position1));
            ip[1] = Long.parseLong(ipStr1.substring(position1 + 1, position2));
            ip[2] = Long.parseLong(ipStr1.substring(position2 + 1, position3));
            ip[3] = Long.parseLong(ipStr1.substring(position3 + 1));
            return (ip[0] * 1_000_000_000) + (ip[1] * 1_000_000) + (ip[2] * 1_000) + ip[3];
        }
        return 0;
    }
}