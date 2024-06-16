# ORIGINAL TEST CASE
```java
@Test
public void testEncryptionAndDecryption() {
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "PLAYFAIR";
    String encryptedText = playfairCipher.encrypt(plaintext);
    String textTodecrypt = "SHHAHRFB";
    String decryptedText = playfairCipher.decrypt(textTodecrypt);
    assertEquals(plaintext, decryptedText);
}

```
SOURCE INPUT: `playfairCipher`,`plaintext`
FOLLOW UP INPUT: `textTodecrypt`


# METHOD UNDER TEST
```java
public String encrypt(String plaintext) {
    plaintext = prepareText(plaintext.replace("J", "I"));
    StringBuilder ciphertext = new StringBuilder();
    for (int i = 0; i < plaintext.length(); i += 2) {
        char char1 = plaintext.charAt(i);
        char char2 = plaintext.charAt(i + 1);
        int[] pos1 = findPosition(char1);
        int[] pos2 = findPosition(char2);
        int row1 = pos1[0];
        int col1 = pos1[1];
        int row2 = pos2[0];
        int col2 = pos2[1];
        if (row1 == row2) {
            ciphertext.append(matrix[row1][(col1 + 1) % 5]);
            ciphertext.append(matrix[row2][(col2 + 1) % 5]);
        } else if (col1 == col2) {
            ciphertext.append(matrix[(row1 + 1) % 5][col1]);
            ciphertext.append(matrix[(row2 + 1) % 5][col2]);
        } else {
            ciphertext.append(matrix[row1][col2]);
            ciphertext.append(matrix[row2][col1]);
        }
    }
    return ciphertext.toString();
}

public String decrypt(String ciphertext) {
    StringBuilder plaintext = new StringBuilder();
    for (int i = 0; i < ciphertext.length(); i += 2) {
        char char1 = ciphertext.charAt(i);
        char char2 = ciphertext.charAt(i + 1);
        int[] pos1 = findPosition(char1);
        int[] pos2 = findPosition(char2);
        int row1 = pos1[0];
        int col1 = pos1[1];
        int row2 = pos2[0];
        int col2 = pos2[1];
        if (row1 == row2) {
            plaintext.append(matrix[row1][(col1 + 4) % 5]);
            plaintext.append(matrix[row2][(col2 + 4) % 5]);
        } else if (col1 == col2) {
            plaintext.append(matrix[(row1 + 4) % 5][col1]);
            plaintext.append(matrix[(row2 + 4) % 5][col2]);
        } else {
            plaintext.append(matrix[row1][col2]);
            plaintext.append(matrix[row2][col1]);
        }
    }
    return plaintext.toString();
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "HELLO";
```

## New source input1:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "WORLD";
```

## New source input2:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVA";
```

## New source input3:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "PROGRAMMING";
```

## New source input4:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "12345";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "PLAYFAIR";
    String textTodecrypt = "SHHAHRFB";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.