import static org.junit.Assert.*;

public class Lab4Test {


    @org.junit.Test
    public void testCommonEnd() {
        assertEquals(true, o.commonEnd(new int[]{0, 2, 3},new int[]{0, 4, 7}));
    }

    @org.junit.Test
    public void sameFirstLast() {
        assertEquals(true, o.sameFirstLast(new int[]{0, 2, 5, 0}) );
        assertEquals(false, o.sameFirstLast(new int[]{5, 2, 5, 0}) );

    }

    @org.junit.Test
    public void firstLast6() {
        assertEquals(true, o.firstLast6(new int[]{0, 4, 4, 6}));
        assertEquals(false, o.firstLast6(new int[]{0, 4, 4, 2}));

    }

    @org.junit.Test
    public void plusTwo() {
        assertArrayEquals(new int[]{1, 2, 3, 4},  o.plusTwo(new int[]{1, 2},new int[]{3, 4}));
    }

    Lab4 o = new Lab4();


}