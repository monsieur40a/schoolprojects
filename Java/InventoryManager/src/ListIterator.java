import java.util.Iterator;

public interface ListIterator<T> extends Iterator<T>
{
    void add(T element);
    void remove();
    void set(T element);
}