// fort0142
public class Random {
    private int p1, p2, m, seed;

    public Random(int p1, int p2, int m) {
        if (m <= 0) {
            throw new IllegalArgumentException("Invalid argument for maximum for Random instantiation."
                    + " Create a new random object with m > 0 to avoid dividing by zero");
        } else {
            this.p1 = p1;
            this.p2 = p2;
            this.m = m;
            this.seed = 0;
        }
    }

    public void setSeed(int seed) {this.seed = seed;}

    public int getSeed() {return seed;}

    public int getMaximum() {return m;}

    public int random() {
        return seed = ((p1 * seed) + p2) % getMaximum();
    }

    public int randomInteger(int lower, int upper) {
        if (lower > upper) { // Swap bounds if improper arguments given.
            int temp = lower;
            lower = upper;
            upper = temp;
        }
//        Random generates int between 0 and max. Remainder + lower bound gives us randomInt in range.
        return random() % (upper - lower + 1) + lower;
    }

    public boolean randomBoolean() {
        int oddOrEven = randomInteger(1, 2);
        if (oddOrEven % 2 == 0) { // Simple even or odd test utilizing randomInt generator.
            return true;
        } else {
            return false;
        }
    }

    public double randomDouble(double lower, double upper) {
        if (lower > upper) { // Swap bounds if improper arguments given.
            double temp = lower;
            lower = upper;
            upper = temp;
        }
//        Get number between 0 and 1 as a double, times that by range your interested in add back in lower to correct bounds.
        return ((((double)random()) / (getMaximum() - 1) * (upper - lower) + lower));
    }

    public static void main(String[] args) {
        System.out.println("Creating new Random Object for testing Random(7919, 65537, 102611)" + "\n");
        Random newRandomObj = new Random(7919, 65537, 102611);

    }
}
