## New input1:
```java
    byte[] testDataBytes = new byte[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31};
```
Explanation: This input consists of 32 bytes, each ranging from 0 to 31. This covers the full range of possible byte values, ensuring that the encoding and decoding processes are thoroughly tested.

## New input2:
```java
    byte[] testDataBytes = new byte[]{-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31};
```
Explanation: This input consists of 32 bytes, each ranging from -1 to -31. This covers the full range of possible negative byte values, ensuring that the encoding and decoding processes are thoroughly tested.

## New input3:
```java
    byte[] testDataBytes = new byte[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
```
Explanation: This input consists of 32 bytes, all of which are 0. This covers the case where the input data consists entirely of zeros, ensuring that the encoding and decoding processes are thoroughly tested.

## New input4:
```java
    byte[] testDataBytes = new byte[]{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
```
Explanation: This input consists of 32 bytes, all of which are 1. This covers the case where the input data consists entirely of ones, ensuring that the encoding and decoding processes are thoroughly tested.

## New input5:
```java
    byte[] testDataBytes = new byte[]{(byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF, (byte) 0xFF};
```
Explanation: This input consists of 32 bytes, each ranging from 255 to 255. This covers the full range of possible byte values, ensuring that the encoding and decoding processes are thoroughly tested.
