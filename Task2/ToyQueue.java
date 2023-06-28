import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.PriorityQueue;

public class ToyQueue {
    public static void main(String[] args) {
        // Инициализация массивов с данными
        String[] ids = {"1", "2", "3"};
        String[] names = {"Кукла", "Мяч", "Машинка"};
        int[] frequencies = {3, 5, 2};

        // Заполнение массива объектами игрушек
        Toy[] toys = new Toy[3];
        for (int i = 0; i < 3; i++) {
            toys[i] = new Toy(ids[i], names[i], frequencies[i]);
        }

        // Создание очереди приоритетов и добавление игрушек
        PriorityQueue<Toy> toyQueue = new PriorityQueue<>();
        for (Toy toy : toys) {
            toyQueue.add(toy);
        }

        // Вызов метода poll() 10 раз и запись результата в файл
        try {
            FileWriter writer = new FileWriter("output.txt", StandardCharsets.UTF_8);
            for (int i = 0; i < 10; i++) {
                Toy toy = toyQueue.poll(); // Извлечение элемента из очереди
                if (toy != null) {
                    writer.write("Игрушка ID: " + toy.getId() + ", Название: " + toy.getName() + "\n");
                } else {
                    writer.write("Очередь пуста\n");
                }
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}