## New input1:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 2).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H2 2020";
```
Explanation: This input is valid because it changes the half-of-year value from 1 to 2, and the year value from 2012 to 2020. This will result in a valid YearHalf object.

## New input2:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 1990";
```
Explanation: This input is valid because it remains the half-of-year value as 1, and the year value changes from 2012 to 1990. This will result in a valid YearHalf object.

## New input3:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 2).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H2 2050";
```
Explanation: This input is valid because it changes the half-of-year value from 1 to 2, and the year value changes from 2012 to 2050. This will result in a valid YearHalf object.

## New input4:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 2100";
```
Explanation: This input is valid because it remains the half-of-year value as 1, and the year value changes from 2012 to 2100. This will result in a valid YearHalf object.

## New input5:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 2).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H2 2000";
```
Explanation: This input is valid because it changes the half-of-year value from 1 to 2, and the year value changes from 2012 to 2000. This will result in a valid YearHalf object.
