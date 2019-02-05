import java.util.Iterator;
import java.util.NoSuchElementException;

public class HashSet<T> implements Set<T>
{
    private Object[] array;
    private boolean[] disabled;
    private int garbage;
    private int size;

    public HashSet(int capacity)
    {
        array = new Object[2 * capacity];
        disabled = new boolean[2 * capacity];
    }

    public int size()
    {
        return size;
    }

    // Subroutine that returns either the index of an item
    // or an index where the item could be inserted.
    private static int hashSearch(Object[] array, Object item)
    {
        // Transform hash code into a legal array index
        int i = Math.abs(item.hashCode() % array.length);

        // Linear probing
        while (array[i] != null && !array[i].equals(item))
        {
            i = (i + 1) % array.length;
        }

        return i;
    }

    private void resize(int newCapacity)
    {
        Object[] newArray = new Object[newCapacity];

        for (T item : this)
        {
            int index = hashSearch(newArray, item);
            newArray[index] = item;
        }

        array = newArray;
        disabled = new boolean[array.length];
        garbage = 0;
    }

    @SuppressWarnings("unchecked")
    public T getMatch(T item)
    {
        int index = hashSearch(array, item);
        return disabled[index] ? null : (T) array[index];
    }

    @SuppressWarnings("unchecked")
    public T add(T item)
    {
        if (2 * (size + garbage) >= array.length)
        {
            resize(4 * size);
        }

        int index = hashSearch(array, item);
        if (array[index] == null || disabled[index])
        {
            array[index] = item;
            size++;

            if (disabled[index])
            {
                disabled[index] = false;
                garbage--;
            }

            return item;
        }
        else
        {
            return (T) array[index];
        }
    }

    @SuppressWarnings("unchecked")
    public T remove(T item)
    {
        int index = hashSearch(array, item);
        if (array[index] == null || disabled[index])
        {
            return null;
        }
        else
        {
            disabled[index] = true;
            garbage++;
            size--;
            return (T)array[index];
        }
    }

    public Iterator<T> iterator()
    {
        return new IteratorImpl<T>(array, disabled);
    }

    // Static nested class (see extra material on inner classes)
    private static class IteratorImpl<T> implements Iterator<T>
    {
        private int current = -1;
        private int next = -1;
        private Object[] array;
        private boolean[] disabled;

        private IteratorImpl(Object[] array, boolean[] disabled)
        {
            this.array = array;
            this.disabled = disabled;
            findNext();
        }

        private void findNext()
        {
            do
            {
                next++;
            }
            while(next < array.length && (array[next] == null || disabled[next]));
        }

        public boolean hasNext()
        {
            return next < array.length;
        }

        @SuppressWarnings("unchecked")
        public T next()
        {
            if (!hasNext())
            {
                throw new NoSuchElementException();
            }

            current = next;
            findNext();
            return (T)array[current];
        }
    }
}
