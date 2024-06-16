# ORIGINAL TEST CASE
```java
@Test
public void isEqualTest() {
    String v1 = "1.0";
    String v2 = "1.10";
    String v3 = "1.0";
    Version a = Version.valueOf(v1);
    Version b = Version.valueOf(v2);
    Version c = Version.valueOf(v3);
    assertFalse(a.isEqual(b));
}

```
TEST INPUT: `v1`


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

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `v1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String v1 = "1.0";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 