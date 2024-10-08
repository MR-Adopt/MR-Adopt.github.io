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
package org.apache.druid.storage.azure;

import org.apache.druid.storage.azure.AzureClientFactoryTest_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount;

import org.apache.druid.storage.azure.AzureClientFactory;
import org.apache.druid.storage.azure.AzureClientFactory.*;
import com.azure.core.http.policy.AzureSasCredentialPolicy;
import com.azure.core.http.policy.BearerTokenAuthenticationPolicy;
import com.azure.storage.blob.BlobServiceClient;
import com.azure.storage.common.StorageSharedKeyCredential;
import com.google.common.collect.ImmutableMap;
import org.easymock.EasyMock;
import org.junit.Assert;
import org.junit.Test;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Arrays;
import java.util.List;

public class AzureClientFactoryTest_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount_h9Test3_valid {

    private AzureClientFactory azureClientFactory;

    private static final String ACCOUNT = "account";

    @Test
    public void test_blobServiceClientBuilder_useNewClientForDifferentRetryCount_h9Test3() {
    Integer retryCount1 = 10;
    String ACCOUNT1 = "account";
		List<Object> transformed_inputs = AzureClientFactoryTest_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount.inputTransformation_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount(retryCount1, ACCOUNT1);
    Integer retryCount2  = (Integer) transformed_inputs.get(0);
    String ACCOUNT2  = (String) transformed_inputs.get(1);
        AzureAccountConfig config = new AzureAccountConfig();
        config.setUseAzureCredentialsChain(true);
        azureClientFactory = new AzureClientFactory(config);
        BlobServiceClient blobServiceClient = azureClientFactory.getBlobServiceClient(retryCount1, ACCOUNT1);
        BlobServiceClient blobServiceClient2 = azureClientFactory.getBlobServiceClient(retryCount2, ACCOUNT2);
        Assert.assertNotEquals(blobServiceClient, blobServiceClient2);
    }
}

