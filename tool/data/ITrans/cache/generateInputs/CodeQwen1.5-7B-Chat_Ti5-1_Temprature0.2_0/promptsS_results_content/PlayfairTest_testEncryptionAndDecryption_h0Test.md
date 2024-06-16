## New input1:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVA";
```
Explanation: This input is valid because it is a simple string of four characters, which is a common scenario in encryption. The string "JAVA" is also a valid input for the Playfair cipher, as it contains no repeated characters.

## New input2:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "HELLO WORLD";
```
Explanation: This input is valid because it contains spaces and is a common scenario in encryption. The string "HELLO WORLD" is also a valid input for the Playfair cipher, as it contains no repeated characters.

## New input3:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JJAVA";
```
Explanation: This input is valid because it contains repeated characters, which is a common scenario in encryption. The string "JJAVA" is also a valid input for the Playfair cipher, as it contains no repeated characters.

## New input4:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JJ";
```
Explanation: This input is valid because it contains only two characters, which is a common scenario in encryption. The string "JJ" is also a valid input for the Playfair cipher, as it contains no repeated characters.

## New input5:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVAJAVA";
```
Explanation: This input is valid because it contains repeated characters, which is a common scenario in encryption. The string "JAVAJAVA" is also a valid input for the Playfair cipher, as it contains no repeated characters.
