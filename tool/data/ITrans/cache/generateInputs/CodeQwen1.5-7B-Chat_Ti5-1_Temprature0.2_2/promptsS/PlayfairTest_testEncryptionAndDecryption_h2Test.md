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
TEST INPUT: `playfairCipher`,`plaintext`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `playfairCipher`,`plaintext`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "PLAYFAIR";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 