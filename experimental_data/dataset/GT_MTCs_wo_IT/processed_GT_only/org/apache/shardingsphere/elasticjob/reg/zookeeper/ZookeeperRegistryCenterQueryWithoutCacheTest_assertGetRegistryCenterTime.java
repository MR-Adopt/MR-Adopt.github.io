/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.shardingsphere.elasticjob.reg.zookeeper;

import org.apache.shardingsphere.elasticjob.reg.zookeeper.ZookeeperRegistryCenter;
import org.apache.shardingsphere.elasticjob.reg.zookeeper.ZookeeperRegistryCenter.*;

import org.apache.shardingsphere.elasticjob.reg.zookeeper.env.RegistryCenterEnvironmentPreparer;
import org.apache.shardingsphere.elasticjob.test.util.EmbedTestingServer;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Collections;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class ZookeeperRegistryCenterQueryWithoutCacheTest_assertGetRegistryCenterTime {
    
    private static final EmbedTestingServer EMBED_TESTING_SERVER = new EmbedTestingServer(9181);
    
    private static final ZookeeperConfiguration ZOOKEEPER_CONFIGURATION =
            new ZookeeperConfiguration(EMBED_TESTING_SERVER.getConnectionString(), ZookeeperRegistryCenterQueryWithoutCacheTest_assertGetRegistryCenterTime.class.getName());
    
    private static ZookeeperRegistryCenter zkRegCenter;
    
    @BeforeAll
    static void setUp() {
        EMBED_TESTING_SERVER.start();
        ZOOKEEPER_CONFIGURATION.setConnectionTimeoutMilliseconds(30000);
        zkRegCenter = new ZookeeperRegistryCenter(ZOOKEEPER_CONFIGURATION);
        zkRegCenter.init();
        RegistryCenterEnvironmentPreparer.persist(zkRegCenter);
        zkRegCenter.addCacheData("/other");
    }
    
    @AfterAll
    static void tearDown() {
        zkRegCenter.close();
    }
    
    @Test
    void assertGetRegistryCenterTime_h() {
        String path1 = "/_systemTime/current";
        String path2 = "/_systemTime/current";
        long regCenterTime = zkRegCenter.getRegistryCenterTime(path1);
        assertTrue(regCenterTime <= System.currentTimeMillis());
        long updatedRegCenterTime = zkRegCenter.getRegistryCenterTime(path2);
        assertTrue(regCenterTime < updatedRegCenterTime);
    }

    public static String inputTransformation_assertGetRegistryCenterTime(String path1) {
        String path2 = path1;
        return path2;
    }

    @Test
    void assertGetRegistryCenterTime_IT() {
        String path1 = "/_systemTime/current";
        String path2 = inputTransformation_assertGetRegistryCenterTime(path1);
        long regCenterTime = zkRegCenter.getRegistryCenterTime(path1);
        assertTrue(regCenterTime <= System.currentTimeMillis());
        long updatedRegCenterTime = zkRegCenter.getRegistryCenterTime(path2);
        assertTrue(regCenterTime < updatedRegCenterTime);
    }
    
}