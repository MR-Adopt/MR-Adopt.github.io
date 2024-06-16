/*
 * Copyright (c) 2007-present, Stephen Colebourne & Michael Nascimento Santos
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *  * Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 *
 *  * Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *
 *  * Neither the name of JSR-310 nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
package org.threeten.extra;

import org.threeten.extra.YearQuarter;
import org.threeten.extra.YearQuarter.*;

import static java.time.temporal.ChronoField.YEAR;
import static java.time.temporal.ChronoUnit.DAYS;
import static java.time.temporal.ChronoUnit.YEARS;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.threeten.extra.TemporalFields.DAY_OF_HALF;
import static org.threeten.extra.TemporalFields.HALF_OF_YEAR;
import static org.threeten.extra.TemporalFields.HALF_YEARS;

import java.time.DateTimeException;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.ResolverStyle;
import java.time.temporal.TemporalAccessor;
import java.time.temporal.TemporalField;
import java.time.temporal.ValueRange;
import java.util.HashMap;
import java.util.Map;

import java.util.List;
import java.util.Arrays;

import org.junit.jupiter.api.Test;

/**
 * Test TemporalFields.
 */
public class TestTemporalFields_test_HALF_YEARSTest {

    //-----------------------------------------------------------------------
    // DAY_OF_HALF
    //-----------------------------------------------------------------------
//     @Test
//     public void test_HALF_YEARS_h() {
//         int year1 = 2023;
//         int quarter1 = 4;
//         int year2 = 2023;
//         int quarter2 = 2;
//         int amount = 1;
// 
//         assertEquals(YearQuarter.of(year1, quarter1), HALF_YEARS.addTo(YearQuarter.of(year2, quarter2), amount));
// 
// 
//         assertEquals(true, HALF_YEARS.isDateBased());
//         assertEquals(false, HALF_YEARS.isTimeBased());
//         assertEquals("HalfYears", HALF_YEARS.toString());
// 
//         assertEquals(true, HALF_YEARS.isSupportedBy(LocalDate.of(2023, 6, 30)));
//         assertEquals(true, HALF_YEARS.isSupportedBy(YearQuarter.of(2023, 2)));
//         assertEquals(true, HALF_YEARS.isSupportedBy(YearMonth.of(2023, 6)));
// 
//         assertEquals(LocalDate.of(2023, 12, 30), HALF_YEARS.addTo(LocalDate.of(2023, 6, 30), 1));
// 
//         assertEquals(YearMonth.of(2023, 12), HALF_YEARS.addTo(YearMonth.of(2023, 6), 1));
// 
//         assertEquals(0, HALF_YEARS.between(LocalDate.of(2023, 6, 30), LocalDate.of(2023, 12, 29)));
//         assertEquals(1, HALF_YEARS.between(LocalDate.of(2023, 6, 30), LocalDate.of(2023, 12, 30)));
// 
//         assertEquals(0, HALF_YEARS.between(YearQuarter.of(2023, 2), YearQuarter.of(2023, 3)));
//         assertEquals(1, HALF_YEARS.between(YearQuarter.of(2023, 2), YearQuarter.of(2023, 4)));
// 
//         assertEquals(0, HALF_YEARS.between(YearMonth.of(2023, 2), YearMonth.of(2023, 7)));
//         assertEquals(1, HALF_YEARS.between(YearMonth.of(2023, 2), YearMonth.of(2023, 8)));
//     }
// 
// //     public static List<Object> inputTransformation_test_HALF_YEARS(int year1, int quarter1) {
// //         int year2 = year1;  // Assume same year for simplicity
// //         int quarter2;       // To be determined
// //         int amount;         // To be determined
// // 
// //         if (quarter1 % 2 == 0) {
// //             quarter2 = quarter1 - 2;  // Move back two quarters within the same year
// //             amount = 1;               // One half-year back
// //         } else {
// //             quarter2 = quarter1 - 1;  // Move back one quarter (odd quarters are trickier)
// //             amount = 1;               // Still one half-year, but this is more of a placeholder
// //         }
// // 
// //         // Adjust for year wrapping
// //         if (quarter2 <= 0) {
// //             year2 -= 1;               // Move to the previous year
// //             quarter2 += 4;            // Adjust the quarter correctly (4 quarters in a year)
// //         }
// // 
// // 		List<Object> transformed_inputs = Arrays.asList(year2, quarter2, amount);
// // 		return transformed_inputs;
// // 	}
// // 
    @Test
    public void test_HALF_YEARS_IT() {
        int year1 = 2023;
        int quarter1 = 4;
        
        List<Object> transformed_inputs = TestTemporalFields_test_HALF_YEARS.inputTransformation_test_HALF_YEARS(year1, quarter1);
        int year2 = (int) transformed_inputs.get(0);
        int quarter2 = (int) transformed_inputs.get(1);
        int amount = (int) transformed_inputs.get(2);

        assertEquals(YearQuarter.of(year1, quarter1), HALF_YEARS.addTo(YearQuarter.of(year2, quarter2), amount));

        assertEquals(true, HALF_YEARS.isDateBased());
        assertEquals(false, HALF_YEARS.isTimeBased());
        assertEquals("HalfYears", HALF_YEARS.toString());

        assertEquals(true, HALF_YEARS.isSupportedBy(LocalDate.of(2023, 6, 30)));
        assertEquals(true, HALF_YEARS.isSupportedBy(YearQuarter.of(2023, 2)));
        assertEquals(true, HALF_YEARS.isSupportedBy(YearMonth.of(2023, 6)));

        assertEquals(LocalDate.of(2023, 12, 30), HALF_YEARS.addTo(LocalDate.of(2023, 6, 30), 1));

        assertEquals(YearMonth.of(2023, 12), HALF_YEARS.addTo(YearMonth.of(2023, 6), 1));

        assertEquals(0, HALF_YEARS.between(LocalDate.of(2023, 6, 30), LocalDate.of(2023, 12, 29)));
        assertEquals(1, HALF_YEARS.between(LocalDate.of(2023, 6, 30), LocalDate.of(2023, 12, 30)));

        assertEquals(0, HALF_YEARS.between(YearQuarter.of(2023, 2), YearQuarter.of(2023, 3)));
        assertEquals(1, HALF_YEARS.between(YearQuarter.of(2023, 2), YearQuarter.of(2023, 4)));

        assertEquals(0, HALF_YEARS.between(YearMonth.of(2023, 2), YearMonth.of(2023, 7)));
        assertEquals(1, HALF_YEARS.between(YearMonth.of(2023, 2), YearMonth.of(2023, 8)));
    }


    //-------------------------------------------------------------------------
}