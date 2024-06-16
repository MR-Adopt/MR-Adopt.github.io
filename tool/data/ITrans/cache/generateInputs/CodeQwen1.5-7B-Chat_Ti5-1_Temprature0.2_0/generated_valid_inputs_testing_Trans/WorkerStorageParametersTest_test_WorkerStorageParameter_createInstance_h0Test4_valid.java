/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.druid.msq.exec;

import org.apache.druid.msq.exec.WorkerStorageParametersTest_test_WorkerStorageParameter_createInstance;

import org.apache.druid.msq.exec.WorkerStorageParameters;
import org.apache.druid.msq.exec.WorkerStorageParameters.*;
import java.util.Arrays;
import java.util.List;
import org.apache.druid.msq.indexing.error.MSQException;
import org.apache.druid.msq.indexing.error.NotEnoughTemporaryStorageFault;
import org.junit.Assert;
import org.junit.Test;

public class WorkerStorageParametersTest_test_WorkerStorageParameter_createInstance_h0Test4_valid {

    @Test
    public void test_WorkerStorageParameter_createInstance_h0Test4() {
    long l = 500000000;
		List<Object> transformed_inputs = WorkerStorageParametersTest_test_WorkerStorageParameter_createInstance.inputTransformation_test_WorkerStorageParameter_createInstance(l);
    long l2  = (long) transformed_inputs.get(0);
    boolean b  = (boolean) transformed_inputs.get(1);
        Assert.assertEquals(WorkerStorageParameters.createInstanceForTests(l), WorkerStorageParameters.createInstance(l2, b));
    }
}

