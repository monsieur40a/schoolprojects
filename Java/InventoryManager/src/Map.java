import java.util.Iterator;

public interface Map<K, V> extends ReadonlyMap<K, V>
{
    Set<Map.Entry<K, V>> entrySet();
    
    default V get(K key)
    {
        Entry<K,V> entry = entrySet().getMatch(new EntryImpl<K, V>(key));
        return entry == null ? null : entry.getValue();
    }

    default int size()
    {
        return entrySet().size();
    }

    default V put(K key, V value)
    {
        Map.Entry<K, V> entry = entrySet().add(new EntryImpl<K,V>(key));
        V previous = entry.getValue();
        entry.setValue(value);
        return previous;
    }

    default V remove(K key)
    {
        Map.Entry<K, V> removed = entrySet().remove(new EntryImpl<K,V>(key));
        return removed == null ? null : removed.getValue();
    }
    
    default Iterator<ReadonlyMap.Entry<K,V>> iterator()
    {
        Iterator<Map.Entry<K,V>> iterator = entrySet().iterator();

        return new Iterator<ReadonlyMap.Entry<K,V>>()
        {
            public boolean hasNext()
            {
                return iterator.hasNext();
            }

            public ReadonlyMap.Entry<K,V> next()
            {
                return iterator.next();
            }
        };
    }

    interface Entry<K, V> extends ReadonlyMap.Entry<K, V>
    {
        void setValue(V value);
    }

    static class EntryImpl<K, V> implements Entry<K, V>
    {
        private final K key;
        private V value;
        
        private EntryImpl(K key)
        {
            if (key == null)
            {
                throw new NullPointerException("key");
            }
            this.key = key;
        }

        public K getKey()
        {
            return key;
        }

        public V getValue()
        {
            return value;
        }

        public void setValue(V value)
        {
            this.value = value;
        }

        public boolean equals(Object other)
        {
            if (other instanceof ReadonlyMap.Entry)
            {
                ReadonlyMap.Entry<?,?> entry = (ReadonlyMap.Entry<?,?>) other;
                return key.equals(entry.getKey());
            }
            else
            {
                return false;
            }
        }

        public int hashCode()
        {
            return key.hashCode();
        }
    }
}
