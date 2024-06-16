/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.dolphinscheduler.plugin.registry.etcd;

import org.apache.dolphinscheduler.plugin.registry.etcd.EtcdKeepAliveLeaseManager;
import org.apache.dolphinscheduler.plugin.registry.etcd.EtcdKeepAliveLeaseManager.*;

import java.io.IOException;
import java.util.Optional;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import io.etcd.jetcd.Client;
import io.etcd.jetcd.launcher.EtcdCluster;
import io.etcd.jetcd.test.EtcdClusterExtension;

class EtcdKeepAliveLeaseManagerTest_getOrCreateKeepAliveLeaseTest_GT {

    static EtcdClusterExtension server;

    static Client client;

    static EtcdKeepAliveLeaseManager etcdKeepAliveLeaseManager;
    @BeforeAll
    public static void before() throws Exception {
        server = EtcdClusterExtension.builder()
                .withNodes(1)
                .withImage("ibmcom/etcd:3.2.24")
                .build();
        server.restart();

        client = Client.builder().endpoints(server.clientEndpoints()).build();

        etcdKeepAliveLeaseManager = new EtcdKeepAliveLeaseManager(client);
    }

    @Test
    void getOrCreateKeepAliveLeaseTest_h() throws Exception {
        String key1 = "/test";
        int timeToLive1 = 3;
        String key2 = "/test";
        int timeToLive2 = 3;
        long first = etcdKeepAliveLeaseManager.getOrCreateKeepAliveLease(key1, timeToLive1);
        long second = etcdKeepAliveLeaseManager.getOrCreateKeepAliveLease(key2, timeToLive2);
        Assertions.assertEquals(first, second);

        client.getLeaseClient().revoke(first).get();

        // wait for lease expire
        Thread.sleep(3000);
        Optional<Long> keepAliveLease = etcdKeepAliveLeaseManager.getKeepAliveLease(key1);
        Assertions.assertFalse(keepAliveLease.isPresent());
    }


    public static String inputTransformation_getOrCreateKeepAliveLeaseTest(String key1) {
        String key2 = key1;
        return key2;
    }


    @Test
    void getOrCreateKeepAliveLeaseTest_IT() throws Exception {
        String key1 = "/test";
        int timeToLive1 = 3;
        String key2 = inputTransformation_getOrCreateKeepAliveLeaseTest(key1);
        int timeToLive2 = 3;
        long first = etcdKeepAliveLeaseManager.getOrCreateKeepAliveLease(key1, timeToLive1);
        long second = etcdKeepAliveLeaseManager.getOrCreateKeepAliveLease(key2, timeToLive2);
        Assertions.assertEquals(first, second);

        client.getLeaseClient().revoke(first).get();

        // wait for lease expire
        Thread.sleep(timeToLive1*10);
        Optional<Long> keepAliveLease = etcdKeepAliveLeaseManager.getKeepAliveLease(key2);
        Assertions.assertFalse(keepAliveLease.isPresent());
    }

    @AfterAll
    public static void after() throws IOException {
        try (EtcdCluster closeServer = server.cluster()) {
            client.close();
        }
    }
}