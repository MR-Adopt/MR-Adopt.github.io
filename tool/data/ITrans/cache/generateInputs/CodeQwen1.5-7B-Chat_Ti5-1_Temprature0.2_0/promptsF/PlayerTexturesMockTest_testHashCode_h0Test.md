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
SOURCE INPUT: `playerTexturesMock`
FOLLOW UP INPUT: `otherPlayerTexturesMock`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    ProfileProperty property = getProperty();
    return (property == null) ? 0 : property.hashCode();
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(new URL("https://github.com/skin1"));
```

## New source input1:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(null);
```

## New source input2:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(new URL("https://github.com/skin"));
    playerTexturesMock.setCape(new URL("https://github.com/cape"));
```

## New source input3:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(new URL("https://github.com/skin"));
    playerTexturesMock.setCape(null);
```

## New source input4:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(null);
    playerTexturesMock.setCape(null);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    PlayerTexturesMock playerTexturesMock = new PlayerTexturesMock(profile);
    playerTexturesMock.setSkin(new URL("https://github.com/skin"));
    PlayerTexturesMock otherPlayerTexturesMock = new PlayerTexturesMock(profile);
    otherPlayerTexturesMock.setSkin(new URL("https://github.com/skin"));
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.