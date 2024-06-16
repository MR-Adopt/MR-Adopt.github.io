## New input1:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("SECRETKEY");
    String plaintext = "HELLOWORLD";
```
Explanation: This input is valid because it uses a different keyword (SECRETKEY) than the original test case (KEYWORD). It also uses a different plaintext (HELLOWORLD) than the original test case (PLAYFAIR). This ensures that the encryption and decryption processes are tested with different inputs.

## New input2:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("JAVA");
    String plaintext = "JAVA";
```
Explanation: This input is valid because it uses a shorter keyword (JAVA) than the original test case (KEYWORD). It also uses the same plaintext (JAVA) as the original test case. This ensures that the encryption and decryption processes are tested with a shorter keyword and the same plaintext.

## New input3:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("LONGKEYWORD");
    String plaintext = "SHORTTEXT";
```
Explanation: This input is valid because it uses a longer keyword (LONGKEYWORD) than the original test case (KEYWORD). It also uses a shorter plaintext (SHORTTEXT) than the original test case (PLAYFAIR). This ensures that the encryption and decryption processes are tested with a longer keyword and a shorter plaintext.

## New input4:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "J";
```
Explanation: This input is valid because it uses the same keyword (KEYWORD) as the original test case. It also uses a single character plaintext (J) that is a single character in the keyword. This ensures that the encryption and decryption processes are tested with a single character plaintext.

## New input5:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JJ";
```
Explanation: This input is valid because it uses the same keyword (KEYWORD) as the original test case. It also uses a double character plaintext (JJ) that is a double character in the keyword. This ensures that the encryption and decryption processes are tested with a double character plaintext.
