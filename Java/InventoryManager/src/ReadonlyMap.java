public interface ReadonlyMap<K, V>
    extends Iterable<ReadonlyMap.Entry<K,V>>
{
    V get(K key);
    int size();

    interface Entry<K, V>
    {
        K getKey();
        V getValue();
    }
}
