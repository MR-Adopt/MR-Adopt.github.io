## New input pair0:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H2 2020";
    int year = 2020;
    int half = 2;
```

## New input pair1:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 1999";
    int year = 1999;
    int half = 1;
```

## New input pair2:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H3 2000";
    int year = 2000;
    int half = 3;
```

## New input pair3:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 1800";
    int year = 1800;
    int half = 1;
```

## New input pair4:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 2100";
    int year = 2100;
    int half = 1;
```

## Code used to generate follow-up input0:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H2 2020";
    int year = 2020;
    int half = 2;
```

## Code used to generate follow-up input1:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 1999";
    int year = 1999;
    int half = 1;
```

## Code used to generate follow-up input2:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H3 2000";
    int year = 2000;
    int half = 3;
```

## Code used to generate follow-up input3:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 1800";
    int year = 1800;
    int half = 1;
```

## Code used to generate follow-up input4:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 2100";
    int year = 2100;
    int half = 1;
```

The inferred relation is that the text input contains the half-of-year and year, and the corresponding output is the parsed YearHalf object. The new source inputs satisfy this relation by providing different half-of-years and years, and the corresponding follow-up inputs generate the expected YearHalf objects.
