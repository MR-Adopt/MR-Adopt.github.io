# METHOD UNDER TEST
```java
/**
 * 根据ip地址计算出long型的数据
 *
 * @param strIP IP V4 地址
 * @return long值
 */
public static long ipv4ToLong(String strIP) {
    if (isValidAddress(strIP)) {
        long[] ip = new long[4];
        // 先找到IP地址字符串中.的位置
        int position1 = strIP.indexOf(".");
        int position2 = strIP.indexOf(".", position1 + 1);
        int position3 = strIP.indexOf(".", position2 + 1);
        // 将每个.之间的字符串转换成整型
        ip[0] = Long.parseLong(strIP.substring(0, position1));
        ip[1] = Long.parseLong(strIP.substring(position1 + 1, position2));
        ip[2] = Long.parseLong(strIP.substring(position2 + 1, position3));
        ip[3] = Long.parseLong(strIP.substring(position3 + 1));
        return (ip[0] * 1_000_000_000) + (ip[1] * 1_000_000) + (ip[2] * 1_000) + ip[3];
    }
    return 0;
}

/**
 * 根据long值获取ip v4地址
 *
 * @param longIP IP的long表示形式
 * @return IP V4 地址
 */
public static String longToIpv4(long longIP) {
    final StringBuilder sb = new StringBuilder();
    // 直接右移24位
    sb.append((longIP / 1_000_000_000));
    sb.append(".");
    // 将高8位置0，然后右移16位
    sb.append(longIP / 1_000_000 % 1_000);
    sb.append(".");
    sb.append(longIP / 1_000 % 1_000);
    sb.append(".");
    sb.append(longIP % 1_000);
    return sb.toString();
}

```


# TEST CASE
```java
@Test
public void ipv4Test() {
    String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
    long ipLong = NetUtils.ipv4ToLong(ipStr1);
    long ipLong2 = 127000000001L;
    String ipStr2 = NetUtils.longToIpv4(ipLong2);
    Assert.assertEquals(ipStr2, ipStr1);
}

```
SOURCE INPUT: `ipStr1`
FOLLOW UP INPUT: `ipLong2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
String ipStr1 = NetUtils.LOCAL_LOOPBACK_IP;
long ipLong2 = 127000000001L;
```

## Input pair2:
```java
String ipStr1 = "192.168.0.1";
long ipLong2 = 192168000001L;
```

## Input pair3:
```java
String ipStr1 = "172.16.0.1";
long ipLong2 = 172016000001L;
```

## Input pair4:
```java
String ipStr1 = "255.255.255.255";
long ipLong2 = 255255255255L;
```

## Input pair5:
```java
String ipStr1 = "0.0.0.0";
long ipLong2 = 0L;
```

## Input pair6:
```java
String ipStr1 = "127.0.0.1";
long ipLong2 = 127000000001L;
```



# OUTPUT FORMAT
```java
public class NetUtilsTest_ipv4Test {
    public static long inputTransformation_ipv4Test(String ipStr1)  {
        // TODO
        long ipLong2 = 
		return ipLong2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.