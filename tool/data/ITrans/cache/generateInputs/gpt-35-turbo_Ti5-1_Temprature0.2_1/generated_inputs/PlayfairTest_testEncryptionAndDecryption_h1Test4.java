package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h1Test4 {

    @Test
    public void testEncryptionAndDecryption_h1Test4() {
PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
String plaintext = "12345";
String textTodecrypt = playfairCipher.encrypt(plaintext);
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

