package com.cedarsoftware.util.convert;

import com.cedarsoftware.util.convert.ConverterTest_testSqlDateToString;

import com.cedarsoftware.util.convert.Converter;
import com.cedarsoftware.util.convert.Converter.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.sql.Timestamp;
import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collection;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TimeZone;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Stream;
import com.cedarsoftware.util.DeepEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.EmptySource;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.NullAndEmptySource;
import org.junit.jupiter.params.provider.NullSource;
import static com.cedarsoftware.util.ArrayUtilities.EMPTY_BYTE_ARRAY;
import static com.cedarsoftware.util.ArrayUtilities.EMPTY_CHAR_ARRAY;
import static com.cedarsoftware.util.Converter.zonedDateTimeToMillis;
import static com.cedarsoftware.util.StringUtilities.EMPTY;
// import static com.cedarsoftware.util.convert.ConverterTest_testSqlDateToString_h2Test4.fubar.bar;
// import static com.cedarsoftware.util.convert.ConverterTest_testSqlDateToString_h2Test4.fubar.foo;
import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatExceptionOfType;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

/**
 * @author John DeRegnaucourt (jdereg@gmail.com) & Ken Partlow
 *         <br>
 *         Copyright (c) Cedar Software LLC
 *         <br><br>
 *         Licensed under the Apache License, Version 2.0 (the "License");
 *         you may not use this file except in compliance with the License.
 *         You may obtain a copy of the License at
 *         <br><br>
 *         http://www.apache.org/licenses/LICENSE-2.0
 *         <br><br>
 *         Unless required by applicable law or agreed to in writing, software
 *         distributed under the License is distributed on an "AS IS" BASIS,
 *         WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *         See the License for the specific language governing permissions and
 *         limitations under the License.
 */
class ConverterTest_testSqlDateToString_h2Test4_valid {

    public static final LocalDateTime LDT_2023_TOKYO = LocalDateTime.of(2023, 6, 25, 0, 57, 29, 729000000);

    public static final LocalDateTime LDT_2023_PARIS = LocalDateTime.of(2023, 6, 24, 17, 57, 29, 729000000);

    public static final LocalDateTime LDT_2023_GMT = LocalDateTime.of(2023, 6, 24, 15, 57, 29, 729000000);

    public static final LocalDateTime LDT_2023_NY = LocalDateTime.of(2023, 6, 24, 11, 57, 29, 729000000);

    public static final LocalDateTime LDT_2023_CHICAGO = LocalDateTime.of(2023, 6, 24, 10, 57, 29, 729000000);

    public static final LocalDateTime LDT_2023_LA = LocalDateTime.of(2023, 6, 24, 8, 57, 29, 729000000);

    public static final LocalDateTime LDT_MILLENNIUM_TOKYO = LocalDateTime.of(2000, 1, 1, 13, 59, 59, 959000000);

    public static final LocalDateTime LDT_MILLENNIUM_PARIS = LocalDateTime.of(2000, 1, 1, 5, 59, 59, 959000000);

    public static final LocalDateTime LDT_MILLENNIUM_GMT = LocalDateTime.of(2000, 1, 1, 4, 59, 59, 959000000);

    public static final LocalDateTime LDT_MILLENNIUM_NY = LocalDateTime.of(1999, 12, 31, 23, 59, 59, 959000000);

    public static final LocalDateTime LDT_MILLENNIUM_CHICAGO = LocalDateTime.of(1999, 12, 31, 22, 59, 59, 959000000);

    public static final LocalDateTime LDT_MILLENNIUM_LA = LocalDateTime.of(1999, 12, 31, 20, 59, 59, 959000000);

    Converter converter;

    public static final LocalDate LD_MILLINNIUM_NY = LocalDate.of(1999, 12, 31);

    public static final LocalDate LD_MILLINNIUM_TOKYO = LocalDate.of(2000, 1, 1);

    public static final LocalDate LD_MILLENNIUM_CHICAGO = LocalDate.of(1999, 12, 31);

    public static final ZoneId TOKYO = ZoneId.of("Asia/Tokyo");

    public static final ZoneId PARIS = ZoneId.of("Europe/Paris");

    public static final ZoneId CHICAGO = ZoneId.of("America/Chicago");

    public static final ZoneId NEW_YORK = ZoneId.of("America/New_York");

    public static final ZoneId LOS_ANGELES = ZoneId.of("America/Los_Angeles");

    public static final ZoneId GMT = ZoneId.of("GMT");

    enum fubar {

        foo, bar, baz, quz
    }

    @BeforeEach
    public void before() {
        // create converter with default options
        this.converter = new Converter(new DefaultConverterOptions());
    }

    public static <T extends Number> Stream<Arguments> paramsForIntegerTypes(T min, T max) {
        List<Arguments> arguments = new ArrayList(20);
        arguments.add(Arguments.of("3.159", 3));
        arguments.add(Arguments.of("3.519", 3));
        arguments.add(Arguments.of("-3.159", -3));
        arguments.add(Arguments.of("-3.519", -3));
        arguments.add(Arguments.of("" + min, min));
        arguments.add(Arguments.of("" + max, max));
        arguments.add(Arguments.of("" + min + ".25", min));
        arguments.add(Arguments.of("" + max + ".75", max));
        arguments.add(Arguments.of((byte) -3, -3));
        arguments.add(Arguments.of((byte) 3, 3));
        arguments.add(Arguments.of((short) -9, -9));
        arguments.add(Arguments.of((short) 9, 9));
        arguments.add(Arguments.of(-13, -13));
        arguments.add(Arguments.of(13, 13));
        arguments.add(Arguments.of(-7L, -7));
        arguments.add(Arguments.of(7L, 7));
        arguments.add(Arguments.of(-11.0d, -11));
        arguments.add(Arguments.of(11.0d, 11));
        arguments.add(Arguments.of(3.14f, 3));
        arguments.add(Arguments.of(3.59f, 3));
        arguments.add(Arguments.of(-3.14f, -3));
        arguments.add(Arguments.of(-3.59f, -3));
        arguments.add(Arguments.of(3.14d, 3));
        arguments.add(Arguments.of(3.59d, 3));
        arguments.add(Arguments.of(-3.14d, -3));
        arguments.add(Arguments.of(-3.59d, -3));
        arguments.add(Arguments.of(new AtomicInteger(0), 0));
        arguments.add(Arguments.of(new AtomicLong(9), 9));
        arguments.add(Arguments.of(BigInteger.valueOf(13), 13));
        arguments.add(Arguments.of(BigDecimal.valueOf(23), 23));
        return arguments.stream();
    }

    public static <T extends Number> Stream<Arguments> paramsForFloatingPointTypes(T min, T max) {
        List<Arguments> arguments = new ArrayList(20);
        arguments.add(Arguments.of("3.159", 3.159d));
        arguments.add(Arguments.of("3.519", 3.519d));
        arguments.add(Arguments.of("-3.159", -3.159d));
        arguments.add(Arguments.of("-3.519", -3.519d));
        arguments.add(Arguments.of("" + min, min));
        arguments.add(Arguments.of("" + max, max));
        arguments.add(Arguments.of(min.doubleValue() + .25, min.doubleValue() + .25d));
        arguments.add(Arguments.of(max.doubleValue() - .75, max.doubleValue() - .75d));
        arguments.add(Arguments.of((byte) -3, -3));
        arguments.add(Arguments.of((byte) 3, 3));
        arguments.add(Arguments.of((short) -9, -9));
        arguments.add(Arguments.of((short) 9, 9));
        arguments.add(Arguments.of(-13, -13));
        arguments.add(Arguments.of(13, 13));
        arguments.add(Arguments.of(-7L, -7));
        arguments.add(Arguments.of(7L, 7));
        arguments.add(Arguments.of(-11.0d, -11.0d));
        arguments.add(Arguments.of(11.0d, 11.0d));
        arguments.add(Arguments.of(3.0f, 3.0d));
        arguments.add(Arguments.of(-5.0f, -5.0d));
        arguments.add(Arguments.of(-3.14d, -3.14d));
        arguments.add(Arguments.of(-3.59d, -3.59d));
        arguments.add(Arguments.of(new AtomicInteger(0), 0));
        arguments.add(Arguments.of(new AtomicLong(9), 9));
        arguments.add(Arguments.of(BigInteger.valueOf(13), 13));
        arguments.add(Arguments.of(BigDecimal.valueOf(23), 23));
        return arguments.stream();
    }

    public static Stream<Arguments> toByteParams() {
        return paramsForIntegerTypes(Byte.MIN_VALUE, Byte.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("toByteParams")
    void toByte(Object source, Number number) {
        byte expected = number.byteValue();
        Byte converted = this.converter.convert(source, Byte.class);
        assertThat(converted).isEqualTo((byte) expected);
    }

    @ParameterizedTest
    @MethodSource("toByteParams")
    void toByteUsingPrimitive(Object source, Number number) {
        byte expected = number.byteValue();
        byte converted = this.converter.convert(source, byte.class);
        assertThat(converted).isEqualTo(expected);
    }

    public static Stream<Arguments> toByte_booleanParams() {
        return Stream.of(Arguments.of(true, CommonValues.BYTE_ONE), Arguments.of(false, CommonValues.BYTE_ZERO), Arguments.of(Boolean.TRUE, CommonValues.BYTE_ONE), Arguments.of(Boolean.FALSE, CommonValues.BYTE_ZERO), Arguments.of(new AtomicBoolean(true), CommonValues.BYTE_ONE), Arguments.of(new AtomicBoolean(false), CommonValues.BYTE_ZERO));
    }

    @ParameterizedTest
    @MethodSource("toByte_booleanParams")
    void toByte_fromBoolean_isSameAsCommonValueObject(Object value, Byte expectedResult) {
        Byte converted = this.converter.convert(value, Byte.class);
        assertThat(converted).isSameAs(expectedResult);
    }

    @ParameterizedTest
    @MethodSource("toByte_booleanParams")
    void toByte_fromBoolean_usingPrimitive_isSameAsCommonValueObject(Object value, Byte expectedResult) {
        byte converted = this.converter.convert(value, byte.class);
        assertThat(converted).isSameAs(expectedResult);
    }

    public static Stream<Arguments> toByte_illegalArguments() {
        return Stream.of(Arguments.of("45badNumber", "not parseable as a byte"), Arguments.of("-129", "not parseable as a byte"), Arguments.of("128", "not parseable as a byte"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("toByte_illegalArguments")
    void toByte_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, byte.class)).withMessageContaining(partialMessage);
    }

    @ParameterizedTest
    @NullAndEmptySource
    void toByte_whenNullOrEmpty_andCovnertingToPrimitive_returnsZero(String s) {
        byte converted = this.converter.convert(s, byte.class);
        assertThat(converted).isZero();
    }

    @ParameterizedTest
    @NullSource
    void toByte_whenNull_andNotPrimitive_returnsNull(String s) {
        Byte converted = this.converter.convert(s, Byte.class);
        assertThat(converted).isNull();
    }

    @ParameterizedTest
    @EmptySource
    void toByte_whenEmpty_andNotPrimitive_returnsZero(String s) {
        Byte converted = this.converter.convert(s, Byte.class);
        assertThat(converted).isZero();
    }

    public static Stream<Arguments> toShortParams() {
        return paramsForIntegerTypes(Short.MIN_VALUE, Short.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("toShortParams")
    void toShort(Object value, Number number) {
        short expected = number.shortValue();
        Short converted = this.converter.convert(value, Short.class);
        assertThat(converted).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("toShortParams")
    void toShort_usingPrimitiveClass(Object value, Number number) {
        short expected = number.shortValue();
        short converted = this.converter.convert(value, short.class);
        assertThat(converted).isEqualTo(expected);
    }

    public static Stream<Arguments> toShort_withBooleanPrams() {
        return Stream.of(Arguments.of(true, CommonValues.SHORT_ONE), Arguments.of(false, CommonValues.SHORT_ZERO), Arguments.of(Boolean.TRUE, CommonValues.SHORT_ONE), Arguments.of(Boolean.FALSE, CommonValues.SHORT_ZERO), Arguments.of(new AtomicBoolean(true), CommonValues.SHORT_ONE), Arguments.of(new AtomicBoolean(false), CommonValues.SHORT_ZERO));
    }

    @ParameterizedTest
    @MethodSource("toShort_withBooleanPrams")
    void toShort_withBooleanPrams_returnsCommonValue(Object value, Short expectedResult) {
        Short converted = this.converter.convert(value, Short.class);
        assertThat(converted).isSameAs(expectedResult);
    }

    @ParameterizedTest
    @MethodSource("toShort_withBooleanPrams")
    void toShort_withBooleanPrams_usingPrimitive_returnsCommonValue(Object value, Short expectedResult) {
        short converted = this.converter.convert(value, short.class);
        assertThat(converted).isSameAs(expectedResult);
    }

    public static Stream<Arguments> toShortParams_withIllegalArguments() {
        return Stream.of(Arguments.of("45badNumber", "not parseable as a short value or outside -32768 to 32767"), Arguments.of("-32769", "not parseable as a short value or outside -32768 to 32767"), Arguments.of("32768", "not parseable as a short value or outside -32768 to 32767"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("toShortParams_withIllegalArguments")
    void toShort_withIllegalArguments_throwsException(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, short.class)).withMessageContaining(partialMessage);
    }

    @ParameterizedTest
    @NullAndEmptySource
    void toShort_usingPrimitive_withNullAndEmptySource_returnsZero(String s) {
        short converted = this.converter.convert(s, short.class);
        assertThat(converted).isZero();
    }

    @ParameterizedTest
    @NullSource
    void toShort_whenNotPrimitive_whenNull_returnsNull(String s) {
        Short converted = this.converter.convert(s, Short.class);
        assertThat(converted).isNull();
    }

    @ParameterizedTest
    @EmptySource
    void toShort_whenNotPrimitive_whenEmptyString_returnsNull(String s) {
        Short converted = this.converter.convert(s, Short.class);
        assertThat(converted).isZero();
    }

    public static Stream<Arguments> toIntParams() {
        return paramsForIntegerTypes(Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("toIntParams")
    void toInt(Object value, Integer expectedResult) {
        Integer converted = this.converter.convert(value, Integer.class);
        assertThat(converted).isEqualTo(expectedResult);
    }

    @ParameterizedTest
    @MethodSource("toIntParams")
    void toInt_usingPrimitives(Object value, int expectedResult) {
        int converted = this.converter.convert(value, int.class);
        assertThat(converted).isEqualTo(expectedResult);
    }

    public static Stream<Arguments> toInt_booleanParams() {
        return Stream.of(Arguments.of(true, CommonValues.INTEGER_ONE), Arguments.of(false, CommonValues.INTEGER_ZERO), Arguments.of(Boolean.TRUE, CommonValues.INTEGER_ONE), Arguments.of(Boolean.FALSE, CommonValues.INTEGER_ZERO), Arguments.of(new AtomicBoolean(true), CommonValues.INTEGER_ONE), Arguments.of(new AtomicBoolean(false), CommonValues.INTEGER_ZERO));
    }

    @ParameterizedTest
    @MethodSource("toInt_booleanParams")
    void toInt_fromBoolean_returnsCommonValue(Object value, Integer expectedResult) {
        Integer converted = this.converter.convert(value, Integer.class);
        assertThat(converted).isSameAs(expectedResult);
    }

    public static Stream<Arguments> toInt_illegalArguments() {
        return Stream.of(Arguments.of("45badNumber", "not parseable as an int value or outside -2147483648 to 2147483647"), Arguments.of("9999999999", "not parseable as an int value or outside -2147483648 to 2147483647"), Arguments.of("12147483648", "not parseable as an int value or outside -2147483648 to 2147483647"), Arguments.of("2147483649", "not parseable as an int value or outside -2147483648 to 2147483647"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("toInt_illegalArguments")
    void toInt_withIllegalArguments_throwsException(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, Integer.class)).withMessageContaining(partialMessage);
    }

    @ParameterizedTest
    @NullAndEmptySource
    void toInt_usingPrimitive_whenEmptyOrNullString_returnsZero(String s) {
        int converted = this.converter.convert(s, int.class);
        assertThat(converted).isZero();
    }

    @ParameterizedTest
    @NullSource
    void toInt_whenNotPrimitive_andNullString_returnsNull(String s) {
        Integer converted = this.converter.convert(s, Integer.class);
        assertThat(converted).isNull();
    }

    @ParameterizedTest
    @EmptySource
    void toInt_whenNotPrimitive_andEmptyString_returnsZero(String s) {
        Integer converted = this.converter.convert(s, Integer.class);
        assertThat(converted).isZero();
    }

    public static Stream<Arguments> toLongParams() {
        return paramsForIntegerTypes(Long.MIN_VALUE, Long.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("toLongParams")
    void toLong(Object value, Number number) {
        Long expected = number.longValue();
        Long converted = this.converter.convert(value, Long.class);
        assertThat(converted).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("toLongParams")
    void toLong_usingPrimitives(Object value, Number number) {
        long expected = number.longValue();
        long converted = this.converter.convert(value, long.class);
        assertThat(converted).isEqualTo(expected);
    }

    public static Stream<Arguments> toLong_booleanParams() {
        return Stream.of(Arguments.of(true, CommonValues.LONG_ONE), Arguments.of(false, CommonValues.LONG_ZERO), Arguments.of(Boolean.TRUE, CommonValues.LONG_ONE), Arguments.of(Boolean.FALSE, CommonValues.LONG_ZERO), Arguments.of(new AtomicBoolean(true), CommonValues.LONG_ONE), Arguments.of(new AtomicBoolean(false), CommonValues.LONG_ZERO));
    }

    @ParameterizedTest
    @MethodSource("toLong_booleanParams")
    void toLong_withBooleanParams_returnsCommonValues(Object value, Long expectedResult) {
        Long converted = this.converter.convert(value, Long.class);
        assertThat(converted).isSameAs(expectedResult);
    }

    @ParameterizedTest
    @NullAndEmptySource
    void toLong_whenPrimitive_andNullOrEmpty_returnsZero(String s) {
        long converted = this.converter.convert(s, long.class);
        assertThat(converted).isZero();
    }

    @ParameterizedTest
    @NullSource
    void toLong_whenNotPrimitive_andNull_returnsNull(String s) {
        Long converted = this.converter.convert(s, Long.class);
        assertThat(converted).isNull();
    }

    @ParameterizedTest
    @EmptySource
    void toLong_whenNotPrimitive_andEmptyString_returnsZero(String s) {
        Long converted = this.converter.convert(s, Long.class);
        assertThat(converted).isZero();
    }

    public static Stream<Arguments> toLongWithIllegalParams() {
        return Stream.of(Arguments.of("45badNumber", "not parseable as a long value or outside -9223372036854775808 to 9223372036854775807"), Arguments.of("-9223372036854775809", "not parseable as a long value or outside -9223372036854775808 to 9223372036854775807"), Arguments.of("9223372036854775808", "not parseable as a long value or outside -9223372036854775808 to 9223372036854775807"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("toLongWithIllegalParams")
    void testLong_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, Long.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> testAtomicLongParams() {
        return Stream.of(Arguments.of("-32768", new AtomicLong(-32768L)), Arguments.of("32767", new AtomicLong(32767L)), Arguments.of(Byte.MIN_VALUE, new AtomicLong(-128L)), Arguments.of(Byte.MAX_VALUE, new AtomicLong(127L)), Arguments.of(Short.MIN_VALUE, new AtomicLong(-32768L)), Arguments.of(Short.MAX_VALUE, new AtomicLong(32767L)), Arguments.of(Integer.MIN_VALUE, new AtomicLong(-2147483648L)), Arguments.of(Integer.MAX_VALUE, new AtomicLong(2147483647L)), Arguments.of(Long.MIN_VALUE, new AtomicLong(-9223372036854775808L)), Arguments.of(Long.MAX_VALUE, new AtomicLong(9223372036854775807L)), Arguments.of(-128.0f, new AtomicLong(-128L)), Arguments.of(127.0f, new AtomicLong(127L)), Arguments.of(-128.0d, new AtomicLong(-128L)), Arguments.of(127.0d, new AtomicLong(127L)), Arguments.of(new BigDecimal("100"), new AtomicLong(100L)), Arguments.of(new BigInteger("120"), new AtomicLong(120L)), Arguments.of(new AtomicInteger(25), new AtomicLong(25L)), Arguments.of(new AtomicLong(100L), new AtomicLong(100L)));
    }

    @ParameterizedTest
    @MethodSource("testAtomicLongParams")
    void testAtomicLong(Object value, AtomicLong expectedResult) {
        AtomicLong converted = this.converter.convert(value, AtomicLong.class);
        assertThat(converted.get()).isEqualTo(expectedResult.get());
    }

    public static Stream<Arguments> testAtomicLong_fromBooleanParams() {
        return Stream.of(Arguments.of(true, new AtomicLong(CommonValues.LONG_ONE)), Arguments.of(false, new AtomicLong(CommonValues.LONG_ZERO)), Arguments.of(Boolean.TRUE, new AtomicLong(CommonValues.LONG_ONE)), Arguments.of(Boolean.FALSE, new AtomicLong(CommonValues.LONG_ZERO)), Arguments.of(new AtomicBoolean(true), new AtomicLong(CommonValues.LONG_ONE)), Arguments.of(new AtomicBoolean(false), new AtomicLong(CommonValues.LONG_ZERO)));
    }

    @ParameterizedTest
    @MethodSource("testAtomicLong_fromBooleanParams")
    void testAtomicLong_fromBoolean(Object value, AtomicLong expectedResult) {
        AtomicLong converted = this.converter.convert(value, AtomicLong.class);
        assertThat(converted.get()).isEqualTo(expectedResult.get());
    }

    @ParameterizedTest
    @NullSource
    void testConvertToAtomicLong_whenNullString(String s) {
        AtomicLong converted = this.converter.convert(s, AtomicLong.class);
        assertThat(converted).isNull();
    }

    @ParameterizedTest
    @EmptySource
    void testConvertToAtomicLong_whenEmptyString(String s) {
        AtomicLong converted = this.converter.convert(s, AtomicLong.class);
        assertThat(converted.get()).isZero();
    }

    public static Stream<Arguments> toBooleanParams_trueCases() {
        return Stream.of(Arguments.of("true"), Arguments.of("True"), Arguments.of("TRUE"), Arguments.of("T"), Arguments.of("t"), Arguments.of("1"), Arguments.of('T'), Arguments.of('t'), Arguments.of('1'), Arguments.of(Short.MIN_VALUE), Arguments.of(Short.MAX_VALUE), Arguments.of(Integer.MAX_VALUE), Arguments.of(Integer.MIN_VALUE), Arguments.of(Long.MIN_VALUE), Arguments.of(Long.MAX_VALUE), Arguments.of(Boolean.TRUE), Arguments.of(new BigInteger("8675309")), Arguments.of(new BigDecimal("59.99")), Arguments.of(Double.MIN_VALUE), Arguments.of(Double.MAX_VALUE), Arguments.of(Float.MIN_VALUE), Arguments.of(Float.MAX_VALUE), Arguments.of(-128.0d), Arguments.of(127.0d), Arguments.of(new AtomicInteger(75)), Arguments.of(new AtomicInteger(1)), Arguments.of(new AtomicInteger(Integer.MAX_VALUE)), Arguments.of(new AtomicLong(Long.MAX_VALUE)));
    }

    @ParameterizedTest
    @MethodSource("toBooleanParams_trueCases")
    void testToBoolean_trueCases(Object input) {
        assertThat(this.converter.convert(input, boolean.class)).isTrue();
    }

    public static Stream<Arguments> toBooleanParams_falseCases() {
        return Stream.of(Arguments.of("false"), Arguments.of("f"), Arguments.of("F"), Arguments.of("FALSE"), Arguments.of("9"), Arguments.of("0"), Arguments.of('F'), Arguments.of('f'), Arguments.of('0'), Arguments.of(Character.MAX_VALUE), Arguments.of((byte) 0), Arguments.of((short) 0), Arguments.of(0), Arguments.of(0L), Arguments.of(BigInteger.ZERO), Arguments.of(BigDecimal.ZERO), Arguments.of(0.0f), Arguments.of(0.0d), Arguments.of(new AtomicInteger(0)), Arguments.of(new AtomicLong(0)));
    }

    @ParameterizedTest
    @MethodSource("toBooleanParams_falseCases")
    void testToBoolean_falseCases(Object input) {
        assertThat(this.converter.convert(input, boolean.class)).isFalse();
    }

    public static Stream<Arguments> epochMilliWithZoneId() {
        return Stream.of(Arguments.of("946702799959", TOKYO), Arguments.of("946702799959", PARIS), Arguments.of("946702799959", GMT), Arguments.of("946702799959", NEW_YORK), Arguments.of("946702799959", CHICAGO), Arguments.of("946702799959", LOS_ANGELES));
    }

    public static Stream<Arguments> dateStringNoZoneOffset() {
        return Stream.of(Arguments.of("2000-01-01T13:59:59", TOKYO), Arguments.of("2000-01-01T05:59:59", PARIS), Arguments.of("2000-01-01T04:59:59", GMT), Arguments.of("1999-12-31T23:59:59", NEW_YORK), Arguments.of("1999-12-31T22:59:59", CHICAGO), Arguments.of("1999-12-31T20:59:59", LOS_ANGELES));
    }

    public static Stream<Arguments> dateStringInIsoOffsetDateTime() {
        return Stream.of(Arguments.of("2000-01-01T13:59:59+09:00"), Arguments.of("2000-01-01T05:59:59+01:00"), Arguments.of("2000-01-01T04:59:59Z"), Arguments.of("1999-12-31T23:59:59-05:00"), Arguments.of("1999-12-31T22:59:59-06:00"), Arguments.of("1999-12-31T20:59:59-08:00"));
    }

    public static Stream<Arguments> dateStringInIsoOffsetDateTimeWithMillis() {
        return Stream.of(Arguments.of("2000-01-01T13:59:59.959+09:00"), Arguments.of("2000-01-01T05:59:59.959+01:00"), Arguments.of("2000-01-01T04:59:59.959Z"), Arguments.of("1999-12-31T23:59:59.959-05:00"), Arguments.of("1999-12-31T22:59:59.959-06:00"), Arguments.of("1999-12-31T20:59:59.959-08:00"));
    }

    public static Stream<Arguments> dateStringInIsoZoneDateTime() {
        return Stream.of(Arguments.of("2000-01-01T13:59:59.959+09:00[Asia/Tokyo]"), Arguments.of("2000-01-01T05:59:59.959+01:00[Europe/Paris]"), Arguments.of("2000-01-01T04:59:59.959Z[GMT]"), Arguments.of("1999-12-31T23:59:59.959-05:00[America/New_York]"), Arguments.of("1999-12-31T22:59:59.959-06:00[America/Chicago]"), Arguments.of("1999-12-31T20:59:59.959-08:00[America/Los_Angeles]"));
    }

    @ParameterizedTest
    @MethodSource("epochMilliWithZoneId")
    void testEpochMilliWithZoneId(String epochMilli, ZoneId zoneId) {
        LocalDateTime localDateTime = this.converter.convert(epochMilli, LocalDateTime.class, createCustomZones(zoneId, NEW_YORK));
        assertThat(localDateTime).hasYear(1999).hasMonthValue(12).hasDayOfMonth(31).hasHour(23).hasMinute(59).hasSecond(59);
    }

    @ParameterizedTest
    @MethodSource("dateStringNoZoneOffset")
    void testStringDateWithNoTimeZoneInformation(String date, ZoneId zoneId) {
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(zoneId, NEW_YORK));
        assertThat(localDateTime).hasYear(1999).hasMonthValue(12).hasDayOfMonth(31).hasHour(23).hasMinute(59).hasSecond(59);
    }

    @ParameterizedTest
    @MethodSource("dateStringInIsoOffsetDateTime")
    void testStringDateWithTimeZoneToLocalDateTime(String date) {
        // source is TOKYO, should be ignored when zone is provided on string.
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(TOKYO, NEW_YORK));
        assertThat(localDateTime).hasYear(1999).hasMonthValue(12).hasDayOfMonth(31).hasHour(23).hasMinute(59).hasSecond(59);
    }

    @ParameterizedTest
    @MethodSource("dateStringInIsoOffsetDateTimeWithMillis")
    void testStringDateWithTimeZoneToLocalDateTimeIncludeMillis(String date) {
        // source is TOKYO, should be ignored when zone is provided on string.
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(TOKYO, NEW_YORK));
        assertThat(localDateTime).hasYear(1999).hasMonthValue(12).hasDayOfMonth(31).hasHour(23).hasMinute(59).hasSecond(59).hasNano(959 * 1_000_000);
    }

    @ParameterizedTest
    @MethodSource("dateStringInIsoZoneDateTime")
    void testStringDateWithTimeZoneToLocalDateTimeWithZone(String date) {
        // source is TOKYO, should be ignored when zone is provided on string.
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(TOKYO, NEW_YORK));
        assertThat(localDateTime).hasYear(1999).hasMonthValue(12).hasDayOfMonth(31).hasHour(23).hasMinute(59).hasSecond(59).hasNano(959 * 1_000_000);
    }

    public static Stream<Arguments> epochMillis_withLocalDateTimeInformation() {
        return Stream.of(Arguments.of(1687622249729L, TOKYO, LDT_2023_TOKYO), Arguments.of(1687622249729L, PARIS, LDT_2023_PARIS), Arguments.of(1687622249729L, GMT, LDT_2023_GMT), Arguments.of(1687622249729L, NEW_YORK, LDT_2023_NY), Arguments.of(1687622249729L, CHICAGO, LDT_2023_CHICAGO), Arguments.of(1687622249729L, LOS_ANGELES, LDT_2023_LA), Arguments.of(946702799959L, TOKYO, LDT_MILLENNIUM_TOKYO), Arguments.of(946702799959L, PARIS, LDT_MILLENNIUM_PARIS), Arguments.of(946702799959L, GMT, LDT_MILLENNIUM_GMT), Arguments.of(946702799959L, NEW_YORK, LDT_MILLENNIUM_NY), Arguments.of(946702799959L, CHICAGO, LDT_MILLENNIUM_CHICAGO), Arguments.of(946702799959L, LOS_ANGELES, LDT_MILLENNIUM_LA));
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        System.out.println(Instant.ofEpochMilli(epochMilli).atZone(zoneId).toOffsetDateTime());
        LocalDateTime localDateTime = this.converter.convert(calendar, LocalDateTime.class, createCustomZones(zoneId, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToLocalDateTime_whenCalendarTimeZoneMatches(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone(zoneId));
        calendar.setTimeInMillis(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(calendar, LocalDateTime.class, createCustomZones(zoneId, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToLocalDateTime_whenCalendarTimeZoneDoesNotMatch(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone(NEW_YORK));
        calendar.setTimeInMillis(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(calendar, LocalDateTime.class, createCustomZones(NEW_YORK, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendar_roundTrip(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone(zoneId));
        calendar.setTimeInMillis(epochMilli);
        assertThat(calendar.get(Calendar.YEAR)).isEqualTo(expected.getYear());
        assertThat(calendar.get(Calendar.MONTH)).isEqualTo(expected.getMonthValue() - 1);
        assertThat(calendar.get(Calendar.DAY_OF_MONTH)).isEqualTo(expected.getDayOfMonth());
        assertThat(calendar.get(Calendar.HOUR_OF_DAY)).isEqualTo(expected.getHour());
        assertThat(calendar.get(Calendar.MINUTE)).isEqualTo(expected.getMinute());
        assertThat(calendar.get(Calendar.SECOND)).isEqualTo(expected.getSecond());
        assertThat(calendar.getTimeInMillis()).isEqualTo(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(calendar, LocalDateTime.class, createCustomZones(zoneId, TOKYO));
        Calendar actual = this.converter.convert(localDateTime, Calendar.class, createCustomZones(TOKYO, zoneId));
        assertThat(actual.get(Calendar.YEAR)).isEqualTo(expected.getYear());
        assertThat(actual.get(Calendar.MONTH)).isEqualTo(expected.getMonthValue() - 1);
        assertThat(actual.get(Calendar.DAY_OF_MONTH)).isEqualTo(expected.getDayOfMonth());
        assertThat(actual.get(Calendar.HOUR_OF_DAY)).isEqualTo(expected.getHour());
        assertThat(actual.get(Calendar.MINUTE)).isEqualTo(expected.getMinute());
        assertThat(actual.get(Calendar.SECOND)).isEqualTo(expected.getSecond());
        assertThat(actual.getTimeInMillis()).isEqualTo(epochMilli);
    }

    public static Stream<Arguments> roundTrip_tokyoTime() {
        return Stream.of(Arguments.of(946652400000L, TOKYO, LD_MILLINNIUM_TOKYO), Arguments.of(946652400000L, NEW_YORK, LD_MILLINNIUM_NY), Arguments.of(946652400000L, CHICAGO, LD_MILLENNIUM_CHICAGO));
    }

    @ParameterizedTest
    @MethodSource("roundTrip_tokyoTime")
    void testCalendar_roundTrip_withLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone(zoneId));
        calendar.setTimeInMillis(epochMilli);
        assertThat(calendar.get(Calendar.YEAR)).isEqualTo(expected.getYear());
        assertThat(calendar.get(Calendar.MONTH)).isEqualTo(expected.getMonthValue() - 1);
        assertThat(calendar.get(Calendar.DAY_OF_MONTH)).isEqualTo(expected.getDayOfMonth());
        assertThat(calendar.getTimeInMillis()).isEqualTo(epochMilli);
        LocalDate localDate = this.converter.convert(calendar, LocalDate.class, createCustomZones(zoneId, TOKYO));
        Calendar actual = this.converter.convert(localDate, Calendar.class, createCustomZones(TOKYO, zoneId));
        assertThat(actual.get(Calendar.YEAR)).isEqualTo(expected.getYear());
        assertThat(actual.get(Calendar.MONTH)).isEqualTo(expected.getMonthValue() - 1);
        assertThat(actual.get(Calendar.DAY_OF_MONTH)).isEqualTo(expected.getDayOfMonth());
        assertThat(actual.getTimeInMillis()).isEqualTo(epochMilli);
    }

    public static Stream<Arguments> localDateToLong() {
        return Stream.of(Arguments.of(946616400000L, NEW_YORK, LD_MILLINNIUM_NY, TOKYO), Arguments.of(946616400000L, NEW_YORK, LD_MILLINNIUM_NY, CHICAGO), Arguments.of(946620000000L, CHICAGO, LD_MILLENNIUM_CHICAGO, TOKYO));
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testConvertLocalDateToLongAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        long intermediate = this.converter.convert(expected, long.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToInstantAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        Instant intermediate = this.converter.convert(expected, Instant.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.toEpochMilli()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToDoubleAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        double intermediate = this.converter.convert(expected, double.class, createCustomZones(zoneId, targetZone));
        assertThat((long) intermediate).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToAtomicLongAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        AtomicLong intermediate = this.converter.convert(expected, AtomicLong.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.get()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToDateAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        Date intermediate = this.converter.convert(expected, Date.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.getTime()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateSqlDateAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        java.sql.Date intermediate = this.converter.convert(expected, java.sql.Date.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.getTime()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateTimestampAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        Timestamp intermediate = this.converter.convert(expected, Timestamp.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.getTime()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateZonedDateTimeAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        ZonedDateTime intermediate = this.converter.convert(expected, ZonedDateTime.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.toInstant().toEpochMilli()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToLocalDateTimeAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        LocalDateTime intermediate = this.converter.convert(expected, LocalDateTime.class, createCustomZones(zoneId, targetZone));
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToBigIntegerAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        BigInteger intermediate = this.converter.convert(expected, BigInteger.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.longValue()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToBigDecimalAndBack(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        BigDecimal intermediate = this.converter.convert(expected, BigDecimal.class, createCustomZones(zoneId, targetZone));
        assertThat(intermediate.longValue()).isEqualTo(epochMilli);
        LocalDate actual = this.converter.convert(intermediate, LocalDate.class, createCustomZones(targetZone, zoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateToLong")
    void testLocalDateToLocalTime(long epochMilli, ZoneId zoneId, LocalDate expected, ZoneId targetZone) {
        float intermediate = this.converter.convert(expected, float.class, createCustomZones(zoneId, targetZone));
        assertThat((long) intermediate).isNotEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testZonedDateTimeToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        ZonedDateTime time = Instant.ofEpochMilli(epochMilli).atZone(zoneId);
        LocalDateTime localDateTime = this.converter.convert(time, LocalDateTime.class, createCustomZones(zoneId, zoneId));
        assertThat(time.toInstant().toEpochMilli()).isEqualTo(epochMilli);
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testZonedDateTimeToLocalTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        ZonedDateTime time = Instant.ofEpochMilli(epochMilli).atZone(zoneId);
        LocalTime actual = this.converter.convert(time, LocalTime.class, createCustomZones(zoneId, zoneId));
        assertThat(actual).isEqualTo(expected.toLocalTime());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testZonedDateTimeToLocalDate(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        ZonedDateTime time = Instant.ofEpochMilli(epochMilli).atZone(zoneId);
        LocalDate actual = this.converter.convert(time, LocalDate.class, createCustomZones(zoneId, zoneId));
        assertThat(actual).isEqualTo(expected.toLocalDate());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testZonedDateTimeToInstant(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        ZonedDateTime time = Instant.ofEpochMilli(epochMilli).atZone(zoneId);
        Instant actual = this.converter.convert(time, Instant.class, createCustomZones(zoneId, zoneId));
        assertThat(actual).isEqualTo(time.toInstant());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testZonedDateTimeToCalendar(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        ZonedDateTime time = Instant.ofEpochMilli(epochMilli).atZone(zoneId);
        Calendar actual = this.converter.convert(time, Calendar.class, createCustomZones(zoneId, zoneId));
        assertThat(actual.getTime().getTime()).isEqualTo(time.toInstant().toEpochMilli());
        assertThat(actual.getTimeZone()).isEqualTo(TimeZone.getTimeZone(zoneId));
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testZonedDateTimeToLong(long epochMilli, ZoneId zoneId, LocalDateTime localDateTime) {
        ZonedDateTime time = ZonedDateTime.of(localDateTime, zoneId);
        long instant = this.converter.convert(time, long.class, createCustomZones(zoneId, zoneId));
        assertThat(instant).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testLongToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        LocalDateTime localDateTime = this.converter.convert(epochMilli, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testAtomicLongToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        AtomicLong time = new AtomicLong(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(time, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testLongToInstant(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant actual = this.converter.convert(epochMilli, Instant.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(Instant.ofEpochMilli(epochMilli));
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testBigIntegerToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        BigInteger bi = BigInteger.valueOf(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(bi, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testBigDecimalToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        BigDecimal bd = BigDecimal.valueOf(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(bd, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(instant, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testDateToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Date date = new Date(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testDateToZonedDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Date date = new Date(epochMilli);
        ZonedDateTime zonedDateTime = this.converter.convert(date, ZonedDateTime.class, createCustomZones(null, zoneId));
        assertThat(zonedDateTime.toLocalDateTime()).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToZonedDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant date = Instant.ofEpochMilli(epochMilli);
        ZonedDateTime zonedDateTime = this.converter.convert(date, ZonedDateTime.class, createCustomZones(null, zoneId));
        assertThat(zonedDateTime.toInstant()).isEqualTo(date);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testDateToInstant(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Date date = new Date(epochMilli);
        Instant actual = this.converter.convert(date, Instant.class, createCustomZones(null, zoneId));
        assertThat(actual.toEpochMilli()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testSqlDateToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        java.sql.Date date = new java.sql.Date(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToLong(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        long actual = this.converter.convert(instant, long.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToAtomicLong(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        AtomicLong actual = this.converter.convert(instant, AtomicLong.class, createCustomZones(null, zoneId));
        assertThat(actual.get()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToFloat(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        float actual = this.converter.convert(instant, float.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo((float) epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToDouble(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        double actual = this.converter.convert(instant, double.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo((double) epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToTimestamp(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        Timestamp actual = this.converter.convert(instant, Timestamp.class, createCustomZones(null, zoneId));
        assertThat(actual.getTime()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToDate(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        Date actual = this.converter.convert(instant, Date.class, createCustomZones(null, zoneId));
        assertThat(actual.getTime()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToSqlDate(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        java.sql.Date actual = this.converter.convert(instant, java.sql.Date.class, createCustomZones(null, zoneId));
        assertThat(actual.getTime()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToCalendar(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        Calendar actual = this.converter.convert(instant, Calendar.class, createCustomZones(null, zoneId));
        assertThat(actual.getTime().getTime()).isEqualTo(epochMilli);
        assertThat(actual.getTimeZone()).isEqualTo(TimeZone.getTimeZone(zoneId));
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToBigInteger(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        BigInteger actual = this.converter.convert(instant, BigInteger.class, createCustomZones(null, zoneId));
        assertThat(actual.longValue()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToBigDecimal(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        BigDecimal actual = this.converter.convert(instant, BigDecimal.class, createCustomZones(null, zoneId));
        assertThat(actual.longValue()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToLocalDate(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        LocalDate actual = this.converter.convert(instant, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(expected.toLocalDate());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testInstantToLocalTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        LocalTime actual = this.converter.convert(instant, LocalTime.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(expected.toLocalTime());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testTimestampToLocalDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Timestamp date = new Timestamp(epochMilli);
        LocalDateTime localDateTime = this.converter.convert(date, LocalDateTime.class, createCustomZones(null, zoneId));
        assertThat(localDateTime).isEqualTo(expected);
    }

    public static Stream<Arguments> epochMillis_withLocalDateInformation() {
        return Stream.of(Arguments.of(1687622249729L, TOKYO, LocalDate.of(2023, 6, 25)), Arguments.of(1687622249729L, PARIS, LocalDate.of(2023, 6, 24)), Arguments.of(1687622249729L, GMT, LocalDate.of(2023, 6, 24)), Arguments.of(1687622249729L, NEW_YORK, LocalDate.of(2023, 6, 24)), Arguments.of(1687622249729L, CHICAGO, LocalDate.of(2023, 6, 24)), Arguments.of(1687622249729L, LOS_ANGELES, LocalDate.of(2023, 6, 24)), Arguments.of(946702799959L, TOKYO, LocalDate.of(2000, 1, 1)), Arguments.of(946702799959L, PARIS, LocalDate.of(2000, 1, 1)), Arguments.of(946702799959L, GMT, LocalDate.of(2000, 1, 1)), Arguments.of(946702799959L, NEW_YORK, LocalDate.of(1999, 12, 31)), Arguments.of(946702799959L, CHICAGO, LocalDate.of(1999, 12, 31)), Arguments.of(946702799959L, LOS_ANGELES, LocalDate.of(1999, 12, 31)));
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testCalendarToDouble(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        double d = this.converter.convert(calendar, double.class, createCustomZones(null, zoneId));
        assertThat(d).isEqualTo((double) epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testCalendarToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        LocalDate localDate = this.converter.convert(calendar, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToLocalTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        LocalTime actual = this.converter.convert(calendar, LocalTime.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(expected.toLocalTime());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToZonedDateTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        ZonedDateTime actual = this.converter.convert(calendar, ZonedDateTime.class, createCustomZones(null, zoneId));
        assertThat(actual.toLocalDateTime()).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToInstant(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        Instant actual = this.converter.convert(calendar, Instant.class, createCustomZones(null, zoneId));
        assertThat(actual.toEpochMilli()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToBigDecimal(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        BigDecimal actual = this.converter.convert(calendar, BigDecimal.class, createCustomZones(null, zoneId));
        assertThat(actual.longValue()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testCalendarToBigInteger(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(epochMilli);
        BigInteger actual = this.converter.convert(calendar, BigInteger.class, createCustomZones(null, zoneId));
        assertThat(actual.longValue()).isEqualTo(epochMilli);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateTimeInformation")
    void testDateToLocalTime(long epochMilli, ZoneId zoneId, LocalDateTime expected) {
        Date date = new Date(epochMilli);
        LocalTime actual = this.converter.convert(date, LocalTime.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(expected.toLocalTime());
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testCalendarToLocalDate_whenCalendarTimeZoneMatches(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Calendar calendar = Calendar.getInstance(TimeZone.getTimeZone(zoneId));
        calendar.setTimeInMillis(epochMilli);
        LocalDate localDate = this.converter.convert(calendar, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testLongToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        LocalDate localDate = this.converter.convert(epochMilli, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testZonedDateTimeToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        LocalDate localDate = this.converter.convert(epochMilli, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testInstantToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Instant instant = Instant.ofEpochMilli(epochMilli);
        LocalDate localDate = this.converter.convert(instant, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testDateToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Date date = new Date(epochMilli);
        LocalDate localDate = this.converter.convert(date, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testSqlDateToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        java.sql.Date date = new java.sql.Date(epochMilli);
        LocalDate localDate = this.converter.convert(date, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testTimestampToLocalDate(long epochMilli, ZoneId zoneId, LocalDate expected) {
        Timestamp date = new Timestamp(epochMilli);
        LocalDate localDate = this.converter.convert(date, LocalDate.class, createCustomZones(null, zoneId));
        assertThat(localDate).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("toLongParams")
    void testLongToBigInteger(Object source, Number number) {
        long expected = number.longValue();
        BigInteger actual = this.converter.convert(source, BigInteger.class, createCustomZones(null, null));
        assertThat(actual).isEqualTo(BigInteger.valueOf(expected));
    }

    @ParameterizedTest
    @MethodSource("epochMillis_withLocalDateInformation")
    void testLongToLocalTime(long epochMilli, ZoneId zoneId, LocalDate expected) {
        LocalTime actual = this.converter.convert(epochMilli, LocalTime.class, createCustomZones(null, zoneId));
        assertThat(actual).isEqualTo(Instant.ofEpochMilli(epochMilli).atZone(zoneId).toLocalTime());
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateToLong(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        long milli = this.converter.convert(initial, long.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(milli).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(milli, LocalDateTime.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    public static Stream<Arguments> localDateTimeConversion_params() {
        return Stream.of(Arguments.of(1687622249729L, NEW_YORK, LDT_2023_NY, TOKYO, LDT_2023_TOKYO), Arguments.of(1687622249729L, LOS_ANGELES, LDT_2023_LA, PARIS, LDT_2023_PARIS));
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToLong(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        long milli = this.converter.convert(initial, long.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(milli).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(milli, LocalDateTime.class, createCustomZones(null, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToInstant(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        Instant intermediate = this.converter.convert(initial, Instant.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(intermediate.toEpochMilli()).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(intermediate, LocalDateTime.class, createCustomZones(null, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToAtomicLong(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        AtomicLong milli = this.converter.convert(initial, AtomicLong.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(milli.longValue()).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(milli, LocalDateTime.class, createCustomZones(null, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToZonedDateTime(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        ZonedDateTime intermediate = this.converter.convert(initial, ZonedDateTime.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(intermediate.toInstant().toEpochMilli()).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(intermediate, LocalDateTime.class, createCustomZones(null, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToLocalTime(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        LocalTime intermediate = this.converter.convert(initial, LocalTime.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(intermediate).isEqualTo(expected.toLocalTime());
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToBigInteger(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        BigInteger milli = this.converter.convert(initial, BigInteger.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(milli.longValue()).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(milli, LocalDateTime.class, createCustomZones(null, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("localDateTimeConversion_params")
    void testLocalDateTimeToBigDecimal(long epochMilli, ZoneId sourceZoneId, LocalDateTime initial, ZoneId targetZoneId, LocalDateTime expected) {
        BigDecimal milli = this.converter.convert(initial, BigDecimal.class, createCustomZones(sourceZoneId, targetZoneId));
        assertThat(milli.longValue()).isEqualTo(epochMilli);
        LocalDateTime actual = this.converter.convert(milli, LocalDateTime.class, createCustomZones(null, targetZoneId));
        assertThat(actual).isEqualTo(expected);
    }

    public static Stream<Arguments> testAtomicLongParams_withIllegalArguments() {
        return Stream.of(Arguments.of("45badNumber", "not parseable as a long value"), Arguments.of("-9223372036854775809", "not parseable as a long value"), Arguments.of("9223372036854775808", "not parseable as a long value"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("testAtomicLongParams_withIllegalArguments")
    void testAtomicLong_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, AtomicLong.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> testStringParams() {
        return Stream.of(Arguments.of("-32768", "-32768"), Arguments.of("Hello", "Hello"), Arguments.of(Byte.MIN_VALUE, "-128"), Arguments.of(Byte.MAX_VALUE, "127"), Arguments.of(Short.MIN_VALUE, "-32768"), Arguments.of(Short.MAX_VALUE, "32767L"), Arguments.of(Integer.MIN_VALUE, "-2147483648L"), Arguments.of(Integer.MAX_VALUE, "2147483647L"), Arguments.of(Long.MIN_VALUE, "-9223372036854775808L"), Arguments.of(Long.MAX_VALUE, "9223372036854775807L"), Arguments.of(-128.0f, "-128"), Arguments.of(127.56f, "127.56"), Arguments.of(-128.0d, "-128"), Arguments.of(1.23456789d, "1.23456789"), Arguments.of(123456789.12345, "123456789.12345"), Arguments.of(new BigDecimal("9999999999999999999999999.99999999"), "9999999999999999999999999.99999999"), Arguments.of(new BigInteger("999999999999999999999999999999999999999999"), "999999999999999999999999999999999999999999"), Arguments.of(new AtomicInteger(25), "25"), Arguments.of(new AtomicLong(Long.MAX_VALUE), "9223372036854775807L"), Arguments.of(3.1415926535897932384626433e18, "3141592653589793300"), Arguments.of(true, "true"), Arguments.of(false, "false"), Arguments.of(Boolean.TRUE, "true"), Arguments.of(Boolean.FALSE, "false"), Arguments.of(new AtomicBoolean(true), "true"), Arguments.of(new AtomicBoolean(false), "false"), Arguments.of('J', "J"), Arguments.of(new BigDecimal("3.1415926535897932384626433"), "3.1415926535897932384626433"), Arguments.of(new BigInteger("123456789012345678901234567890"), "123456789012345678901234567890"));
    }

    @ParameterizedTest
    @MethodSource("testAtomicLongParams")
    void testStringParams(Object value, AtomicLong expectedResult) {
        AtomicLong converted = this.converter.convert(value, AtomicLong.class);
        assertThat(converted.get()).isEqualTo(expectedResult.get());
    }

    @ParameterizedTest
    @NullAndEmptySource
    void testStringNullAndEmpty(String value) {
        String converted = this.converter.convert(value, String.class);
        assertThat(converted).isSameAs(value);
    }

    public static Stream<Arguments> testConvertStringParams_withIllegalArguments() {
        return Stream.of(Arguments.of(ZoneId.systemDefault(), "Unsupported conversion"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("testConvertStringParams_withIllegalArguments")
    void testConvertString_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, AtomicLong.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> testBigDecimalParams() {
        return paramsForFloatingPointTypes(Double.MIN_VALUE, Double.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("testBigDecimalParams")
    void testBigDecimal(Object value, Number number) {
        BigDecimal converted = this.converter.convert(value, BigDecimal.class);
        assertThat(converted).isEqualTo(new BigDecimal(number.toString()));
    }

    public static Stream<Arguments> testBigDecimalParams_withObjectsShouldBeSame() {
        return Stream.of(Arguments.of(new AtomicBoolean(true), BigDecimal.ONE), Arguments.of(new AtomicBoolean(false), BigDecimal.ZERO), Arguments.of(true, BigDecimal.ONE), Arguments.of(false, BigDecimal.ZERO), Arguments.of(Boolean.TRUE, BigDecimal.ONE), Arguments.of(Boolean.FALSE, BigDecimal.ZERO), Arguments.of("", BigDecimal.ZERO));
    }

    @ParameterizedTest
    @MethodSource("testBigDecimalParams_withObjectsShouldBeSame")
    void testBigDecimal_withObjectsThatShouldBeSameAs(Object value, BigDecimal expected) {
        BigDecimal converted = this.converter.convert(value, BigDecimal.class);
        assertThat(converted).isSameAs(expected);
    }

    public static Stream<Arguments> testConvertToBigDecimalParams_withIllegalArguments() {
        return Stream.of(Arguments.of("45badNumber", "not parseable"), Arguments.of(ZoneId.systemDefault(), "Unsupported conversion"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("testConvertToBigDecimalParams_withIllegalArguments")
    void testConvertToBigDecimal_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, BigDecimal.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> testBigIntegerParams() {
        return paramsForIntegerTypes(Long.MIN_VALUE, Long.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("testBigIntegerParams")
    void testBigInteger(Object value, Number number) {
        BigInteger converted = this.converter.convert(value, BigInteger.class);
        assertThat(converted).isEqualTo(new BigInteger(number.toString()));
    }

    public static Stream<Arguments> testBigIntegerParams_withObjectsShouldBeSameAs() {
        return Stream.of(Arguments.of(CommonValues.INTEGER_ZERO, BigInteger.ZERO), Arguments.of(CommonValues.INTEGER_ONE, BigInteger.ONE), Arguments.of(CommonValues.LONG_ZERO, BigInteger.ZERO), Arguments.of(CommonValues.LONG_ONE, BigInteger.ONE), Arguments.of(new AtomicBoolean(true), BigInteger.ONE), Arguments.of(new AtomicBoolean(false), BigInteger.ZERO), Arguments.of(true, BigInteger.ONE), Arguments.of(false, BigInteger.ZERO), Arguments.of(Boolean.TRUE, BigInteger.ONE), Arguments.of(Boolean.FALSE, BigInteger.ZERO), Arguments.of("", BigInteger.ZERO), Arguments.of(BigInteger.ZERO, BigInteger.ZERO), Arguments.of(BigInteger.ONE, BigInteger.ONE), Arguments.of(BigInteger.TEN, BigInteger.TEN));
    }

    @ParameterizedTest
    @MethodSource("testBigIntegerParams_withObjectsShouldBeSameAs")
    void testBigInteger_withObjectsShouldBeSameAs(Object value, BigInteger expected) {
        BigInteger converted = this.converter.convert(value, BigInteger.class);
        assertThat(converted).isSameAs(expected);
    }

    public static Stream<Arguments> testConvertToBigIntegerParams_withIllegalArguments() {
        return Stream.of(Arguments.of("45badNumber", "not parseable"), Arguments.of(ZoneId.systemDefault(), "Unsupported conversion"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("testConvertToBigIntegerParams_withIllegalArguments")
    void testConvertToBigInteger_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, BigInteger.class)).withMessageContaining(partialMessage);
    }

    @ParameterizedTest
    @MethodSource("toIntParams")
    void testAtomicInteger(Object value, int expectedResult) {
        AtomicInteger converted = this.converter.convert(value, AtomicInteger.class);
        assertThat(converted.get()).isEqualTo(new AtomicInteger(expectedResult).get());
    }

    public static Stream<Arguments> testAtomicIntegerParams_withBooleanTypes() {
        return Stream.of(Arguments.of(new AtomicBoolean(true), new AtomicInteger(1)), Arguments.of(new AtomicBoolean(false), new AtomicInteger(0)), Arguments.of(true, new AtomicInteger(1)), Arguments.of(false, new AtomicInteger(0)), Arguments.of(Boolean.TRUE, new AtomicInteger(1)), Arguments.of(Boolean.FALSE, new AtomicInteger(0)));
    }

    @ParameterizedTest
    @MethodSource("testAtomicIntegerParams_withBooleanTypes")
    void testAtomicInteger_withBooleanTypes(Object value, AtomicInteger expected) {
        AtomicInteger converted = this.converter.convert(value, AtomicInteger.class);
        assertThat(converted.get()).isEqualTo(expected.get());
    }

    public static Stream<Arguments> testAtomicInteger_withIllegalArguments_params() {
        return Stream.of(Arguments.of("45badNumber", "not parseable"), Arguments.of(ZoneId.systemDefault(), "Unsupported conversion"), Arguments.of(TimeZone.getDefault(), "Unsupported conversion"));
    }

    @ParameterizedTest
    @MethodSource("testAtomicInteger_withIllegalArguments_params")
    void testAtomicInteger_withIllegalArguments(Object value, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(value, BigInteger.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> epochMilli_exampleOneParams() {
        return Stream.of(Arguments.of(1705601070270L), Arguments.of(Long.valueOf(1705601070270L)), Arguments.of(new AtomicLong(1705601070270L)), Arguments.of(1705601070270.798659898d), Arguments.of(BigInteger.valueOf(1705601070270L)), Arguments.of(BigDecimal.valueOf(1705601070270L)), Arguments.of("1705601070270"));
    }

    @ParameterizedTest
    @MethodSource("epochMilli_exampleOneParams")
    void testDate(Object value) {
        Date expected = new Date(1705601070270L);
        Date converted = this.converter.convert(value, Date.class);
        assertThat(converted).isEqualTo(expected);
    }

    // float doesn't have enough significant digits to accurately represent today's dates
    public static Stream<Arguments> conversionsWithPrecisionLoss_primitiveParams() {
        return Stream.of(// double ->
        Arguments.of(1705601070270.89765d, float.class, 1705601010100f), Arguments.of(1705601070270.89765d, Float.class, 1705601010100f), Arguments.of(1705601070270.89765d, byte.class, (byte) -1), Arguments.of(1705601070270.89765d, Byte.class, (byte) -1), Arguments.of(1705601070270.89765d, short.class, (short) -1), Arguments.of(1705601070270.89765d, Short.class, (short) -1), Arguments.of(1705601070270.89765d, int.class, 2147483647), Arguments.of(1705601070270.89765d, Integer.class, 2147483647), Arguments.of(1705601070270.89765d, long.class, 1705601070270L), Arguments.of(1705601070270.89765d, Long.class, 1705601070270L), // float ->
        Arguments.of(65679.6f, byte.class, (byte) -113), Arguments.of(65679.6f, Byte.class, (byte) -113), Arguments.of(65679.6f, short.class, (short) 143), Arguments.of(65679.6f, Short.class, (short) 143), Arguments.of(65679.6f, int.class, 65679), Arguments.of(65679.6f, Integer.class, 65679), Arguments.of(65679.6f, long.class, 65679L), Arguments.of(65679.6f, Long.class, 65679L), // long ->
        Arguments.of(new BigInteger("92233720368547738079919"), double.class, 92233720368547740000000.0d), Arguments.of(new BigInteger("92233720368547738079919"), Double.class, 92233720368547740000000.0d), Arguments.of(new BigInteger("92233720368547738079919"), float.class, 92233720368547760000000f), Arguments.of(new BigInteger("92233720368547738079919"), Float.class, 92233720368547760000000f), Arguments.of(new BigInteger("92233720368547738079919"), Byte.class, (byte) -81), Arguments.of(new BigInteger("92233720368547738079919"), byte.class, (byte) -81), Arguments.of(new BigInteger("92233720368547738079919"), short.class, (short) -11601), Arguments.of(new BigInteger("92233720368547738079919"), Short.class, (short) -11601), Arguments.of(new BigInteger("92233720368547738079919"), int.class, -20000081), Arguments.of(new BigInteger("92233720368547738079919"), Integer.class, -20000081), Arguments.of(new BigInteger("92233720368547738079919"), long.class, -20000081L), Arguments.of(new BigInteger("92233720368547738079919"), Long.class, -20000081L), // long ->
        Arguments.of(9223372036854773807L, double.class, 9223372036854773800.0d), Arguments.of(9223372036854773807L, Double.class, 9223372036854773800.0d), Arguments.of(9223372036854773807L, float.class, 9223372036854776000.0f), Arguments.of(9223372036854773807L, Float.class, 9223372036854776000.0f), Arguments.of(9223372036854773807L, Byte.class, (byte) 47), Arguments.of(9223372036854773807L, byte.class, (byte) 47), Arguments.of(9223372036854773807L, short.class, (short) -2001), Arguments.of(9223372036854773807L, Short.class, (short) -2001), Arguments.of(9223372036854773807L, int.class, -2001), Arguments.of(9223372036854773807L, Integer.class, -2001), // AtomicLong ->
        Arguments.of(new AtomicLong(9223372036854773807L), double.class, 9223372036854773800.0d), Arguments.of(new AtomicLong(9223372036854773807L), Double.class, 9223372036854773800.0d), Arguments.of(new AtomicLong(9223372036854773807L), float.class, 9223372036854776000.0f), Arguments.of(new AtomicLong(9223372036854773807L), Float.class, 9223372036854776000.0f), Arguments.of(new AtomicLong(9223372036854773807L), Byte.class, (byte) 47), Arguments.of(new AtomicLong(9223372036854773807L), byte.class, (byte) 47), Arguments.of(new AtomicLong(9223372036854773807L), short.class, (short) -2001), Arguments.of(new AtomicLong(9223372036854773807L), Short.class, (short) -2001), Arguments.of(new AtomicLong(9223372036854773807L), int.class, -2001), Arguments.of(new AtomicLong(9223372036854773807L), Integer.class, -2001), Arguments.of(2147473647, float.class, 2147473664.0f), Arguments.of(2147473647, Float.class, 2147473664.0f), Arguments.of(2147473647, Byte.class, (byte) -17), Arguments.of(2147473647, byte.class, (byte) -17), Arguments.of(2147473647, short.class, (short) -10001), Arguments.of(2147473647, Short.class, (short) -10001), // AtomicInteger ->
        Arguments.of(new AtomicInteger(2147473647), float.class, 2147473664.0f), Arguments.of(new AtomicInteger(2147473647), Float.class, 2147473664.0f), Arguments.of(new AtomicInteger(2147473647), Byte.class, (byte) -17), Arguments.of(new AtomicInteger(2147473647), byte.class, (byte) -17), Arguments.of(new AtomicInteger(2147473647), short.class, (short) -10001), Arguments.of(new AtomicInteger(2147473647), Short.class, (short) -10001), // short ->
        Arguments.of((short) 62212, Byte.class, (byte) 4), Arguments.of((short) 62212, byte.class, (byte) 4));
    }

    @ParameterizedTest
    @MethodSource("conversionsWithPrecisionLoss_primitiveParams")
    void conversionsWithPrecisionLoss_primitives(Object value, Class c, Object expected) {
        Object converted = this.converter.convert(value, c);
        assertThat(converted).isEqualTo(expected);
    }

    // float doesn't have enough significant digits to accurately represent today's dates
    public static Stream<Arguments> conversionsWithPrecisionLoss_toAtomicIntegerParams() {
        return Stream.of(Arguments.of(1705601070270.89765d, new AtomicInteger(2147483647)), Arguments.of(65679.6f, new AtomicInteger(65679)), Arguments.of(9223372036854773807L, new AtomicInteger(-2001)), Arguments.of(new AtomicLong(9223372036854773807L), new AtomicInteger(-2001)));
    }

    @ParameterizedTest
    @MethodSource("conversionsWithPrecisionLoss_toAtomicIntegerParams")
    void conversionsWithPrecisionLoss_toAtomicInteger(Object value, AtomicInteger expected) {
        AtomicInteger converted = this.converter.convert(value, AtomicInteger.class);
        assertThat(converted.get()).isEqualTo(expected.get());
    }

    public static Stream<Arguments> conversionsWithPrecisionLoss_toAtomicLongParams() {
        return Stream.of(// double ->
        Arguments.of(1705601070270.89765d, new AtomicLong(1705601070270L)), Arguments.of(65679.6f, new AtomicLong(65679L)));
    }

    @ParameterizedTest
    @MethodSource("conversionsWithPrecisionLoss_toAtomicLongParams")
    void conversionsWithPrecisionLoss_toAtomicLong(Object value, AtomicLong expected) {
        AtomicLong converted = this.converter.convert(value, AtomicLong.class);
        assertThat(converted.get()).isEqualTo(expected.get());
    }

    public static Stream<Arguments> extremeDateParams() {
        return Stream.of(Arguments.of((short) 75, new Date(75)), Arguments.of(Byte.MIN_VALUE, new Date(Byte.MIN_VALUE)), Arguments.of(Byte.MAX_VALUE, new Date(Byte.MAX_VALUE)), Arguments.of(Short.MIN_VALUE, new Date(Short.MIN_VALUE)), Arguments.of(Short.MAX_VALUE, new Date(Short.MAX_VALUE)), Arguments.of(Integer.MIN_VALUE, new Date(Integer.MIN_VALUE)), Arguments.of(Integer.MAX_VALUE, new Date(Integer.MAX_VALUE)), Arguments.of(Long.MIN_VALUE, new Date(Long.MIN_VALUE)), Arguments.of(Long.MAX_VALUE, new Date(Long.MAX_VALUE)), Arguments.of(127.0d, new Date(127)), Arguments.of(new AtomicInteger(25), new Date(25)));
    }

    @ParameterizedTest
    @MethodSource("extremeDateParams")
    void testExtremeDateParams(Object value, Date expected) {
        Date converted = this.converter.convert(value, Date.class);
        assertThat(converted).isEqualTo(expected);
    }

    public static Stream<Arguments> toCalendarParams() {
        return Stream.of(Arguments.of(new Date(1687622249729L)), Arguments.of(new java.sql.Date(1687622249729L)), Arguments.of(new Timestamp(1687622249729L)), Arguments.of(Instant.ofEpochMilli(1687622249729L)), Arguments.of(1687622249729L), Arguments.of(BigInteger.valueOf(1687622249729L)), Arguments.of(BigDecimal.valueOf(1687622249729L)), Arguments.of("1687622249729"), Arguments.of(new AtomicLong(1687622249729L)));
    }

    @ParameterizedTest
    @MethodSource("toCalendarParams")
    void toCalendar(Object source) {
        Long epochMilli = 1687622249729L;
        Calendar calendar = this.converter.convert(source, Calendar.class);
        assertEquals(calendar.getTime().getTime(), epochMilli);
        // BigInteger to Calendar
        // Other direction --> Calendar to other date types
        Calendar now = Calendar.getInstance();
        // Calendar to Date
        calendar = this.converter.convert(now, Calendar.class);
        Date date = this.converter.convert(calendar, Date.class);
        assertEquals(calendar.getTime(), date);
        // Calendar to SqlDate
        java.sql.Date sqlDate = this.converter.convert(calendar, java.sql.Date.class);
        assertEquals(calendar.getTime().getTime(), sqlDate.getTime());
        // Calendar to Timestamp
        Timestamp timestamp = this.converter.convert(calendar, Timestamp.class);
        assertEquals(calendar.getTime().getTime(), timestamp.getTime());
        // Calendar to Long
        long tnow = this.converter.convert(calendar, long.class);
        assertEquals(calendar.getTime().getTime(), tnow);
        // Calendar to AtomicLong
        AtomicLong atomicLong = this.converter.convert(calendar, AtomicLong.class);
        assertEquals(calendar.getTime().getTime(), atomicLong.get());
        // Calendar to String
        String strDate = this.converter.convert(calendar, String.class);
        String strDate2 = this.converter.convert(now, String.class);
        assertEquals(strDate, strDate2);
        // Calendar to BigInteger
        BigInteger bigInt = this.converter.convert(calendar, BigInteger.class);
        assertEquals(now.getTime().getTime(), bigInt.longValue());
        // Calendar to BigDecimal
        BigDecimal bigDec = this.converter.convert(calendar, BigDecimal.class);
        assertEquals(now.getTime().getTime(), bigDec.longValue());
    }

    public static Stream<Arguments> identityParams() {
        return Stream.of(Arguments.of(9L, Long.class), Arguments.of((short) 10, Short.class), Arguments.of("foo", String.class), Arguments.of(LocalDate.now(), LocalDate.class), Arguments.of(LocalDateTime.now(), LocalDateTime.class));
    }

    @ParameterizedTest
    @MethodSource("identityParams")
    void testConversions_whenClassTypeMatchesObjectType_returnsItself(Object o, Class<?> c) {
        Object converted = this.converter.convert(o, c);
        assertThat(converted).isSameAs(o);
    }

    public static Stream<Arguments> nonIdentityParams() {
        return Stream.of(Arguments.of(new Date(), Date.class), Arguments.of(new java.sql.Date(System.currentTimeMillis()), java.sql.Date.class), Arguments.of(new Timestamp(System.currentTimeMillis()), Timestamp.class), Arguments.of(Calendar.getInstance(), Calendar.class));
    }

    @ParameterizedTest
    @MethodSource("nonIdentityParams")
    void testConversions_whenClassTypeMatchesObjectType_stillCreatesNewObject(Object o, Class<?> c) {
        Object converted = this.converter.convert(o, c);
        assertThat(converted).isNotSameAs(o);
    }

    public static Stream<Arguments> unparseableDates() {
        return Stream.of(Arguments.of(" "), Arguments.of(""));
    }

    @ParameterizedTest
    @MethodSource("unparseableDates")
    void testUnparseableDates_Date(String date) {
        assertNull(this.converter.convert(date, Date.class));
    }

    @ParameterizedTest
    @MethodSource("unparseableDates")
    void testUnparseableDates_SqlDate(String date) {
        assertNull(this.converter.convert(date, java.sql.Date.class));
    }

    @ParameterizedTest
    @MethodSource("unparseableDates")
    void testUnparseableDates_Timestamp(String date) {
        assertNull(this.converter.convert(date, Timestamp.class));
    }

    public static Stream<Arguments> toFloatParams() {
        return paramsForFloatingPointTypes(Float.MIN_VALUE, Float.MAX_VALUE);
    }

    @ParameterizedTest()
    @MethodSource("toFloatParams")
    void toFloat(Object initial, Number number) {
        float expected = number.floatValue();
        float f = this.converter.convert(initial, float.class);
        assertThat(f).isEqualTo(expected);
    }

    @ParameterizedTest()
    @MethodSource("toFloatParams")
    void toFloat_objectType(Object initial, Number number) {
        Float expected = number.floatValue();
        float f = this.converter.convert(initial, Float.class);
        assertThat(f).isEqualTo(expected);
    }

    public static Stream<Arguments> toFloat_illegalArguments() {
        return Stream.of(Arguments.of(TimeZone.getDefault(), "Unsupported conversion"), Arguments.of("45.6badNumber", "not parseable"));
    }

    @ParameterizedTest()
    @MethodSource("toFloat_illegalArguments")
    void testConvertToFloat_withIllegalArguments(Object initial, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(initial, float.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> toFloat_booleanArguments() {
        return Stream.of(Arguments.of(true, CommonValues.FLOAT_ONE), Arguments.of(false, CommonValues.FLOAT_ZERO), Arguments.of(Boolean.TRUE, CommonValues.FLOAT_ONE), Arguments.of(Boolean.FALSE, CommonValues.FLOAT_ZERO), Arguments.of(new AtomicBoolean(true), CommonValues.FLOAT_ONE), Arguments.of(new AtomicBoolean(false), CommonValues.FLOAT_ZERO));
    }

    @ParameterizedTest
    @MethodSource("toFloat_booleanArguments")
    void toFloat_withBooleanArguments_returnsCommonValue(Object initial, Float expected) {
        Float f = this.converter.convert(initial, Float.class);
        assertThat(f).isSameAs(expected);
    }

    @ParameterizedTest
    @MethodSource("toFloat_booleanArguments")
    void toFloat_withBooleanArguments_returnsCommonValueWhenPrimitive(Object initial, float expected) {
        float f = this.converter.convert(initial, float.class);
        assertThat(f).isEqualTo(expected);
    }

    public static Stream<Arguments> toDoubleParams() {
        return paramsForFloatingPointTypes(Double.MIN_VALUE, Double.MAX_VALUE);
    }

    @ParameterizedTest
    @MethodSource("toDoubleParams")
    void testDouble(Object value, Number number) {
        double converted = this.converter.convert(value, double.class);
        assertThat(converted).isEqualTo(number.doubleValue());
    }

    @ParameterizedTest
    @MethodSource("toDoubleParams")
    void testDouble_ObjectType(Object value, Number number) {
        Double converted = this.converter.convert(value, Double.class);
        assertThat(converted).isEqualTo(number.doubleValue());
    }

    @ParameterizedTest
    @MethodSource("toCalendarParams")
    void testMapToCalendar(Object value) {
        final Map map = new HashMap();
        map.put("value", value);
        Calendar cal = this.converter.convert(map, Calendar.class);
        assertThat(cal).isNotNull();
        map.clear();
        map.put("value", "");
        assert null == this.converter.convert(map, Calendar.class);
        map.clear();
        map.put("value", null);
        assert null == this.converter.convert(map, Calendar.class);
        map.clear();
        assertThatThrownBy(() -> this.converter.convert(map, Calendar.class)).isInstanceOf(IllegalArgumentException.class).hasMessageContaining("To convert from Map to Calendar the map must include one of the following: [time, zone], [_v], or [value] with associated values");
    }

    public static Stream<Arguments> classesThatReturnZero_whenConvertingFromNull() {
        return Stream.of(Arguments.of(byte.class, CommonValues.BYTE_ZERO), Arguments.of(int.class, CommonValues.INTEGER_ZERO), Arguments.of(short.class, CommonValues.SHORT_ZERO), Arguments.of(char.class, CommonValues.CHARACTER_ZERO), Arguments.of(long.class, CommonValues.LONG_ZERO), Arguments.of(float.class, CommonValues.FLOAT_ZERO), Arguments.of(double.class, CommonValues.DOUBLE_ZERO));
    }

    @ParameterizedTest
    @MethodSource("classesThatReturnZero_whenConvertingFromNull")
    void testClassesThatReturnZero_whenConvertingFromNull(Class c, Object expected) {
        Object zero = this.converter.convert(null, c);
        assertThat(zero).isSameAs(expected);
    }

    public static Stream<Arguments> classesThatReturnFalse_whenConvertingFromNull() {
        return Stream.of(Arguments.of(Boolean.class), Arguments.of(boolean.class));
    }

    public static Stream<Arguments> toCharacterParams() {
        return Stream.of(Arguments.of((byte) 65), Arguments.of((short) 65), Arguments.of(65), Arguments.of(65L), Arguments.of(65.0), Arguments.of(65.0d), Arguments.of(Byte.valueOf("65")), Arguments.of(Short.valueOf("65")), Arguments.of(Integer.valueOf("65")), Arguments.of(Long.valueOf("65")), Arguments.of(Float.valueOf("65")), Arguments.of(Double.valueOf("65")), Arguments.of(BigInteger.valueOf(65)), Arguments.of(BigDecimal.valueOf(65)), Arguments.of('A'), Arguments.of("A"));
    }

    @ParameterizedTest
    @MethodSource("toCharacterParams")
    void toCharacter_ObjectType(Object source) {
        Character ch = this.converter.convert(source, Character.class);
        assertThat(ch).isEqualTo('A');
        Object roundTrip = this.converter.convert(ch, source.getClass());
        assertThat(source).isEqualTo(roundTrip);
    }

    @ParameterizedTest
    @MethodSource("toCharacterParams")
    void toCharacter(Object source) {
        char ch = this.converter.convert(source, char.class);
        assertThat(ch).isEqualTo('A');
        Object roundTrip = this.converter.convert(ch, source.getClass());
        assertThat(source).isEqualTo(roundTrip);
    }

    public static Stream<Arguments> toChar_illegalArguments() {
        return Stream.of(Arguments.of(TimeZone.getDefault(), "Unsupported conversion"), Arguments.of(Integer.MAX_VALUE, "out of range to be converted to character"));
    }

    @ParameterizedTest()
    @MethodSource("toChar_illegalArguments")
    void testConvertTCharacter_withIllegalArguments(Object initial, String partialMessage) {
        assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> this.converter.convert(initial, Character.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> toChar_numberFormatException() {
        return Stream.of(Arguments.of("45.number", "For input string: \"45.number\""), Arguments.of("AB", "For input string: \"AB\""));
    }

    @ParameterizedTest()
    @MethodSource("toChar_numberFormatException")
    void testConvertTCharacter_withNumberFormatExceptions(Object initial, String partialMessage) {
        assertThatExceptionOfType(NumberFormatException.class).isThrownBy(() -> this.converter.convert(initial, Character.class)).withMessageContaining(partialMessage);
    }

    public static Stream<Arguments> trueValues() {
        return Stream.of(Arguments.of(true), Arguments.of(Boolean.TRUE), Arguments.of(new AtomicBoolean(true)));
    }

    @ParameterizedTest
    @MethodSource("trueValues")
    void toCharacter_whenTrue_withDefaultOptions_returnsCommonValue(Object source) {
        assertThat(this.converter.convert(source, char.class)).isSameAs(CommonValues.CHARACTER_ONE);
    }

    @ParameterizedTest
    @MethodSource("trueValues")
    void toCharacter_whenTrue_withDefaultOptions_andObjectType_returnsCommonValue(Object source) {
        assertThat(this.converter.convert(source, Character.class)).isSameAs(CommonValues.CHARACTER_ONE);
    }

    @ParameterizedTest
    @MethodSource("trueValues")
    void toCharacter_whenTrue_withCustomOptions_returnsTrueCharacter(Object source) {
        assertThat(this.converter.convert(source, Character.class, TF_OPTIONS)).isEqualTo('T');
        assertThat(this.converter.convert(source, Character.class, YN_OPTIONS)).isEqualTo('Y');
    }

    public static final ConverterOptions TF_OPTIONS = createCustomBooleanCharacter('T', 'F');

    public static final ConverterOptions YN_OPTIONS = createCustomBooleanCharacter('Y', 'N');

    public static Stream<Arguments> falseValues() {
        return Stream.of(Arguments.of(false), Arguments.of(Boolean.FALSE), Arguments.of(new AtomicBoolean(false)));
    }

    @ParameterizedTest
    @MethodSource("falseValues")
    void toCharacter_whenFalse_withDefaultOptions_returnsCommonValue(Object source) {
        assertThat(this.converter.convert(source, char.class)).isSameAs(CommonValues.CHARACTER_ZERO);
    }

    @ParameterizedTest
    @MethodSource("falseValues")
    void toCharacter_whenFalse_withDefaultOptions_andObjectType_returnsCommonValue(Object source) {
        assertThat(this.converter.convert(source, Character.class)).isSameAs(CommonValues.CHARACTER_ZERO);
    }

    @ParameterizedTest
    @MethodSource("falseValues")
    void toCharacter_whenFalse_withCustomOptions_returnsTrueCharacter(Object source) {
        assertThat(this.converter.convert(source, Character.class, TF_OPTIONS)).isEqualTo('F');
        assertThat(this.converter.convert(source, Character.class, YN_OPTIONS)).isEqualTo('N');
    }

    public static Stream<Arguments> stringToClassParams() {
        return Stream.of(Arguments.of("java.math.BigInteger"), Arguments.of("java.lang.String"));
    }

    @ParameterizedTest
    @MethodSource("stringToClassParams")
    void stringToClass(String className) {
        Class<?> c = this.converter.convert(className, Class.class);
        assertThat(c).isNotNull();
        assertThat(c.getName()).isEqualTo(className);
    }

    @Test
    void testSqlDateToString_h2Test4() {
    Class<?> clazz1 = LocalDate.class;
    long now = -1;
    Date date = new Date(now);
    String strDate = this.converter.convert(date, String.class);
		List<Object> transformed_inputs = ConverterTest_testSqlDateToString.inputTransformation_testSqlDateToString(date, clazz1);
    Class<?> clazz2  = (Class<?>) transformed_inputs.get(1);
    Date x  = (Date) transformed_inputs.get(0);
        LocalDate l1 = (LocalDate) this.converter.convert(date, clazz1);
        LocalDate l2 = (LocalDate) this.converter.convert(x, clazz2);
        assertEquals(l1, l2);
    }

    static class DumbNumber extends BigInteger {

        DumbNumber(String val) {
            super(val);
        }

        public String toString() {
            return super.toString();
        }
    }

    static class Normie {

        String name;

        Normie(String name) {
            this.name = name;
        }

        void setName(String name) {
            this.name = name;
        }
    }

    static class Weirdo {

        String name;

        Weirdo(String name) {
            this.name = reverseString(name);
        }

        void setName(String name) {
            this.name = reverseString(name);
        }
    }

    static String reverseString(String in) {
        StringBuilder reversed = new StringBuilder();
        for (int i = in.length() - 1; i >= 0; i--) {
            reversed.append(in.charAt(i));
        }
        return reversed.toString();
    }

    public static Stream<Arguments> emptyStringTypes_withSameAsReturns() {
        return Stream.of(Arguments.of("", byte.class, CommonValues.BYTE_ZERO), Arguments.of("", Byte.class, CommonValues.BYTE_ZERO), Arguments.of("", short.class, CommonValues.SHORT_ZERO), Arguments.of("", Short.class, CommonValues.SHORT_ZERO), Arguments.of("", int.class, CommonValues.INTEGER_ZERO), Arguments.of("", Integer.class, CommonValues.INTEGER_ZERO), Arguments.of("", long.class, CommonValues.LONG_ZERO), Arguments.of("", Long.class, CommonValues.LONG_ZERO), Arguments.of("", float.class, CommonValues.FLOAT_ZERO), Arguments.of("", Float.class, CommonValues.FLOAT_ZERO), Arguments.of("", double.class, CommonValues.DOUBLE_ZERO), Arguments.of("", Double.class, CommonValues.DOUBLE_ZERO), Arguments.of("", boolean.class, Boolean.FALSE), Arguments.of("", Boolean.class, Boolean.FALSE), Arguments.of("", char.class, CommonValues.CHARACTER_ZERO), Arguments.of("", Character.class, CommonValues.CHARACTER_ZERO), Arguments.of("", BigDecimal.class, BigDecimal.ZERO), Arguments.of("", BigInteger.class, BigInteger.ZERO), Arguments.of("", String.class, EMPTY), Arguments.of("", byte[].class, EMPTY_BYTE_ARRAY), Arguments.of("", char[].class, EMPTY_CHAR_ARRAY));
    }

    @ParameterizedTest
    @MethodSource("emptyStringTypes_withSameAsReturns")
    void testEmptyStringToType_whereTypeReturnsSpecificObject(Object value, Class<?> type, Object expected) {
        Object converted = this.converter.convert(value, type);
        assertThat(converted).isSameAs(expected);
    }

    public static Stream<Arguments> emptyStringTypes_notSameObject() {
        return Stream.of(Arguments.of("", ByteBuffer.class, ByteBuffer.wrap(EMPTY_BYTE_ARRAY)), Arguments.of("", CharBuffer.class, CharBuffer.wrap(EMPTY_CHAR_ARRAY)));
    }

    @ParameterizedTest
    @MethodSource("emptyStringTypes_notSameObject")
    void testEmptyStringToType_whereTypeIsEqualButNotSameAs(Object value, Class<?> type, Object expected) {
        Object converted = this.converter.convert(value, type);
        assertThat(converted).isNotSameAs(expected);
        assertThat(converted).isEqualTo(expected);
    }

    public static Stream<Arguments> stringToByteArrayParams() {
        return Stream.of(Arguments.of("$1,000", StandardCharsets.US_ASCII, new byte[] { 36, 49, 44, 48, 48, 48 }), Arguments.of("$1,000", StandardCharsets.ISO_8859_1, new byte[] { 36, 49, 44, 48, 48, 48 }), Arguments.of("$1,000", StandardCharsets.UTF_8, new byte[] { 36, 49, 44, 48, 48, 48 }), Arguments.of("£1,000", StandardCharsets.ISO_8859_1, new byte[] { -93, 49, 44, 48, 48, 48 }), Arguments.of("£1,000", StandardCharsets.UTF_8, new byte[] { -62, -93, 49, 44, 48, 48, 48 }), Arguments.of("€1,000", StandardCharsets.UTF_8, new byte[] { -30, -126, -84, 49, 44, 48, 48, 48 }));
    }

    public static Stream<Arguments> stringToCharArrayParams() {
        return Stream.of(Arguments.of("$1,000", StandardCharsets.US_ASCII, new char[] { '$', '1', ',', '0', '0', '0' }), Arguments.of("$1,000", StandardCharsets.ISO_8859_1, new char[] { '$', '1', ',', '0', '0', '0' }), Arguments.of("$1,000", StandardCharsets.UTF_8, new char[] { '$', '1', ',', '0', '0', '0' }), Arguments.of("£1,000", StandardCharsets.ISO_8859_1, new char[] { '£', '1', ',', '0', '0', '0' }), Arguments.of("£1,000", StandardCharsets.UTF_8, new char[] { '£', '1', ',', '0', '0', '0' }), Arguments.of("€1,000", StandardCharsets.UTF_8, new char[] { '€', '1', ',', '0', '0', '0' }));
    }

    @ParameterizedTest
    @MethodSource("stringToByteArrayParams")
    void testStringToByteArray(String source, Charset charSet, byte[] expected) {
        byte[] actual = this.converter.convert(source, byte[].class, createCharsetOptions(charSet));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("stringToByteArrayParams")
    void testStringToByteBuffer(String source, Charset charSet, byte[] expected) {
        ByteBuffer actual = this.converter.convert(source, ByteBuffer.class, createCharsetOptions(charSet));
        assertThat(actual).isEqualTo(ByteBuffer.wrap(expected));
    }

    @ParameterizedTest
    @MethodSource("stringToByteArrayParams")
    void testByteArrayToString(String expected, Charset charSet, byte[] source) {
        String actual = this.converter.convert(source, String.class, createCharsetOptions(charSet));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("stringToCharArrayParams")
    void testCharArrayToString(String expected, Charset charSet, char[] source) {
        String actual = this.converter.convert(source, String.class, createCharsetOptions(charSet));
        assertThat(actual).isEqualTo(expected);
    }

    @ParameterizedTest
    @MethodSource("stringToCharArrayParams")
    void testStringToCharArray(String source, Charset charSet, char[] expected) {
        char[] actual = this.converter.convert(source, char[].class, createCharsetOptions(charSet));
        assertThat(actual).isEqualTo(expected);
    }

    public ConverterOptions createCharsetOptions(final Charset charset) {
        return new ConverterOptions() {

            @Override
            public <T> T getCustomOption(String name) {
                return null;
            }

            @Override
            public Charset getCharset() {
                return charset;
            }
        };
    }

    public ConverterOptions createCustomZones(final ZoneId sourceZoneId, final ZoneId targetZoneId) {
        return new ConverterOptions() {

            @Override
            public <T> T getCustomOption(String name) {
                return null;
            }

            @Override
            public ZoneId getZoneId() {
                return targetZoneId;
            }

            @Override
            public ZoneId getSourceZoneIdForLocalDates() {
                return sourceZoneId;
            }
        };
    }

    public static ConverterOptions createCustomBooleanCharacter(final Character trueChar, final Character falseChar) {
        return new ConverterOptions() {

            @Override
            public <T> T getCustomOption(String name) {
                return null;
            }

            @Override
            public Character trueChar() {
                return trueChar;
            }

            @Override
            public Character falseChar() {
                return falseChar;
            }
        };
    }

    public ConverterOptions chicagoZone() {
        return createCustomZones(CHICAGO, CHICAGO);
    }
}

