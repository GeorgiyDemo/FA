import java.io.*;
import java.util.stream.Collectors;

// Класс для работы с файлами
public class FileProcessing {

    String fileName;

    public FileProcessing(String fileName) {
        this.fileName = fileName;
    }

    //Чтение
    public String Read() throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(this.fileName));
        String lines = reader.lines().collect(Collectors.joining());
        reader.close();
        return lines;
    }

    //Запись
    public void Write(String data) throws IOException {

        BufferedWriter writer = new BufferedWriter(new FileWriter(this.fileName));
        writer.write(data);
        writer.close();
    }
}