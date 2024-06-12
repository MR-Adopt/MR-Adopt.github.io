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

package cn.hippo4j.common.toolkit.logtracing;

import cn.hippo4j.common.toolkit.logtracing.LogMessage;
import cn.hippo4j.common.toolkit.logtracing.LogMessage.*;

import org.apache.logging.log4j.util.Strings;
import org.junit.Before;
import org.junit.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class LogMessageTest_testSetMsgShouldSetAnewMessageInLogMessage {

    private final static String MESSAGE = "message";
    private final static String THROWABLE_MESSAGE = "throwable message";
    private LogMessage logMessage;

//     @Before
//     public void init() {
//         logMessage = LogMessage.getInstance();
//     }
// 
//     @Test
//     public void testSetMsgShouldSetAnewMessageInLogMessage_h() {
//         LogMessage logMessage = LogMessage.getInstance();
//         String MESSAGE = "message";
//         logMessage.setMsg(MESSAGE);
// 
//         LogMessage logMessage2 = LogMessage.getInstance(); logMessage2.setMsg("message");
//         assertEquals(MESSAGE, logMessage2.toString());
//     }
// 
//     @Test
//     public void testSetMsgShouldSetAnewMessageInLogMessage_IT() {
//         LogMessage logMessage = LogMessage.getInstance();
//         String MESSAGE = "message";
//         logMessage.setMsg(MESSAGE);
// 
//         LogMessage logMessage2 = inputTransformation_testSetMsgShouldSetAnewMessageInLogMessage(logMessage, MESSAGE);
//         assertEquals(MESSAGE, logMessage2.toString());
//     }
// 
    public static LogMessage inputTransformation_testSetMsgShouldSetAnewMessageInLogMessage(LogMessage logMessage, String MESSAGE) {
        logMessage.setMsg(MESSAGE);
        return logMessage;
    }

}