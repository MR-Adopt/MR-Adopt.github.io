package org.threeten.extra;

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
import org.junit.jupiter.api.Test;


import org.threeten.extra.YearQuarter;
import org.threeten.extra.YearQuarter.*;
import java.util.List;
import java.util.Arrays;

public class TestTemporalFields_test_HALF_YEARS {
    public static List<Object> inputTransformation_test_HALF_YEARS(int year1, int quarter1)  {
        int year2 = year1;
        int quarter2 = quarter1 - 2;
        int amount = 1;
        List<Object> transformed_inputs = Arrays.asList(year2, quarter2, amount);
        return transformed_inputs;
    }
}