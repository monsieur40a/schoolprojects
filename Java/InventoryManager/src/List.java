import java.util.Comparator;

public interface List<T> extends ReadonlyList<T>
{
    void addFirst(T element);
    void addLast(T element);
    void add(int index, T element);

    void removeFirst();
    void removeLast();
    void remove(int index);

    void set(int index, T element);
    void sort(Comparator<T> c);
    void clear();

    ListIterator<T> listIterator();
}