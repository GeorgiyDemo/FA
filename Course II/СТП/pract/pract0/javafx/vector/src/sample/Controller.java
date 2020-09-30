package sample;

import javafx.scene.control.Label;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;

/*
Класс на проверку корректности ввода данных
 */
class FilterInput{

    private String v1String;
    private String v2String;
    private int [] v1result;
    private int [] v2result;

    public FilterInput(String v1, String v2){
        v1String = v1;
        v2String = v2;

        v1result = new int[3];
        v2result = new int[3];
    }


    /*
    Валидация введенных данных
     */
    public boolean Validate(){

        try {
            String[] buffer = v1String.split(",");

            for (int i = 0; i < buffer.length; i++)
                v1result[i] = Integer.parseInt(buffer[i]);

            buffer = v2String.split(",");
            for (int i = 0; i < buffer.length; i++)
                v1result[i] = Integer.parseInt(buffer[i]);

            return true;
        }
        catch(Exception e) {
            return false;
        }
    }

    public int[] getV1result() {
        return v1result;
    }

    public int[] getV2result() {
        return v2result;
    }




}
/*
Контроллер MainScene
 */
public class Controller {

    @FXML
    private TextField vectorATextField;
    @FXML
    private TextField vectorBTextField;
    @FXML
    private Label lengthALabel;
    @FXML
    private  Label lengthBLabel;
    @FXML
    private  Label dotProductLabel;
    @FXML
    private  Label crossProductLabel;
    @FXML
    private  Label vectorCosLabel;
    @FXML
    private  Label summLabel;
    @FXML
    private  Label diffLabel;

    /*
    Основной обработчик нажатия на button
     */
    @FXML
    private void mainButtonClick() {
        String vectorAString = vectorATextField.getText();
        String vectorBString = vectorBTextField.getText();
        FilterInput filter = new FilterInput(vectorAString, vectorBString);

        //Если успешно прошли валидацию данных
        if (filter.Validate()){

            int [] buf1 = filter.getV1result();
            int [] buf2 = filter.getV2result();

            Vector vectorA = new Vector(buf1[0], buf1[1], buf1[2]);
            Vector vectorB = new Vector(buf2[0], buf2[1], buf2[2]);

            lengthALabel.setText("Длина вектора А:\n" + vectorA.length());
            lengthBLabel.setText("Длина вектора B:\n" + vectorB.length());

            dotProductLabel.setText("Скалярное произведение вектора A и B:\n" + vectorA.DotProduct(vectorB));
            crossProductLabel.setText("Векторное произведение вектора A и B:\n"+vectorA.CrossProduct(vectorB).value());
            vectorCosLabel.setText("Угол между векторами A и B:\n" + vectorA.VectorCos(vectorB));

            summLabel.setText("Сумма векторов A и B:\n"+vectorA.summ(vectorB).value());
            diffLabel.setText("Разность векторов A и B:\n"+vectorA.difference(vectorB).value());

        }
        else {
            System.out.println("Некорректные данные");
        }


    }
}
