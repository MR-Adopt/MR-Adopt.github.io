## New input1:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVA";
```
Explanation: This input is valid because it contains only uppercase letters and no repeated characters, which are required for the Playfair cipher. Additionally, it is a boundary case because it has a length of 4, which is one less than the required length of 5.

## New input2:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVAJAVA";
```
Explanation: This input is valid because it contains only uppercase letters and no repeated characters, which are required for the Playfair cipher. Additionally, it is a boundary case because it has a length of 7, which is one more than the required length of 5.

## New input3:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVAJAVAJAVA";
```
Explanation: This input is valid because it contains only uppercase letters and no repeated characters, which are required for the Playfair cipher. Additionally, it is a boundary case because it has a length of 10, which is equal to the required length of 5.

## New input4:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVAJAVAJAVAJAVA";
```
Explanation: This input is valid because it contains only uppercase letters and no repeated characters, which are required for the Playfair cipher. Additionally, it is a boundary case because it has a length of 15, which is more than the required length of 5.

## New input5:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVAJAVAJAVAJAVAJAVA";
```
Explanation: This input is valid because it contains only uppercase letters and no repeated characters, which are required for the Playfair cipher. Additionally, it is a boundary case because it has a length of 20, which is more than the required length of 5.
