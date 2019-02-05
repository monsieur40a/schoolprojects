import java.util.Comparator;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class ArrayList<T> implements List<T>
{
    private Object[] array;
    private int size;

    public ArrayList(int capacity)
    {
        array = new Object[capacity];
    }

    public int size()
    {
        return size;
    }

    @SuppressWarnings("unchecked")
    public T get(int index)
    {
        if (index >= size)
        {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        else
        {
            return (T) array[index];
        }
    }

    public void set(int index, T element)
    {
        if (index >= size)
        {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        else
        {
            array[index] = element;
        }
    }

    public void clear()
    {
        size = 0;
    }

    private void resize(int newCapacity)
    {
        Object[] original = array;
        array = new Object[newCapacity];

        for (int i = 0; i < size; i++)
        {
            array[i] = original[i];
        }
    }

    public void add(T element)
    {
        if (size == array.length)
        {
            resize(size * 2);
        }

        array[size] = element;
        size++;
    }


    public void addAll(T[] elements)
    {
        for (T v : elements)
        {
            add(v);
        }
    }

    private void shiftRight(int index, int amount)
    {
        for (int k = size - 1; k >= index; k--)
        {
            array[k + amount] = array[k];
        }
    }

    public void add(int index, T element)
    {
        if (index > size)
        {
            throw new IndexOutOfBoundsException(
                    "Index: " + index + ", Size: " + size);
        }

        if (size == array.length)
        {
            resize(size * 2);
        }

        shiftRight(index, 1);
        array[index] = element;
        size++;
    }

    public void addFirst(T element)
    {
        add(0, element);
    }

    public void addLast(T element)
    {
        add(element);
    }

    public void addAll(int index, T[] elements)
    {
        if (index > size)
        {
            throw new IndexOutOfBoundsException(
                    "Index: " + index + ", Size: " + size);
        }

        if (size + elements.length > array.length)
        {
            resize((size + elements.length) * 2);
        }

        shiftRight(index, elements.length);

        for (int k = 0; k < elements.length; k++)
        {
            array[index + k] = elements[k];
        }

        size += elements.length;
    }

    public void remove()
    {
        if (size <= 0)
        {
            throw new EmptyListException();
        }
        else
        {
            size--;
        }
    }

    private void shiftLeft(int index, int amount)
    {
        for (int k = index; k + amount < size; k++)
        {
            array[k] = array[k + amount];
        }
    }

    public void remove(int index, int count)
    {
        if (index + count > size)
        {
            throw new IndexOutOfBoundsException(
                    "Index: " + size + ", Size: " + size);
        }
        else
        {
            shiftLeft(index, count);
            size -= count;
        }
    }

    public void remove(int index)
    {
        remove(index, 1);
    }

    public void removeFirst()
    {
        remove(0);
    }

    public void removeLast()
    {
        remove();
    }

    public void sort(Comparator<T> c) // Sorts in descending order, switched get(j), n
    {
        for (int i = 1; i < size; i++)
        {
            T n = get(i);

            for (int j = i - 1; j >= 0 && c.compare(n, get(j)) < 0; j--)
            {
                array[j + 1] = get(j);
                array[j] = n;
            }
        }
    }

    public String toString()
    {
        if (size == 0)
        {
            return "[]";
        }
        else
        {
            StringBuilder stringBuilder = new StringBuilder("[");
            stringBuilder.append(get(0));

            for (int i = 1; i < size; i++)
            {
                stringBuilder.append(", ");
                stringBuilder.append(get(i));
            }

            stringBuilder.append("]");
            return stringBuilder.toString();
        }
    }

    // Example of an static nested class (see extra material on inner classes)
    private static class ListIteratorImpl<T> implements ListIterator<T>
    {
        private int i = -1;
        private ArrayList<T> list;

        private ListIteratorImpl(ArrayList<T> list)
        {
            this.list = list;
        }

        public boolean hasNext()
        {
            return i + 1 < list.size();
        }

        public T next()
        {
            if (!hasNext())
            {
                throw new NoSuchElementException();
            }
            i++;
            return list.get(i);
        }

        public void set(T element)
        {
            list.set(i, element);
        }

        public void add(T element)
        {
            i++;
            list.add(i, element);
        }

        public void remove()
        {
            if (i == -1)
            {
                throw new IllegalStateException(
                        "Remove not allowed in the current state.");
            }

            list.remove(i);
            i--;
        }
    }

    public ListIterator<T> listIterator()
    {
        return new ListIteratorImpl<T>(this);
    }

    public Iterator<T> iterator()
    {
        return new ListIteratorImpl<T>(this);
    }
}