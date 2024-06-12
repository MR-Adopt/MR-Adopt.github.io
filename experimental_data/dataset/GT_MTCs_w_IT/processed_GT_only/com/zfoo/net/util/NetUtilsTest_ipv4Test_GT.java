/*
 * Copyright (C) 2020 The zfoo Authors
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and limitations under the License.
 */

package com.zfoo.net.util;

import com.zfoo.net.util.NetUtils;
import com.zfoo.net.util.NetUtils.*;

import org.junit.Assert;
import org.junit.Ignore;
import org.junit.Test;

import java.io.IOException;
import java.net.InetAddress;

/**
 * @author godotg
 */
public class NetUtilsTest_ipv4Test_GT {

    @Test
    public void ipv4Test_h() {
        String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
        long ipLong = NetUtils.ipv4ToLong(ipStr1);
        long ipLong2 = 127000000001L;
        String ipStr2 = NetUtils.longToIpv4(ipLong2);
        Assert.assertEquals(ipStr2, ipStr1);
    }

    public static long inputTransformation_ipv4Test(String ipStr1) {
        String ipStr = ipStr1;
        long ipLong = NetUtils.ipv4ToLong(ipStr);
        return ipLong;
    }


    @Test
    public void ipv4Test_IT() {
        String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
        long ipLong = NetUtils.ipv4ToLong(ipStr1);
        long ipLong2 = inputTransformation_ipv4Test(ipStr1);
        String ipStr2 = NetUtils.longToIpv4(ipLong2);
        Assert.assertEquals(ipStr2, ipStr1);
    }

}