public class HashMap<K,V> implements Map<K,V>
{
    private HashSet<Map.Entry<K,V>> entrySet;

    public HashMap(int capacity)
    {
        entrySet = new HashSet<Map.Entry<K,V>>(capacity);
    }

    public Set<Map.Entry<K,V>> entrySet()
    {
        return entrySet;
    }
}
