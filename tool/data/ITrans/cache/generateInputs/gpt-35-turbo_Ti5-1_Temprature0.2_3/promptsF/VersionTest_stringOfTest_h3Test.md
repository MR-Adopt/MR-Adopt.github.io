# ORIGINAL TEST CASE
```java
@Test
public void stringOfTest() {
    String v = "1.0.0";
    String v1 = "1.0.0";
    Version version = Version.valueOf(v);
    Version version1 = Version.valueOf(v1);
    assertEquals(v, version.stringOf());
    assertEquals(v, Version.stringOf(version1));
}

```
SOURCE INPUT: `v`
FOLLOW UP INPUT: `version1`


# METHOD UNDER TEST
```java
/**
 * 构建Version。
 * <p>
 * 1.0、1.0-A1、1.1.0、1.1.0-A1
 * </p>
 *
 * @param version
 * @return
 * @throws IllegalArgumentException
 */
public static Version valueOf(String version) throws IllegalArgumentException {
    if (!isValidVersion(version))
        throw new IllegalArgumentException("illegal version : " + version);
    String[] vs = version.split(SPLITTER_D_REGEX);
    String major = vs[0];
    String minor = (vs.length > 1 ? vs[1] : null);
    String revision = (vs.length > 2 ? vs[2] : null);
    String build = null;
    if (revision != null) {
        String[] bs = revision.split(SPLITTER_L_REGEX);
        revision = bs[0];
        build = (bs.length > 1 ? bs[1] : null);
    } else if (minor != null) {
        String[] bs = minor.split(SPLITTER_L_REGEX);
        minor = bs[0];
        build = (bs.length > 1 ? bs[1] : null);
    } else if (major != null) {
        String[] bs = major.split(SPLITTER_L_REGEX);
        major = bs[0];
        build = (bs.length > 1 ? bs[1] : null);
    }
    return new Version(major, minor, revision, build);
}

/**
 * 返回{@linkplain Version}的字符串形式。
 *
 * @param version
 * @return
 */
public static String stringOf(Version version) {
    return version.stringOf();
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    String v = "2.0.0";
```

## New source input1:
```java
    String v = "1.1.0";
```

## New source input2:
```java
    String v = "1.0.1";
```

## New source input3:
```java
    String v = "1.0.0-A1";
```

## New source input4:
```java
    String v = "1.1.0-A1";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String v = "1.0.0";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.