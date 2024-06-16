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
package org.apache.rocketmq.tieredstore.common;

import org.apache.rocketmq.tieredstore.common.InFlightRequestFutureTest_testInFlightRequestKey;

import org.apache.rocketmq.tieredstore.common.InFlightRequestKey;
import org.apache.rocketmq.tieredstore.common.InFlightRequestKey.*;
import org.apache.rocketmq.tieredstore.common.InFlightRequestFuture;
import org.apache.rocketmq.tieredstore.common.InFlightRequestFuture.*;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import org.apache.commons.lang3.tuple.Pair;
import org.junit.Assert;
import org.junit.Test;

public class InFlightRequestFutureTest_testInFlightRequestKey_h5Test2_valid {

    @Test
    public void testInFlightRequestKey_h5Test2() {
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2  = InFlightRequestFutureTest_testInFlightRequestKey.inputTransformation_testInFlightRequestKey(requestKey1);
        Assert.assertEquals(requestKey1.hashCode(), requestKey2.hashCode());
    }
}

