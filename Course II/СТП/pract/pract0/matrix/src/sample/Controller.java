package sample;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

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
    private Label dotProductLabel;
    @FXML
    private Label crossProductLabel;
    @FXML
    private Label vectorCosLabel;
    @FXML
    private Label summLabel;
    @FXML
    private Label diffLabel;
    @FXML
    private Label wrongInputLabel;


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

            wrongInputLabel.setVisible(false);
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
            wrongInputLabel.setVisible(true);
        }


    }
}
