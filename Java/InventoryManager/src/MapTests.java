import java.util.Comparator;

// Tests one of several Set implementations.
public class MapTests
{
    public static void main(String[] args)
    {
        Map<String, Integer> map = new HashMap<String, Integer>(10);

        System.out.println();
        System.out.println("Putting: ");
        for (int i = 0; i < args.length; i++)
        {
            int k = (int)Math.floor(Math.random() * 100);
            System.out.print(args[i] + ":" + k + "(" + map.put(args[i], k) + ") ");
            
            if (map.get(args[i]) != k)
            {
                System.out.print("[FAIL] ");
            }
        }
        System.out.println();

        System.out.println("Size: " + map.size());
        
        for (ReadonlyMap.Entry<String, Integer> e : map.entrySet())
        {
            System.out.print(e.getKey() + ":" + e.getValue() + " ");
        }
        System.out.println();
        
        for (int i = 0; i < args.length; i++)
        {
            System.out.print(args[i] + ":" + map.get(args[i]) + " ");
        }
        System.out.println();

        System.out.println();
        System.out.println("Removing: ");
        int removeCount = 0;
        for (int i = 1; i < args.length; i += 2)
        {
            Integer result = map.remove(args[i]);
            System.out.print(args[i] + "(" + result + ") ");
            removeCount += (result == null ? 0 : 1);
            
            if (map.get(args[i]) != null)
            {
                System.out.print("[FAIL] ");
            }
        }
        System.out.println();   
        System.out.println("Removed: " + removeCount);
        System.out.println("Size: " + map.size());

        for (ReadonlyMap.Entry<String, Integer> e : map.entrySet())
        {
            System.out.print(e.getKey() + ":" + e.getValue() + " ");
        }
        System.out.println();

        for (int i = 0; i < args.length; i++)
        {
            System.out.print(args[i] + ":" + map.get(args[i]) + " ");
        }
        System.out.println();

        System.out.println();
        System.out.println("Redundant removing: ");
        removeCount = 0;
        for (int i = 1; i < args.length; i += 2)
        {
            Integer result = map.remove(args[i]);
            System.out.print(args[i] + "(" + result + ") ");
            removeCount += (result == null ? 0 : 1);
            
            if (map.get(args[i]) != null)
            {
                System.out.print("[FAIL] ");
            }
        }
        System.out.println();   
        System.out.println("Removed: " + removeCount);
        System.out.println("Size: " + map.size());
        
        for (ReadonlyMap.Entry<String, Integer> e : map.entrySet())
        {
            System.out.print(e.getKey() + ":" + e.getValue() + " ");
        }
        System.out.println();
        
        for (int i = 0; i < args.length; i++)
        {
            System.out.print(args[i] + ":" + map.get(args[i]) + " ");
        }
        System.out.println();

        System.out.println();
        System.out.println("Overwriting: ");
        for (int i = 0; i < args.length; i += 4)
        {
            int k = (int)Math.floor(Math.random() * 100);
            System.out.print(args[i] + ":" + k + "(" + map.put(args[i], k) + ") ");
            
            if (map.get(args[i]) != k)
            {
                System.out.print("[FAIL] ");
            }
        }
        System.out.println();

        System.out.println("Size: " + map.size());
        
        for (ReadonlyMap.Entry<String, Integer> e : map.entrySet())
        {
            System.out.print(e.getKey() + ":" + e.getValue() + " ");
        }
        System.out.println();
        
        for (int i = 0; i < args.length; i++)
        {
            System.out.print(args[i] + ":" + map.get(args[i]) + " ");
        }
        System.out.println();
    }
}