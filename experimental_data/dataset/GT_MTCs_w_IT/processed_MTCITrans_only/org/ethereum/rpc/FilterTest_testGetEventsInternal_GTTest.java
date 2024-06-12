/*
 * This file is part of RskJ
 * Copyright (C) 2023 RSK Labs Ltd.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

package org.ethereum.rpc;

import org.ethereum.rpc.Filter;
import org.ethereum.rpc.Filter.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertTrue;

class FilterTest_testGetEventsInternal_GTTest {

    Filter filter;

    @BeforeEach
    void setUp() {
        filter = new Filter();
    }

//     @Test
//     void testGetEventsInternal_h() {
//         Filter.FilterEvent mockEvent1 = new FilterEventMock();
//         Filter.FilterEvent mockEvent2 = new FilterEventMock();
//         Filter filter = new Filter(); filter.add(mockEvent1); filter.add(mockEvent2);
// 
//         // get the internal events list and make sure it's a copy of the original list
//         List<Filter.FilterEvent> events = filter.getEventsInternal();
// 
//         Filter filter2 = new Filter();filter2.add(mockEvent1); filter2.add(mockEvent2); filter2.getEventsInternal();
// 
//         assertNotSame(events, filter2.getEventsInternal());
//         assertArrayEquals(new Object[] { mockEvent1, mockEvent2 }, events.toArray());
//     }
// 
// //     public static Filter inputTransformation_testGetEventsInternal(Filter filter) {
// //         int size = filter.getEvents().length;
// //         Filter filter2 = new Filter();
// //         for (int i = 0; i < size; i++) {
// //             Filter.FilterEvent mockEvent = new FilterEventMock();
// //             filter2.add(mockEvent);
// //         }
// //         filter2.getEventsInternal();
// // 		return filter2;
// // 	}
// // 
    @Test
    void testGetEventsInternal_IT() {
        Filter.FilterEvent mockEvent1 = new FilterEventMock();
        Filter.FilterEvent mockEvent2 = new FilterEventMock();
        Filter filter = new Filter(); filter.add(mockEvent1); filter.add(mockEvent2);

        // get the internal events list and make sure it's a copy of the original list
        List<Filter.FilterEvent> events = filter.getEventsInternal();

        Filter filter2 = FilterTest_testGetEventsInternal_GT.inputTransformation_testGetEventsInternal(filter);

        assertNotSame(events, filter2.getEventsInternal());
        assertArrayEquals(new Object[] { mockEvent1, mockEvent2 }, events.toArray());
    }


    static class FilterEventMock implements Filter.FilterEvent {

        @Override
        public Object getJsonEventObject() {
            return "MockObject";
        }
    }
}