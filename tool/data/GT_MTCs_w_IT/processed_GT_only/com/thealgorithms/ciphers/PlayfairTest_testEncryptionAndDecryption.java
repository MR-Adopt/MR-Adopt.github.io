package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption {

    @Test
    public void testEncryptionAndDecryption_h() {
        PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");

        String plaintext = "PLAYFAIR";
        String encryptedText = playfairCipher.encrypt(plaintext);
        assertEquals("SHHAHRFB", encryptedText);
        String textTodecrypt = "SHHAHRFB";
        String decryptedText = playfairCipher.decrypt(textTodecrypt);

        assertEquals(plaintext, decryptedText);
    }

    public static String inputTransformation_testEncryptionAndDecryption(PlayfairCipher playfairCipher, String plaintext) {
        String encryptedText = playfairCipher.encrypt(plaintext);
        return encryptedText;
    }


    @Test
    public void testEncryptionAndDecryption_IT() {
        PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");

        String plaintext = "PLAYFAIR";
        String encryptedText = playfairCipher.encrypt(plaintext);
        assertEquals("SHHAHRFB", encryptedText);
        String textTodecrypt = inputTransformation_testEncryptionAndDecryption(playfairCipher, plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);

        assertEquals(plaintext, decryptedText);
    }
}