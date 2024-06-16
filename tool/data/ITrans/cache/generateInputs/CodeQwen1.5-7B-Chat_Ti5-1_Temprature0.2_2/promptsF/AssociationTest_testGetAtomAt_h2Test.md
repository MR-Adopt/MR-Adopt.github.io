# ORIGINAL TEST CASE
```java
@Test
void testGetAtomAt() {
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    // Assertions.assertEquals(c, association.getAtomAt(0));
    // Assertions.assertEquals(o, association.getAtomAt(1));
    int position = 0;
    association.setAtomAt(n, position);
    Association association2 = new Association(n, o);
    int position2 = 0;
    Assertions.assertEquals(n, association2.getAtomAt(position2));
}

```
SOURCE INPUT: `association`,`n`,`position`
FOLLOW UP INPUT: `association2`,`position2`


# METHOD UNDER TEST
```java
/**
 * Sets an Atom in this Association.
 *
 * @param   atom  The atom to be set
 * @param   position  The position in this Association where the atom is to be inserted
 *
 * @see     #getAtomAt
 */
public void setAtomAt(IAtom atom, int position) {
    atoms[position] = atom;
    notifyChanged();
}

/**
 * Returns an Atom from this Association.
 *
 * @param   position  The position in this bond where the atom is
 * @return            The atom at the specified position
 *
 * @see     #setAtomAt
 */
public IAtom getAtomAt(int position) {
    return atoms[position];
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 1;
```

## New source input1:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = -1;
```

## New source input2:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 2;
```

## New source input3:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 0;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 0;
    Association association2 = new Association(n, o);
    int position2 = 0;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.