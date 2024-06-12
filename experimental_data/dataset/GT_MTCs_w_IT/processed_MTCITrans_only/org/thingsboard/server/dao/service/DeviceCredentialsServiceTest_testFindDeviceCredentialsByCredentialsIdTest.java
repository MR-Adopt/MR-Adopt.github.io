/**
 * Copyright © 2016-2024 The Thingsboard Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.thingsboard.server.dao.service;

import org.thingsboard.server.dao.device.DeviceCredentialsService.*;

import com.datastax.oss.driver.api.core.uuid.Uuids;
import org.junit.Assert;
import org.junit.Test;
import org.junit.jupiter.api.Assertions;
import org.springframework.beans.factory.annotation.Autowired;
import org.thingsboard.server.common.data.Device;
import org.thingsboard.server.common.data.id.DeviceCredentialsId;
import org.thingsboard.server.common.data.id.DeviceId;
import org.thingsboard.server.common.data.security.DeviceCredentials;
import org.thingsboard.server.common.data.security.DeviceCredentialsType;
import org.thingsboard.server.dao.device.DeviceCredentialsService;
import org.thingsboard.server.dao.device.DeviceService;
import org.thingsboard.server.dao.exception.DataValidationException;
import org.thingsboard.server.common.data.id.TenantId;

@DaoSqlTest
public class DeviceCredentialsServiceTest_testFindDeviceCredentialsByCredentialsIdTest extends AbstractServiceTest {

    @Autowired
    static
    DeviceCredentialsService deviceCredentialsService;
    @Autowired
    DeviceService deviceService;

//     @Test
//     public void testFindDeviceCredentialsByCredentialsId_h() {
//         Device device = new Device();
//         device.setTenantId(tenantId);
//         device.setName("My device");
//         device.setType("default");
//         Device savedDevice = deviceService.saveDevice(device);
//         DeviceCredentials deviceCredentials = deviceCredentialsService.findDeviceCredentialsByDeviceId(tenantId, savedDevice.getId());
//         Assert.assertEquals(savedDevice.getId(), deviceCredentials.getDeviceId());
//         System.out.println("deviceCredentials.getCredentialsId() = " + deviceCredentials.getCredentialsId());
//         System.out.println("tenantId " + tenantId);
//         DeviceCredentials foundDeviceCredentials = deviceCredentialsService.findDeviceCredentialsByCredentialsId(deviceCredentials.getCredentialsId());
//         Assert.assertEquals(deviceCredentials, foundDeviceCredentials);
//         deviceService.deleteDevice(tenantId, savedDevice.getId());
//         foundDeviceCredentials = deviceCredentialsService.findDeviceCredentialsByCredentialsId(deviceCredentials.getCredentialsId());
//         Assert.assertNull(foundDeviceCredentials);
//     }
// 
// //     public static String inputTransformation_testFindDeviceCredentialsByCredentialsId(TenantId tenantId, Device savedDevice) {
// //         DeviceCredentials deviceCredentials = deviceCredentialsService.findDeviceCredentialsByDeviceId(tenantId, savedDevice.getId());
// //         String id = deviceCredentials.getCredentialsId();
// //         return id;
// //     }
// // 
    @Test
    public void testFindDeviceCredentialsByCredentialsId_IT() {
        Device device = new Device();
        device.setTenantId(tenantId);
        device.setName("My device");
        device.setType("default");
        Device savedDevice = deviceService.saveDevice(device);
        DeviceCredentials deviceCredentials = deviceCredentialsService.findDeviceCredentialsByDeviceId(tenantId, savedDevice.getId());

        System.out.println("deviceCredentials.getCredentialsId() = " + deviceCredentials.getCredentialsId());
        System.out.println("tenantId " + tenantId);


        Assert.assertEquals(savedDevice.getId(), deviceCredentials.getDeviceId());
        String id = DeviceCredentialsServiceTest_testFindDeviceCredentialsByCredentialsId.inputTransformation_testFindDeviceCredentialsByCredentialsId(tenantId, savedDevice);
        DeviceCredentials foundDeviceCredentials = deviceCredentialsService.findDeviceCredentialsByCredentialsId(id);
        Assert.assertEquals(deviceCredentials, foundDeviceCredentials);
        deviceService.deleteDevice(tenantId, savedDevice.getId());
        foundDeviceCredentials = deviceCredentialsService.findDeviceCredentialsByCredentialsId(deviceCredentials.getCredentialsId());
        Assert.assertNull(foundDeviceCredentials);
    }

}