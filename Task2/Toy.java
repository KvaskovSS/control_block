class Toy implements Comparable<Toy> {
    private String id;
    private String name;
    private int frequency;

    public Toy(String id, String name, int frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }

    @Override
    public int compareTo(Toy other) {
        // Сравнение по частоте выпадения игрушек
        return Integer.compare(this.frequency, other.frequency);
    }
}