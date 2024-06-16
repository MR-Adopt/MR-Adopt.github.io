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
TEST INPUT: `association`,`n`,`position`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `association`,`n`,`position`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Atom c = new Atom("C");
    Atom o = new Atom("O");
    Atom n = new Atom("N");
    Association association = new Association(c, o);
    int position = 0;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 