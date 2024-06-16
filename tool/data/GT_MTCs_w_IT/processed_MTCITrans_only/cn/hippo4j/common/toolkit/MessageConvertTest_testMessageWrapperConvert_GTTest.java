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

package cn.hippo4j.common.toolkit;

import cn.hippo4j.common.toolkit.MessageConvertTest_testMessageWrapperConvert_GT;

import cn.hippo4j.common.toolkit.MessageConvert;
import cn.hippo4j.common.toolkit.MessageConvert.*;

import cn.hippo4j.common.model.ThreadPoolRunStateInfo;
import cn.hippo4j.common.monitor.*;
import org.junit.Test;
import org.junit.jupiter.api.Assertions;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

/***
 * @description : Todo
 * @author : DDDreame
 * @date : 2023/5/27 23:24 
 */
public class MessageConvertTest_testMessageWrapperConvert_GTTest {


//     public void testMessageWrapperConvert_h() {
//         AbstractMessage message = new RuntimeMessage();
//         List<Message> runtimeMessages = new ArrayList<>();
//         ThreadPoolRunStateInfo poolRunState = ThreadPoolRunStateInfo.builder()
//                 .tpId("testTPid")
//                 .activeSize(4)
//                 .poolSize(12)
//                 .completedTaskCount(8L)
//                 .largestPoolSize(12)
//                 .currentLoad("6")
//                 .clientLastRefreshTime(LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")))
//                 .peakLoad("20")
//                 .queueSize(0)
//                 .queueRemainingCapacity(512)
//                 .rejectCount(0L)
//                 .timestamp(System.currentTimeMillis())
//                 .build();
//         RuntimeMessage runtimeMessage = BeanUtil.convert(poolRunState, RuntimeMessage.class);
//         runtimeMessage.setGroupKey("test-groupKeys");
//         runtimeMessages.add(runtimeMessage);
// 
//         message.setMessageType(MessageTypeEnum.RUNTIME);
//         message.setMessages(runtimeMessages);
//         MessageWrapper messageWrapper = MessageConvert.convert(message);
//         
//         AbstractMessage message2 = new RuntimeMessage();
//         MessageWrapper messageWrapper2 = new MessageWrapper();
//         message2.setMessages(runtimeMessages);
//         messageWrapper2.setMessageType(MessageTypeEnum.RUNTIME);
//         messageWrapper2.setResponseClass(message2.getClass());
//         messageWrapper2.setMessageType(message2.getMessageType());
//         List<Map<String, Object>> messageMapList = new ArrayList<>();
//         List<Message> messages = message2.getMessages();
//         messages.forEach(each -> {
//             String eachVal = JSONUtil.toJSONString(each);
//             Map mapObj = JSONUtil.parseObject(eachVal, Map.class);
//             messageMapList.add(mapObj);
//         });
//         messageWrapper2.setContentParams(messageMapList);
// 
//         // System.out.println("messageWrapper: " + messageWrapper);
//         Message messageResult = MessageConvert.convert(messageWrapper2);
//         Assertions.assertNotNull(messageResult);
//         Assertions.assertEquals(message, messageResult);
//     }
// 
    @Test
    public void testMessageWrapperConvert_IT() {
        AbstractMessage message = new RuntimeMessage();
        List<Message> runtimeMessages = new ArrayList<>();
        ThreadPoolRunStateInfo poolRunState = ThreadPoolRunStateInfo.builder()
                .tpId("testTPid")
                .activeSize(4)
                .poolSize(12)
                .completedTaskCount(8L)
                .largestPoolSize(12)
                .currentLoad("6")
                .clientLastRefreshTime(LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")))
                .peakLoad("20")
                .queueSize(0)
                .queueRemainingCapacity(512)
                .rejectCount(0L)
                .timestamp(System.currentTimeMillis())
                .build();
        RuntimeMessage runtimeMessage = BeanUtil.convert(poolRunState, RuntimeMessage.class);
        runtimeMessage.setGroupKey("test-groupKeys");
        runtimeMessages.add(runtimeMessage);

        message.setMessageType(MessageTypeEnum.RUNTIME);
        message.setMessages(runtimeMessages);
        MessageWrapper messageWrapper = MessageConvert.convert(message);
        MessageWrapper messageWrapper2 = MessageConvertTest_testMessageWrapperConvert_GT.inputTransformation_testMessageWrapperConvert(message);
        // System.out.println("messageWrapper: " + messageWrapper);
        Message messageResult = MessageConvert.convert(messageWrapper2);
        Assertions.assertNotNull(messageResult);
        Assertions.assertEquals(message, messageResult);
    }

//     public static MessageWrapper inputTransformation_testMessageWrapperConvert(AbstractMessage message) {
//         MessageWrapper messageWrapper = MessageConvert.convert(message);
//         return messageWrapper;
//     }
// 
}