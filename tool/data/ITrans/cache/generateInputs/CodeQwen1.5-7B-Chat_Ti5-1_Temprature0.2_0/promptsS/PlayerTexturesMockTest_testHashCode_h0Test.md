# ORIGINAL TEST CASE
```java
@Test
void testHashCode() throws MalformedURLException {
    // Assert that they both result into the same hashCode
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(new URL("https://github.com/skin"));
    PlayerTexturesMock otherPlayerTexturesMock = new PlayerTexturesMock(profile);
    otherPlayerTexturesMock.setSkin(new URL("https://github.com/skin"));
    Assertions.assertEquals(playerTexturesMock.hashCode(), otherPlayerTexturesMock.hashCode());
}

```
TEST INPUT: `playerTexturesMock`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    ProfileProperty property = getProperty();
    return (property == null) ? 0 : property.hashCode();
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `playerTexturesMock`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(new URL("https://github.com/skin"));
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 