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
    public static long inputTransformation_ipv4Test(String ipStr1)  {
        long ipLong2 = NetUtils.ipv4ToLong(ipStr1);
        return ipLong2;
    }
}