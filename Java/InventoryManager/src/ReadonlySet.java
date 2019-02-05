public interface ReadonlySet<T> extends Iterable<T>
{
    T getMatch(T item);
    int size();
}
