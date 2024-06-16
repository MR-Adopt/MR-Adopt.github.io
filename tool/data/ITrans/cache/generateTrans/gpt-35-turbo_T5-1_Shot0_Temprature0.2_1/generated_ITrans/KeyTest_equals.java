package io.bootique.di;

import org.junit.jupiter.api.Test;
import javax.inject.Qualifier;
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.util.Map;


import io.bootique.di.Key;
import io.bootique.di.Key.*;
import java.util.List;
import java.util.Arrays;

public class KeyTest_equals {
    public static Class<?> inputTransformation_equals(Class<?> type1)  {
        Class<?> type2 = type1;
        return type2;
    }
}