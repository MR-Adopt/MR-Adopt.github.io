package org.apache.druid.storage.azure;

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


import org.apache.druid.storage.azure.AzureClientFactory;
import org.apache.druid.storage.azure.AzureClientFactory.*;
import java.util.List;
import java.util.Arrays;

import org.apache.commons.lang3.tuple.Pair;

public class AzureClientFactoryTest_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount {
    public static List<Object> inputTransformation_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount(Integer retryCount1, String ACCOUNT1) {
        Integer retryCount2 = retryCount1;
        String ACCOUNT2 = ACCOUNT1;
        List<Object> transformed_inputs = Arrays.asList(retryCount2, ACCOUNT2);
        return transformed_inputs;
    }
}